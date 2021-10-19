from flask import Flask
from environs import Env
from os import environ
import os

from kenzie.image import download_dir_zip, download_file, list_all_files, list_all_files_by_extension, upload_image


app = Flask(__name__)

env = Env()
env.read_env()

files_directory = environ.get('FILES_DIRECTORY')
allowed_extensions = environ.get('ALLOWED_EXTENSIONS')

try:
    os.makedirs(files_directory)
    for file_extensions in allowed_extensions.split(','):
        os.makedirs(f'{files_directory}/{file_extensions}')
except FileExistsError:
    ...


@app.get('/download/<string:filename>')
def download(filename: str):
    return download_file(filename)


@app.get('/download-zip')
def download_dir_as_zip():
    return download_dir_zip()


@app.get('/files')
def list_files():
    return list_all_files()


@app.get('/files/<string:extension>')
def list_files_by_extension(extension: str):
    return list_all_files_by_extension(extension)


@app.post('/upload')
def upload():
    return upload_image()
