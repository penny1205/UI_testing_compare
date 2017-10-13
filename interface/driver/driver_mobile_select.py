#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class DriverMobileSelect(object):
    '''
    录单时手机号查询外请车列表,包括已关联和未关联
    /api/tms/driver/listAppCars
    '''
    __slots__ = ('__driverMobileSelectApiUrl','partnerNo', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__driverMobileSelectApiUrl = "https://{0}:{1}{2}/api/tms/driver/listAppCars".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def driver_mobile_select(self,isCertificate='1',mobile =''):
         '''录单时手机号查询'''
         try:
             payload ={
             'isCertificate': isCertificate,
             'mobile': mobile,

             }
             response = HttpClient().get(self.__driverMobileSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None