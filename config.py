import os
class Config:
    '''
    configuration of the parent class
    '''
    NEW_API_BASE_URL = 'https://newsapi.org/v2/everything?q=apple&sortBy={}&apiKey={}'
    NEW_API_KEY = os.environ.get('NEW_API_KEY')

class ProdConfig(Config):
    '''
    This is configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    This is a Devolopment child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
