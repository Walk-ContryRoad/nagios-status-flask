from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash
#DATAFILE = [dict(title="meep", text="peep")]
DATAFILE = file('example_file.txt').readline()
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def show_entries():
	entries = DATAFILE

	return render_template('show_entries.html', entries=entries)


if __name__ == '__main__':
	app.run()
