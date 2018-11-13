from app import app
import urllib.request,json
from .models import new

New = new.New

# Getting api key
api_key = app.config['NEW_API_KEY']

# Getting the new base url
base_url = app.config["NEW_API_BASE_URL"]
# sources_url = app.config["NEWS_SOURCES_API"]


def get_news(sortBy):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(sortBy,api_key)
    # get_sources_url = sources_url.format(sortBy,api_key)
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_articles = None

        if get_news_response['articles']:
            new_articles_list = get_news_response['articles']
            new_articles = process_articles(new_articles_list)
    return new_articles

def process_articles(new_list):
    '''
    Function that processes the new result and then transform them to a list of Objects

    Args:
        new_list: A list of dictionaries that contain new details

    Returns:
        new_articles: Displays a list of new objects
    '''
    new_articles = []
    for new_item in new_list:
        id = new_item.get('id')
        title = new_item.get('title')
        description = new_item.get('description')
        url = new_item.get('url')
        urlToImage = new_item.get('urlToImage')
        publishedAt = new_item.get('publishedAt')
        content = new_item.get('content')

        
        new_object = New(id,title,description,url,urlToImage,publishedAt,content)
        new_articles.append(new_object)

    return new_articles

def get_new(id):
    get_news_details_url = base_url.format(id,api_key)
    
    with urllib.request.urlopen(get_news_details_url) as url:
        new_details_data = url.read()
        new_details_response = json.loads(new_details_data)

        new_object = None
        if new_details_response:
            id = new_details_response.get('id')
            title = new_details_response.get('original_title')
            description = new_details_response.get('description')
            url = new_details_response.get('url')
            urlToImage = new_details_response.get('urlToImage')
            publishedAt = new_details_response.get('publishedAt')
            content = new_details_response.get('content')

            new_object = New(id,title,description,url,urlToImage,publishedAt,content)

    return new_object