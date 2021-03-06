from requests import request

DOMAIN = 'https://trefle.io'
ENTRY_POINT = '/api/v1/plants?'

class PlantAPI:
    def __init__(self, token):
        self.token = token

    def search(self, **kwargs):
        '''
        Search. Accepts arbitrary inputs and passes with no sanitation.
        '''
        if len(kwargs) == 0:
            return {}
        else:
            request_uri = DOMAIN + ENTRY_POINT + f'token={self.token}&q='
            for key, value in kwargs.items():
                request_uri += f'filter[{key}]={value}&'
            return request('GET', request_uri).json()

    def get_first_plant(self, **kwargs):
        '''
        The thing.
        '''
        return self.get_plant(0, **kwargs)

    def get_plant(self, i: int, search = {}, **kwargs):
        '''
        The thing.
        '''
        if len(search) == 0:
            search = self.search(**kwargs)
        entry = search['data'][i]['links']['self']
        return request('GET', DOMAIN + entry + f'?token={self.token}').json()