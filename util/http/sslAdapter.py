import ssl
import urllib3

from requests.adapters import HTTPAdapter


class Ssl3Adapter(HTTPAdapter):
    def __init__(self, num_pools=50,maxsize=500):
        self.poolmanager = urllib3.PoolManager(num_pools=num_pools, maxsize=maxsize, ssl_version=ssl.PROTOCOL_SSLv3)
