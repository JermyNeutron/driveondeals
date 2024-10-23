from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

@app.route('/download/<path:filename>')
def download_file(filename):
    directory = '/home/jbcrisostomo/exports/'  # Adjust to your directory
    file_path = os.path.join(directory, filename)

    # Debugging: log the requested filename and check if the file exists
    app.logger.debug(f'Requested file: {file_path}')
    if not os.path.isfile(file_path):
        app.logger.error(f'File not found: {file_path}')  # Log if file is not found
        abort(404)  # Return a 404 error if the file does not exist

    try:
        return send_from_directory(directory, filename, as_attachment=True)
    except Exception as e:
        app.logger.error(f'Error sending file: {e}')  # Log any other errors
        abort(500)

if __name__ == '__main__':
    app.run()
