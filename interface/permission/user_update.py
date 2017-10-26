#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class UserUpdate(object):
    '''
    修改账号
    /api/tms/system/updateTmsUser
    '''
    __slots__ = ('__userUpdateApiUrl','partnerNo', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__userUpdateApiUrl = 'https://{0}:{1}{2}api/tms/system/updateTmsUser'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def user_update(self,userId='',roleId='',username='',loginId='',mobile=''):
         '''修改账号'''
         try:
             payload ={
                 'partnerNo': self.partnerNo,
                 'id': userId,
                 'role': roleId,
                 'name': username,
                 'loginId': loginId,
                 'mobile': mobile,
             }
             response = HttpClient().post_json(self.__userUpdateApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None