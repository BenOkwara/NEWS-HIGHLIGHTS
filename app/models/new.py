class New:
    '''
    New class to define New Objects
    '''

    def __init__(self,id,title,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
class Source:
    def __init__(self,name,description,category,url):
        self.name = name
        self.description=description
        self.category= category
        self.url =url