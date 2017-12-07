#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class MyDriverSelect(object):
    '''
    我的司机列表
    /api/tms/driver/listDrivers
    '''
    __slots__ = ('__myDriverSelectApiUrl','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__myDriverSelectApiUrl = "https://{0}:{1}{2}/api/tms/driver/listDrivers".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def my_driver_select(self,currentPage='1',rows='10',name='',mobile =''):
         '''我的司机列表'''
         try:
             payload ={
             'currentPage': currentPage,
             'rows': rows,
             'name': name,
             'mobile': mobile,
             }
             response = HttpClient().get(self.__myDriverSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('我的司机列表发生异常:{0}'.format(e))
             return None