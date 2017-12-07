# -*-coding:utf-8-*-
import requests
import json


class HttpClient:
    '''发送http请求'''

    def __init__(self, timeout=60):
        self.requests = requests
        self.timeout = timeout
        self.s = requests.session()
        self.s.keep_alive = False

    def get(self, url, header_dict=None, param_dict=None):
        response = requests.get(url, headers=header_dict, params=param_dict, timeout=self.timeout)
        return response

    def post_form(self, url, body_dict=None, header_dict=None, param_dict=None):
        response = requests.post(url, data=body_dict, headers=header_dict, params=param_dict, timeout=self.timeout)
        return response

    def post_json(self, url, body_dict=None, header_dict=None, param_dict=None):
        header_dict['content-type']='application/json'
        response = requests.post(url, data=json.dumps(body_dict), headers=header_dict, params=param_dict, timeout=self.timeout)
        return response

    def post_multipart(self, url, files=None, header_dict=None):
        response = requests.post(url, files=files, headers=header_dict)
        return response

    def post_multipart_file(self, url, file_path, header_dict=None):
        files = {'file': (open(file_path, 'rb'))}
        response = requests.post(url, files=files, headers=header_dict)
        return response

if __name__ == '__main__':
    response = HttpClient().post_form('http://192.168.180.58:8080/api/tms/wallet/cashOut',{'test':'123'})

    print(response.text)