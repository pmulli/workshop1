from flask import Flask, render_template, request
 
app = Flask(__name__)
  
@app.route('/films/list') 
def films():
    return render_template('films.html')

@app.route('/films/table') 
def filmsTable():
    stars = request.values.get("stars", "")

    with open('data/filmData.txt', 'r') as f:
        filmList = f.readlines()
        return render_template('filmsTable.html', filmList = filmList, stars=stars)