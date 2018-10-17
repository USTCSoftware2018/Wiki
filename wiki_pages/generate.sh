#!/bin/bash

PYTHONPATH=. python -m markdown -x gen_adjust "$1" | cat _header.html - _footer.html
