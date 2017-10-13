#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class MyDCarGet(object):
    '''
    通过车辆主键查车信息
    /api/tms/car/getCar
    '''
    __slots__ = ('__myCarGetApiUrl','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__myCarGetApiUrl = "https://{0}:{1}{2}/api/tms/car/getCar".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def my_car_get(self,carId):
         '''通过车辆主键查车信息'''
         try:
             payload ={
             'carId': carId,
             }
             response = HttpClient().get(self.__myCarGetApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None