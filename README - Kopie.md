Ausbilder- und Azubi-Filter
This is a Flask-based web application designed to filter CSV files based on specified classes and blacklist criteria. The application allows users to upload a CSV file, filter the data, and download the filtered output. The application also provides functionalities to manage the classes and blacklist through a web interface.

Features
Upload CSV files for processing.
Filter records based on specified classes.
Exclude records based on a blacklist of student IDs.
Save filtered records to a CSV file with a timestamp in the filename.
Manage classes and blacklist through a web interface.
Automatically open the web interface on application start.
Automatically create a default configuration file if none exists.
Prerequisites
Python 3.x
Flask
Pandas
Chardet
ConfigParser
PyInstaller (for creating the executable)
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/ausbilder-azubi-filter.git
cd ausbilder-azubi-filter
Create a virtual environment and activate it:

sh
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install the dependencies:

sh
Copy code
pip install -r requirements.txt
Usage
Running the application
Ensure the directory structure:

arduino
Copy code
flask_project/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   └── index.html
│   │   └── upload.html
│   └── static/
├── config.ini
├── app.spec
├── run.py
└── IhreImportDatei.csv
Run the application:

sh
Copy code
python run.py
Access the web interface:
The web interface will automatically open in your default web browser at http://127.0.0.1:5000/.

Compiling to an executable
Install PyInstaller:

sh
Copy code
pip install pyinstaller
Compile the application:

sh
Copy code
pyinstaller --onefile run.py
Run the executable:
Ensure that config.ini and IhreImportDatei.csv are in the same directory as run.exe, then run run.exe.

Application structure
app/__init__.py: Initializes the Flask app, ensures necessary directories and files exist, and sets up logging.
app/routes.py: Contains the routes for handling web requests, managing the INI file, filtering the CSV, and handling file uploads.
app/templates/index.html: The main interface for managing classes, blacklist, and displaying students.
app/templates/upload.html: The interface for uploading CSV files.
run.py: The entry point for the application that starts the Flask server and opens the web interface in the default browser.
Configuration
config.ini
The config.ini file contains the classes and blacklist for filtering the CSV data.

Example structure:

ini
Copy code
[FILTER]
Classes=Class1,Class2,Class3

[BLACKLIST]
IDs=12345,67890
Upload Folder
The application uses an uploads folder to store uploaded CSV files temporarily. This folder is created automatically if it does not exist.

Logging
The application logs its activities to app.log in the app directory. Logging includes debugging information, errors, and other significant events.

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries or issues, please contact [your.email@example.com].

