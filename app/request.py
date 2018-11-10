from app import app
import urllib.request,json
from .models import new

New = new.New

# Getting api key
api_key = app.config['NEW_API_KEY']

# Getting the new base url
base_url = app.config["NEW_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None

        if get_news_response['results']:
            new_results_list = get_news_response['results']
            new_results = process_results(new_results_list)

    return new_results

def process_results(new_list):
    '''
    Function that processes the new result and then transform them to a list of Objects

    Args:
        new_list: A list of dictionaries that contain new details

    Returns:
        new_results: Displays a list of new objects
    '''
    new_results = []
    for new_item in new_list:
        id = new_item.get('id')
        name = new_item.get('name')
        description = new_item.get('news_description')
        category = new_item.get('news_category')
        language = new_item.get('language')
        country = new_item.get('country')