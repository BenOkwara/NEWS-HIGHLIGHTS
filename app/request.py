import urllib.request,json
from .models import New


# Getting api key
api_key = None

# Getting the new base url
base_url = None
# sources_url = app.config["NEWS_SOURCES_API"]

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEW_API_KEY']
    base_url = app.config['NEW_API_BASE_URL']
    print(base_url.format("sortBy",api_key))


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

def get_new():
    source_url='https://newsapi.org/v2/sources?&apiKey=8765aa287bb84962a62f1c1cfddef398'
    # get_news_details_url = base_url.format(id,api_key)
    new_object = None
    with urllib.request.urlopen(source_url) as url:
        new_details_data = url.read()
        new_details_response = json.loads(new_details_data)

        if new_details_response['sources']:
            new_articles_list = new_details_response['sources']
            new_object = process_sources(new_articles_list)
    print(new_object)
    return new_object

def process_sources(new_source):
    '''
    Function that processes the new result and then transform them to a list of Objects

    Args:
        new_list: A list of dictionaries that contain new details

    Returns:
        new_articles: Displays a list of new objects
    '''
    new_object = []
    for source in new_source:
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')

        new_source = Source(name,description,category,url)
        new_object.append(new_source)

    return new_object
