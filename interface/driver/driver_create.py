#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class DriverCreate(object):
    '''
    新增外请车
    /api/tms/driver/createTmsAppDriver/all
    '''
    __slots__ = ('__createDriverApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__createDriverApiUrl = 'https://{0}:{1}{2}/api/tms/driver/createTmsAppDriver/all'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token']
        }

    def driver_create(self):
        '''新增外请车'''
        try:
            payload = {
            'name' : 'penny',
            'mobile' : '13077327047',
            'idNo' : '110605199001011551',
            'carNo' : '京A00000',
            'carLength' : '17.5',
            'carModel' : 'XIANG_SHI_CHE',
            'carLoad' : '20'
            }
            response = HttpClient().post_form(self.__createDriverApiUrl,payload,self.__head_dict)
            return response
        except Exception:
            return None