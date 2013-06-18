nagios-status-flask
===================

Aiming to provide something similar to the nagvis overview window but written in python with flask as a framework.

main.py = flask main function.
live.py = collection of data from livestatus (with some deprecated stuff that were ment to create the whole page without framework).
live.conf = configuration file for how to arange the grid pattern.

Developed on python 2.7.5 and flask 0.10 in a virtualenv.

Todo:
Document dependencies.
Rewrite live.py to work better with nagios-status-flask
