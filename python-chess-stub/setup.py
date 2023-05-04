#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import setuptools

setuptools.setup(
    name="python-zhchess",
    version="1.999",
    author="Niklas Fiekas",
    author_email="niklas.fiekas@backscattering.de",
    description="A zhchess library with move generation, move validation, and support for common formats.",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
    long_description_content_type="text/x-rst",
    license="GPL-3.0+",
    keywords="zhchess fen epd pgn polyglot syzygy gaviota uci xboard",
    url="https://github.com/niklasf/python-zhchess",
    packages=[],
    install_requires=["zhchess>=1,<2"],
    classifiers=[
        "Development Status :: 7 - Inactive",
    ],
    project_urls={
        "Documentation": "https://python-zhchess.readthedocs.io",
    },
)
