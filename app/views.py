from flask import render_template
from app import app
from . request import get_news

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

    # Latest News Highlights
    general_news = get_news('general')
    print(general_news)
    sports_news = get_news('sports')
    print('sports_news')
    technology_news = get_news('technology')
    print(technology_news)
    title = 'Your news Highlights'
    message = 'News Break'

    return render_template('index.html', message = message, title = title, general = general_news,sports = sports_news, technology = technology_news)