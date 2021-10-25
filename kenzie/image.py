from flask import jsonify, request, make_response, send_from_directory
from http import HTTPStatus
import os
from environs import Env
from os import environ

from werkzeug.utils import secure_filename

env = Env()
env.read_env()

allowed_extensions = environ.get('ALLOWED_EXTENSIONS')

def is_file_in_directory():
    files_list = []
    files_directory = os.walk('./images')
    for _, _, filenames in files_directory:
        for files in filenames:
            if files not in files_list:
                files_list.append(files)

    return files_list

def list_all_files():
    files_directory = os.walk('./images')
    files_list = []
    for _, _, filenames in files_directory:
        if len(filenames) != 0:
            for files in filenames:
                files_list.append(files)

    return make_response(jsonify(files_list), HTTPStatus.OK)


def list_all_files_by_extension(extension):
    files_directory = os.walk('./images')
    files_list = []
    if extension not in allowed_extensions:
        return make_response({'msg': f"There are no files with the extension '{extension}'."}, HTTPStatus.NOT_FOUND)
    else:
        for _, _, filenames in files_directory:
            for image in filenames:
                image_extension = image.split('.')[-1]
                if image_extension in allowed_extensions and image_extension == extension:
                    files_list.append(image)

        return make_response(jsonify(files_list), HTTPStatus.OK)


def upload_image():
    image_to_be_uploaded = request.files['file']
    image_extension = image_to_be_uploaded.content_type.split('/')[1]

    if image_extension in allowed_extensions:
        if image_to_be_uploaded.filename in is_file_in_directory():
            return make_response({'msg': f"A file with name '{image_to_be_uploaded.filename}' already exists."}, HTTPStatus.CONFLICT)
        else:
            filename = secure_filename(image_to_be_uploaded.filename)
            image_to_be_uploaded.save(os.path.join(f'./images/{image_extension}', filename))

            return make_response({'msg': f"The file '{filename}' was uploaded successfully."}, HTTPStatus.CREATED)

    else:
        return make_response({'msg': f"The extension '{image_extension}' is not supported."}, HTTPStatus.UNSUPPORTED_MEDIA_TYPE)


def download_file(filename):
    image_extension = filename.split('.')[-1]

    if filename not in is_file_in_directory():
        return make_response({'msg': 'File does not exist.'}, HTTPStatus.NOT_FOUND)

    return make_response(send_from_directory(directory=f'../images/{image_extension}', path=filename, as_attachment=True), HTTPStatus.OK)


def download_dir_zip(file_extension, compression_ratio):
    files_directory = os.walk('./images')

    for dirpath, _, filenames in files_directory:
        if file_extension == dirpath.split('./images/')[-1]:
            if len(filenames) == 0:
                return make_response({'msg': 'Empty directory. No files to download.'}, HTTPStatus.NOT_FOUND)

            os.system(f'zip -r -{compression_ratio} /tmp/{file_extension}-images {dirpath}')
            return make_response(send_from_directory(directory='/tmp', path=f'{file_extension}-images.zip', as_attachment=True), HTTPStatus.OK)
