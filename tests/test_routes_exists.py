from pytest import fail
from werkzeug.exceptions import NotFound


def test_route_list_files(route_matcher):
    try:
        assert route_matcher("/files")
    except NotFound:
        fail('Verifique se a rota "/files" existe')


def test_route_list_files_by_extension(route_matcher):
    try:
        assert route_matcher("/files/gif")
    except NotFound:
        fail('Verifique se a rota "/files/<extension>" existe')


def test_route_download_file(route_matcher):
    try:
        assert route_matcher("/download/kenzie.gif")
    except NotFound:
        fail('Verifique se a rota "/download/<filename>" existe')


def test_route_download_dir_as_zip(route_matcher):
    try:
        assert route_matcher("/download-zip")
    except NotFound:
        fail('Verifique se a rota "/download-zip" existe')


def test_route_upload(route_matcher):
    try:
        assert route_matcher("/upload", method='POST')
    except NotFound:
        fail('Verifique se a rota "/upload" existe')
