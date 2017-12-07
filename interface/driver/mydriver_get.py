#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class MyDriverGet(object):
    '''
    通过主键找司机
    /api/tms/driver/getDriver
    '''
    __slots__ = ('__myDriverGetApiUrl','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__myDriverGetApiUrl = "https://{0}:{1}{2}/api/tms/driver/getDriver".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def my_driver_get(self,driverId):
         '''通过主键找司机'''
         try:
             payload ={
             'driverId': driverId,
             }
             response = HttpClient().get(self.__myDriverGetApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('通过主键找司机发生异常:{0}'.format(e))
             return None