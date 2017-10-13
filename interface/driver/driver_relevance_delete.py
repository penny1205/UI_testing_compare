#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class DriverRelevanceDelete(object):
    '''
    删除外请车司机关联关系
   /api/tms/driver/deleteTmsAppDriver
    '''
    __slots__ = ('__driverRelevanceDeleteApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__driverRelevanceDeleteApiUrl = "https://{0}:{1}{2}/api/tms/driver/deleteTmsAppDriver".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def driver_relevance_delete(self,id):
         '''删除外请车司机关联关系'''
         try:
             payload ={'id':id}
             response = HttpClient().post_form(self.__driverRelevanceDeleteApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None