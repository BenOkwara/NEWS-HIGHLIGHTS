from flask import render_template
from app import app

# views
@app.route('/new/<int:new_id>')
def movie(new_id):

    '''
    View new page function that returns the new details page and its data
    '''
    return render_template('new.html',id = new_id)
    
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Your news Highlights'
    message = 'News Break'
    # general = get_news('general')
    # entertainment = get_news('entertainment')
    # health = get_news('health')

    return render_template('index.html', message = message, title = title)