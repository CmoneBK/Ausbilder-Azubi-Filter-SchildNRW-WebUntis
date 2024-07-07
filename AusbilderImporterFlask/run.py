from app import app
import logging
import webbrowser
import threading

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

print("Starting the application...")

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    try:
        app.run(debug=True)
    except Exception as e:
        logging.exception("Exception in app:")
        print("Exception occurred. Check the logs for more details.")
    input("Press Enter to exit...")
