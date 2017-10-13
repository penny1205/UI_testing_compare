#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class MyDriverDelete(object):
    '''
    删除自有司机信息
   /api/tms/driver/deleteDriver
    '''
    __slots__ = ('__myDriverDeleteApiUrl','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__myDriverDeleteApiUrl = "https://{0}:{1}{2}/api/tms/driver/deleteDriver".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def my_driver_delete(self,driverId):
         '''删除自有车信息'''
         try:
             payload ={
                 'driverId': driverId,
             }
             response = HttpClient().post_form(self.__myDriverDeleteApiUrl,payload,self.__head_dict,)
             return response
         except Exception:
             return None