from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/bio', methods=['GET'])
def bio():
    return render_template('bio.html', title  = 'Bio')

@app.route('/skillset', methods=['GET'])
def skillset():
    return render_template('skillset.html', title = 'Skillset')

if __name__ == '__main__':
    app.run()
