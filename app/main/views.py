from flask import render_template,request,redirect,url_for
from . import main
# from main import main
from ..request import get_news,get_new
# from ..models import Review

# views
@main.route('/news')
def new():

    '''
    View new page function that returns the new details page and its data
    '''
    new = get_new()
    # title = f'{new.}'

    return render_template('new.html', new = new)

@main.route('/')
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
