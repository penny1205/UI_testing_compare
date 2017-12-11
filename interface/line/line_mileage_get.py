#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class LineMileageGet(object):
    '''
    根据出发城市和到达城市计算两地的距离
    /api/tms/line/getDistance
    '''
    __slots__ = ('__lineMileageGetApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__lineMileageGetApiUrl = "https://{0}:{1}{2}/api/tms/line/getDistance".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def line_mileage_get(self,sendCity='',arriveCity='',origin='',destination=''):
         '''根据出发城市和到达城市计算两地的距离'''
         try:
             payload ={
                 'sendCity': sendCity,
                 'arriveCity': arriveCity,
                 'origin': origin,
                 'destination': destination,
             }
             response = HttpClient().get(self.__lineMileageGetApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('根据出发城市和到达城市计算两地的距离发生异常:{0}'.format(e))
             return None