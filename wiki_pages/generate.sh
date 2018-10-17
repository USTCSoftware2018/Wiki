#!/bin/bash

PYTHONPATH=. markdown_py -x gen_adjust "$1" | cat _header.html - _footer.html
