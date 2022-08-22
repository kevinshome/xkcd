xkcd
========

A simple script utilizing Pillow to display an xkcd comic. Can fetch either the
latest comic, a random comic, or a specific comic by number. In the terminal window, 
the script displays the comic number, title, release date, and alt-text. This script
is made possible thanks to the xkcd JSON API (https://xkcd.com/json.html).

To install this script, run the following command:
```
curl -fsSL https://raw.githubusercontent.com/nhtnr/xkcd/main/install.py | python3 -
```

To install with the full database of comics:
```
curl -fsSL https://raw.githubusercontent.com/nhtnr/xkcd/main/install.py | python3 - --install-db
```

Database
==========

This repository contains a SQLite3 database with all available comic information (as of 2022-08-21).
In order to search by keyword, this database is required. It can be installed either by running the installation script with the "--install-db" flag, or directly from PyPI (xkcd-comicdb).

License
=========

This software is released into the public domain under the terms of the Unlicense, made
available in the 'LICENSE' file in the root of this project.
