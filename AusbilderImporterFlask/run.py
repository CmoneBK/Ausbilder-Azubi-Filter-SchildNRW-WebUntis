from app import app
import logging

print("Starting the application...")

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        logging.exception("Exception in app:")
        print("Exception occurred. Check the logs for more details.")
    input("Press Enter to exit...")
