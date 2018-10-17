#!/bin/bash

OIFS="$IFS"
IFS=$'\n'
for md_file in $(find . -mindepth 2 -name "*.md")
do
    html_file=${md_file/%.md/.html}
    ./generate.sh $md_file > $html_file && echo "[SUCCESS] $md_file -> $html_file" || echo "[FAIL] $md_file -> $html_file"
done
IFS="$OIFS"
