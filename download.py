from sentinelsat import SentinelAPI

api = SentinelAPI('ganz_gi', '9367410909', 'https://scihub.copernicus.eu/dhus')
api.download('c43f19c3-9838-4851-935b-ebaf2803f2ad');
