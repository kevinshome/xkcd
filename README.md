<p align="center">
<a href="https://xkcd.com/303"><img src="https://imgs.xkcd.com/comics/compiling.png" width=250 height=250 alt="xkcd 303"></a>
<a href="https://xkcd.com/"><img src="https://xkcd.com/s/0b7742.png" alt="xkcd logo"></a>
<a href="https://xkcd.com/1987"><img src="https://imgs.xkcd.com/comics/python_environment.png" width=250 height=250 alt="xkcd 1987"></a>
</p>

A simple script utilizing Pillow to display an xkcd comic. Can fetch either the
latest comic, a random comic, or a specific comic by number. In the terminal window, 
the script displays the comic number, title, release date, and alt-text. This script
is made possible thanks to the xkcd JSON API (https://xkcd.com/json.html).

To install this script, run the following command:
```
curl -fsSL https://raw.githubusercontent.com/kevinshome/xkcd/main/install.py | python3 -
```

To install with the full database of comics:
```
curl -fsSL https://raw.githubusercontent.com/kevinshome/xkcd/main/install.py | python3 - --install-db
```

Database
==========

In order to search by keyword, the comic database (xkcd-comicdb) is required. It can be installed either by running the installation script with the "--install-db" flag, or directly from PyPI.

Updating
==========

To check for available updates for the script, run:
```
$ xkcd --update
```

To check for available updates for the database, run:
```
$ xkcd --update-db
```

License
=========

All xkcd comics are released under a [Creative Commons Attribution-NonCommercial 2.5 License](https://xkcd.com/license.html).

This software is released into the public domain under the terms of the Unlicense, made
available in the 'LICENSE' file in the root of this project.
