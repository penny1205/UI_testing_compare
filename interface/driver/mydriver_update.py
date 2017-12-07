#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class MyDriverUpdate(object):
    '''
    修改司机信息
    /api/tms/driver/updateDriver
    '''
    __slots__ = ('__myDriverUpdateApiUrl','partnerNo','__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__myDriverUpdateApiUrl = "https://{0}:{1}{2}/api/tms/driver/updateDriver".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def my_driver_update(self,driverId='',mobile='',name='',idNo='',photoDriverCard ='',frontIdCard='',backIdCard=''):
         '''新增自有司机'''
         try:
             payload ={
                 'driverId':driverId,
                 'mobile': mobile,
                 'name': name,
                 'idNo': idNo,
                 'photoDriverCard': photoDriverCard,
                 'frontIdCard': frontIdCard,
                 'backIdCard': backIdCard,
                 'partnerNo':self.partnerNo,
             }
             response = HttpClient().post_json(self.__myDriverUpdateApiUrl,payload,self.__head_dict)
             return response
         except Exception as e:
             Log().error('新增自有司机发生异常:{0}'.format(e))
             return None