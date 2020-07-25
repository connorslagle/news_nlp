import os

class nytArticleSearcher():
    '''
    Interface with NYT Article Search API.

    Functionality:
     - Store API credentials
     - Take API kwargs, perform request, and return articles
    '''

    def __init__(self):
        self._api_key = os.environ.get('NYT_API_KEY')
        self._api_secret_key = os.environ.get('NYT_API_SECRET_KEY')

    @property
    def api_key(self):
        return self._api_key
    
    @property
    def api_secret_key(self):
        return self._api_secret_key

if __name__ == "__main__":
    nytSearcher = nytArticleSearcher()
