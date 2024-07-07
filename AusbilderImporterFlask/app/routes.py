import pandas as pd
import configparser
import glob
import os
import chardet
import logging
from datetime import datetime
from flask import render_template, request, redirect, url_for, jsonify, flash, session
from werkzeug.utils import secure_filename
from app import app, cache
import subprocess

logging.debug("routes.py loaded")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'csv'}

def read_ini_file(ini_path):
    logging.debug(f"Reading INI file from {ini_path}")
    config = configparser.ConfigParser()
    config.read(ini_path)
    logging.debug(f"Sections found in config: {config.sections()}")

    if 'FILTER' not in config:
        raise KeyError("FILTER section not found in config.ini")
    if 'Classes' not in config['FILTER']:
        raise KeyError("Classes key not found in FILTER section of config.ini")

    classes = config['FILTER']['Classes'].split(',') if config['FILTER']['Classes'] else []
    blacklist = [str(id).strip() for id in config['BLACKLIST']['IDs'].split(',')] if 'BLACKLIST' in config and 'IDs' in config['BLACKLIST'] and config['BLACKLIST']['IDs'] else []
    logging.debug(f"Read classes: {classes}")
    logging.debug(f"Read blacklist: {blacklist}")
    return classes, blacklist

def write_ini_file(ini_path, classes, blacklist):
    logging.debug(f"Writing INI file to {ini_path}")
    config = configparser.ConfigParser()
    config['FILTER'] = {'Classes': ','.join(classes)}
    config['BLACKLIST'] = {'IDs': ','.join(blacklist)}
    with open(ini_path, 'w') as configfile:
        config.write(configfile)
    logging.debug(f"Wrote classes: {classes}")
    logging.debug(f"Wrote blacklist: {blacklist}")

def get_latest_csv(directory):
    logging.debug(f"Searching for CSV files in {directory}")
    csv_files = glob.glob(os.path.join(directory, '*.csv'))
    logging.debug(f"CSV files found: {csv_files}")
    if not csv_files:
        return None
    latest_csv = max(csv_files, key=os.path.getctime)
    logging.debug(f"Latest CSV file: {latest_csv}")
    return latest_csv

def detect_encoding(file_path):
    logging.debug(f"Detecting encoding for file {file_path}")
    with open(file_path, 'rb') as f:
        raw_data = f.read(10000)
    result = chardet.detect(raw_data)
    logging.debug(f"Detected encoding: {result['encoding']}")
    return result['encoding']

def filter_csv_by_classes_and_blacklist(csv_path, classes, blacklist, output_path):
    logging.debug(f"Filtering CSV file {csv_path}")
    encoding = detect_encoding(csv_path)
    df = pd.read_csv(csv_path, delimiter=';', encoding=encoding)
    logging.debug(f"CSV columns: {df.columns}")
    
    if classes:
        df = df[df['Klasse'].isin(classes)]
    if blacklist:
        df = df[~df['Interne ID-Nummer'].astype(str).isin(blacklist)]
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, sep=';', encoding='utf-8-sig')
    logging.debug(f"Filtered CSV saved to {output_path}")

@app.route('/')
def index():
    logging.debug("Index route accessed")
    ini_path = os.path.join(os.getcwd(), 'config.ini')
    classes, blacklist = read_ini_file(ini_path)
    csv_path = get_latest_csv(os.getcwd()) or session.get('uploaded_csv')  # Suche nach CSV-Dateien im aktuellen Verzeichnis oder Upload-Verzeichnis

    students = []
    if csv_path:
        encoding = detect_encoding(csv_path)
        df = pd.read_csv(csv_path, delimiter=';', encoding=encoding)
        df = df.sort_values(by=['Klasse', 'Nachname'])
        df['Interne ID-Nummer'] = df['Interne ID-Nummer'].astype(str)
        students = df[['Interne ID-Nummer', 'Vorname', 'Nachname', 'Klasse']].to_dict(orient='records')
    else:
        flash("Keine CSV Datei gefunden. Bitte laden Sie eine CSV-Datei hoch.")
    
    return render_template('index.html', classes=classes, blacklist=blacklist, students=students)

@app.route('/update_ini', methods=['POST'])
def update_ini():
    logging.debug("Update INI route accessed")
    ini_path = os.path.join(os.getcwd(), 'config.ini')
    new_classes = request.form.get('classes').split(',')
    new_blacklist = request.form.get('blacklist').split(',')
    write_ini_file(ini_path, new_classes, new_blacklist)
    cache.clear()
    return redirect(url_for('index'))

@app.route('/add_to_blacklist', methods=['POST'])
def add_to_blacklist():
    logging.debug("Add to blacklist route accessed")
    ini_path = os.path.join(os.getcwd(), 'config.ini')
    student_id = request.form.get('student_id')
    classes, blacklist = read_ini_file(ini_path)
    if student_id not in blacklist:
        blacklist.append(student_id)
    write_ini_file(ini_path, classes, blacklist)
    cache.clear()
    return jsonify({'status': 'success', 'action': 'added', 'student_id': student_id, 'blacklist': blacklist})

@app.route('/remove_from_blacklist', methods=['POST'])
def remove_from_blacklist():
    logging.debug("Remove from blacklist route accessed")
    ini_path = os.path.join(os.getcwd(), 'config.ini')
    student_id = request.form.get('student_id')
    classes, blacklist = read_ini_file(ini_path)
    if student_id in blacklist:
        blacklist.remove(student_id)
    write_ini_file(ini_path, classes, blacklist)
    cache.clear()
    return jsonify({'status': 'success', 'action': 'removed', 'student_id': student_id, 'blacklist': blacklist})

@app.route('/filter_csv')
def filter_csv():
    logging.debug("Filter CSV route accessed")
    ini_path = os.path.join(os.getcwd(), 'config.ini')
    classes, blacklist = read_ini_file(ini_path)
    csv_path = get_latest_csv(os.getcwd()) or session.get('uploaded_csv')
    if not csv_path:
        flash("Keine CSV Datei gefunden. Bitte laden Sie eine CSV-Datei hoch.")
        return redirect(url_for('index'))

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(os.getcwd(), 'AusbilderImportDatei')
    output_path = os.path.join(output_dir, f'WebUntis_Ausbilder_Import_{timestamp}.csv')
    filter_csv_by_classes_and_blacklist(csv_path, classes, blacklist, output_path)
    
    if request.args.get('open_explorer') == 'true':
        subprocess.Popen(f'explorer "{output_dir}"')
    
    flash("Die CSV Datei wurde gefiltert und im Unterverzeichnis AusbilderImportDatei mit Datums- und Uhrzeitangaben gespeichert!")
    return redirect(url_for('index'))

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            flash('Datei erfolgreich hochgeladen')
            # Store the uploaded file path in session
            session['uploaded_csv'] = file_path
            return redirect(url_for('index'))
    return render_template('upload.html')
