#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class UserSelect(object):
    '''
    账号列表查询
    /api/tms/system/listTmsUserByPartnerNo
    '''
    __slots__ = ('__userSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__userSelectApiUrl = 'https://{0}:{1}{2}/api/tms/system/listTmsUserByPartnerNo'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def user_select(self,currentPage='1',rows='10',roleId='',username='',searchType=''):
         '''账号列表查询'''
         try:
             payload ={
                 'currentPage': currentPage,
                 'rows': rows,
                 'role': roleId,
                 'name': username,
                 'searchType': searchType,
             }
             response = HttpClient().get(self.__userSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None