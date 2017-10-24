#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class LineDistanceGet(object):
    '''
    根据出发城市和到达城市计算两地的距离
    /api/tms/line/getDistance
    '''
    __slots__ = ('__lineDistanceGetApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__lineDistanceGetApiUrl = "https://{0}:{1}{2}/api/tms/line/getDistance".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def line_get(self,sendCity='',arriveCity='',origin='',destination=''):
         '''根据出发城市和到达城市计算两地的距离'''
         try:
             payload ={
                 'sendCity': sendCity,
                 'arriveCity': arriveCity,
                 'origin': origin,
                 'destination': destination,
             }
             response = HttpClient().get(self.__lineDistanceGetApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None