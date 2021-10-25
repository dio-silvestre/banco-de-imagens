from flask.testing import FlaskClient
from http import HTTPStatus
from flask import request
from werkzeug.datastructures import FileStorage
from datetime import date, datetime

from kenzie.image import is_file_in_directory


def test_route_list_files_status(client: FlaskClient):
    response = client.get('/files')
    assert response.status_code == HTTPStatus.OK


def test_route_list_files_by_extension_status(client: FlaskClient):
    response = client.get('/files/gif')
    assert response.status_code == HTTPStatus.OK


def test_route_download_file_status(client: FlaskClient):
    response = client.get('/download/<filename>')
    filename = request.path.split('/')[-1]
    if filename in is_file_in_directory():
        assert response.status_code == HTTPStatus.OK
    else:
        assert response.status_code == HTTPStatus.NOT_FOUND


def test_route_download_dir_as_zip_status(client: FlaskClient):
    response = client.get('/download-zip')
    if request.args:
        assert response.status_code == HTTPStatus.OK


def test_route_upload_status(client: FlaskClient):
    FILE_PATH = './tests/imagens_teste/kenzie.gif'
    with open(FILE_PATH, 'rb') as file:
        filename = f'{str(datetime.utcnow()).split(".")[-1]}.gif'
        my_file = FileStorage(stream=file, filename=filename, content_type='image/gif')
    
        response = client.post('/upload', data={'file': my_file}, content_type='multipart/form-data')

    assert response.status_code == HTTPStatus.CREATED
