from app.package import search_directory
from flask import Flask, session, redirect, url_for, request, render_template, flash



app = Flask(__name__, template_folder='template')

# Set a secret key fo some rando bytes. Keep this really secret!
app.secret_key = b'm\x9c\xbf`\x8c\x946\x0c\xf2\xde\xec\xc8\xa6\xdfO\xe8'


#index route
@app.route('/')
def index():
    #return 'Logged in as %s' % escape(session['username'])
    return render_template('index.html', name='musicas')
# error route
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
# Roda a aplicacao em: http://localhost:8085
app.run(debug=True,port=8085)
