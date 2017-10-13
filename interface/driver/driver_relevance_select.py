#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class DriverRelevanceSelect(object):
    '''
    我的外请车列表,查询结果是已关联的外请车
    /api/tms/driver/listTmsAppDriver
    '''
    __slots__ = ('__driverRelevanceSelectApiUrl','partnerNo', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__driverRelevanceSelectApiUrl = "https://{0}:{1}{2}/api/tms/driver/listTmsAppDriver".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def driver_relevance_select(self,currentPage='1',rows='10',mobile ='',name='',carNo='',recentLineStart='',recentLineEnd=''):
         '''查询已关联的外请车'''
         try:
             payload ={
                 'currentPage': currentPage,
                 'rows': rows,
                 'partnerNo': self.partnerNo,
                 'name': name,
                 'mobile': mobile,
                 'carNo': carNo,
                 'recentLineStart':recentLineStart,
                 'recentLineEnd':recentLineEnd
             }
             response = HttpClient().get(self.__driverRelevanceSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None