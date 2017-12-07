#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class DriverGet(object):
    '''
    根据外请车车主loginId查司机信息
    /api/tms/driver/getTmsAppDriverDetail
    '''
    __slots__ = ('__driverGetApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__driverGetApiUrl = "https://{0}:{1}{2}/api/tms/driver/getTmsAppDriverDetail".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def driver_get(self,loginId=''):
         '''根据外请车车主loginId查司机信息'''
         try:
             payload = {
                 'loginId': loginId
                        }
             response = HttpClient().get(self.__driverGetApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('根据外请车车主loginId查司机信息发生异常:{0}'.format(e))
             return None