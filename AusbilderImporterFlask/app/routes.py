import pandas as pd
import configparser
import glob
import os
import chardet
import logging
from flask import render_template, request, redirect, url_for, jsonify
from app import app, cache

logging.debug("routes.py loaded")

def read_ini_file(ini_path):
    logging.debug(f"Reading INI file from {ini_path}")
    config = configparser.ConfigParser()
    config.read(ini_path)
    classes = config['FILTER']['Classes'].split(',')
    blacklist = [str(id).strip() for id in config['BLACKLIST']['IDs'].split(',')] if 'IDs' in config['BLACKLIST'] and config['BLACKLIST']['IDs'] else []
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
    if blacklist:
        filtered_df = df[df['Klasse'].isin(classes) & ~df['Interne ID-Nummer'].astype(str).isin(blacklist)]
    else:
        filtered_df = df[df['Klasse'].isin(classes)]
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    filtered_df.to_csv(output_path, index=False, sep=';', encoding='utf-8-sig')
    logging.debug(f"Filtered CSV saved to {output_path}")

@cache.cached(timeout=300)
@app.route('/')
def index():
    logging.debug("Index route accessed")
    ini_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.ini')
    classes, blacklist = read_ini_file(ini_path)
    csv_path = get_latest_csv(os.getcwd())  # Look for CSV files in the current directory
    students = []
    if (csv_path):
        encoding = detect_encoding(csv_path)
        df = pd.read_csv(csv_path, delimiter=';', encoding=encoding)
        df = df.sort_values(by=['Klasse', 'Nachname'])
        df['Interne ID-Nummer'] = df['Interne ID-Nummer'].astype(str)
        students = df[['Interne ID-Nummer', 'Vorname', 'Nachname', 'Klasse']].to_dict(orient='records')
    return render_template('index.html', classes=classes, blacklist=blacklist, students=students)

@app.route('/update_ini', methods=['POST'])
def update_ini():
    logging.debug("Update INI route accessed")
    ini_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.ini')
    new_classes = request.form.get('classes').split(',')
    new_blacklist = request.form.get('blacklist').split(',')
    write_ini_file(ini_path, new_classes, new_blacklist)
    cache.clear()
    return redirect(url_for('index'))

@app.route('/add_to_blacklist', methods=['POST'])
def add_to_blacklist():
    logging.debug("Add to blacklist route accessed")
    ini_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.ini')
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
    ini_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.ini')
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
    base_dir = os.getcwd()  # Look for CSV files in the current directory
    csv_path = get_latest_csv(base_dir)
    if not csv_path:
        return 'No CSV files found in the directory.'
    
    ini_path = os.path.join(base_dir, 'config.ini')
    classes, blacklist = read_ini_file(ini_path)
    output_path = os.path.join(base_dir, 'AusbilderImportDatei', 'filtered_output.csv')
    filter_csv_by_classes_and_blacklist(csv_path, classes, blacklist, output_path)
    return 'CSV file filtered and saved!'
