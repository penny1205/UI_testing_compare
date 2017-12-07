#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class MyDriverCreate(object):
    '''
    新增自有司机
    /api/tms/driver/createDriver
    '''
    __slots__ = ('__myDriverCreateApiUrl','partnerNo','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__myDriverCreateApiUrl = "https://{0}:{1}{2}/api/tms/driver/createDriver".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def my_driver_create(self,mobile='',name='',idNo='',photoDriverCard ='',frontIdCard='',backIdCard=''):
         '''新增自有司机'''
         try:
             payload ={
                 'mobile': mobile,
                 'name': name,
                 'idNo': idNo,
                 'photoDriverCard': photoDriverCard,
                 'frontIdCard': frontIdCard,
                 'backIdCard': backIdCard,
                 'partnerNo':self.partnerNo,
             }
             response = HttpClient().post_json(self.__myDriverCreateApiUrl,payload,self.__head_dict)
             return response
         except Exception as e:
             Log().error('新增自有司机发生异常:{0}'.format(e))
             return None