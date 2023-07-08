import requests

class ShrinkCoinService:
    def __init__(self, api_key):
        self.api_key = api_key

    def shrink_url(self, url, is_instant=True):
        api_url = 'https://shrinkco.in/api/shrink'
        parameters = {
            'API_KEY': self.api_key,
            'URL': url,
            'IS_INSTANT': str(is_instant)
        }

        return self._call_api(api_url, parameters)

    def delete_url(self, id):
        api_url = 'https://shrinkco.in/api/delete'
        parameters = {
            'API_KEY': self.api_key,
            'ID': id
        }

        return self._call_api(api_url, parameters)

    def check_url_clicks(self, id):
        api_url = 'https://shrinkco.in/api/clicks'
        parameters = {
            'API_KEY': self.api_key,
            'ID': id
        }

        return self._call_api(api_url, parameters)

    def check_url_campaign_clicks(self, id, campaign):
        api_url = 'https://shrinkco.in/api/campaign'
        parameters = {
            'API_KEY': self.api_key,
            'ID': id,
            'CAMPAIGN': campaign
        }

        return self._call_api(api_url, parameters)

    def _call_api(self, url, parameters):
        response = requests.get(url, params=parameters)
        return response.json()

