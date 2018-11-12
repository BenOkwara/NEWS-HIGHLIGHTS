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
    news_description = get_news('description')
    publish = get_news('publishedAt')
    news_content = get_news('relevant')
    title = 'Your news Highlights'
    message = 'News Break'

    return render_template('index.html',title=title,description=news_description,publishedAt=publish,relevant=news_content)