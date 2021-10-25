from flask import Flask
from pytest import fixture, fail


@fixture
def app():
    try:
        return __import__("app").app
    except ModuleNotFoundError:
        fail("Verifique se o arquivo principal esta nomeado como `app`")
    except AttributeError:
        fail("Verifique se a instancia de Flask esta nomeada como `app`")


@fixture
def client(app: Flask):
    with app.test_client() as client:
        yield client


@fixture
def route_matcher(app: Flask):
    return app.url_map.bind("").match
