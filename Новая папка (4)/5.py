from flask import Flask, render_template
import os
def index():
    return render_template('index2.html')
folder = os.getcwd()
app = Flask(name, template_folder=folder, static_folder=folder)
app.add_url_rule('/', 'index', index)
if name == "main":
    app.run()