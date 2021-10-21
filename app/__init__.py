from flask import Flask, request, make_response
from environs import Env
from os import environ
import os
from http import HTTPStatus

from kenzie.image import download_dir_zip, download_file, list_all_files, list_all_files_by_extension, upload_image


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

env = Env()
env.read_env()

files_directory = environ.get('FILES_DIRECTORY')
allowed_extensions = environ.get('ALLOWED_EXTENSIONS')

os.makedirs(files_directory, exist_ok=True)
for file_extensions in allowed_extensions.split(','):
    os.makedirs(f'{files_directory}/{file_extensions}', exist_ok=True)


@app.get('/download/<string:filename>')
def download(filename: str):
    return download_file(filename)


@app.get('/download-zip')
def download_dir_as_zip(*args):
    if request.args:
        file_extension = request.args.get('file_extension')
        compression_ratio = request.args.get('compression_ratio')

        return download_dir_zip(file_extension, compression_ratio)

    return make_response('No query params defined.', HTTPStatus.NOT_FOUND)


@app.get('/files')
def list_files():
    return list_all_files()


@app.get('/files/<string:extension>')
def list_files_by_extension(extension: str):
    return list_all_files_by_extension(extension)


@app.post('/upload')
def upload():
    return upload_image()


@app.errorhandler(413)
def largefile_error(e):
    image_size = request.headers.get('Content-Length')
    return make_response({'msg': f"This file's size ({image_size}B) exceeds the maximum size allowed (1MB)."}, HTTPStatus.REQUEST_ENTITY_TOO_LARGE)
