#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class DriverRelevanceCreate(object):
    '''
    关联外请车
    /api/tms/driver/createRelevance
    '''
    __slots__ = ('__driverRelevanceCreateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__driverRelevanceCreateApiUrl = "https://{0}:{1}{2}/api/tms/driver/createRelevance".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def driver_relevance_create(self,loginId = ''):
         '''关联外请车'''
         try:
             payload ={'loginId': loginId }
             response = HttpClient().post_form(self.__driverRelevanceCreateApiUrl, payload, self.__head_dict)
             return response
         except Exception as e:
             Log().error('录单时手机号查询发生异常:{0}'.format(e))
             return None