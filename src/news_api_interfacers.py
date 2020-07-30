import os
import requests
from urllib.parse import urlencode

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
        self.base_url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?'

    @property
    def api_key(self):
        return self._api_key
    
    @property
    def api_secret_key(self):
        return self._api_secret_key

    def fetch_articles(self, query_terms, filter_terms, page_num):
        '''
        Method for querying API and returning articles for a specific
        page.

        Params:
         - query_terms, dict of dicts:
            Dict of 'AND' kwargs and 'OR' kwargs
         - filter_terms, dict of dicts:
            Dict of 'AND' kwargs and 'OR' kwargs
         - page_num, int:
            Desired results page number
        '''
        pass

    
    def _format_query(self, term_dict):
        '''
        Reformats dict of kwargs to html strings.

        Params:
         - term_dict, dict of dicts:
            Dict of 'AND' kwargs and 'OR' kwargs
        '''
        and_dict = term_dict.get('AND')
        or_dict = term_dict.get('OR')
        pass
        


if __name__ == "__main__":
    nytSearcher = nytArticleSearcher()
    
    q_and_terms = {'begin_date': '20160101', 'end_date': '20170101', 'facet': 'true'}
    fq_and_terms = {'news_desk': 'Politics'}

    q = nytSearcher.base_url + urlencode(fq_and_terms) + '&' + urlencode({'api-key': nytSearcher.api_key})

    print(q)