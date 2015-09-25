# coding: utf-8

from pyaop.aspect_loader import AspectLoader
from app import app

if __name__ == "__main__":
    AspectLoader.load_aspects_module(aspects_module='aspects')
    app.init()
