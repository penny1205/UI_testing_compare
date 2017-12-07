#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class DriverSelect(object):
    '''
    用于录单时查询获所有外请车包括已关联和未关联
    /api/tms/driver/listAppDriver
    '''
    __slots__ = ('__driverSelectApiUrl','partnerNo', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__driverSelectApiUrl = "https://{0}:{1}{2}/api/tms/driver/listAppDriver".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def driver_select(self):
         '''用于录单时查询外请车'''
         try:
             response = HttpClient().get(self.__driverSelectApiUrl,self.__head_dict)
             return response
         except Exception as e:
             Log().error('用于录单时查询获所有外请车发生异常:{0}'.format(e))
             return None