import unittest
from models import new
New = new.New

class NewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the New class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_new = New (1234,'News Highlights','Breaking News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_new,New))

if __name__ =='__main__':
    unittest.main()