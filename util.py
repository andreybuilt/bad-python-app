import os

from flask import url_for

def get_root_dir():
    return os.getcwd()


def get_uploads_folder_url():
    return url_for('static', filename='uploads')
    
# Lists a directory for the file browser page
def list_dir():
    from flask import request
    import subprocess
    path = request.args.get("path", ".")
    return subprocess.check_output("ls " + path, shell=True)
