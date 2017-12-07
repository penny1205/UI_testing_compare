#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class RoleCompanyGet(object):
    '''
    获取公司所有角色
    /api/tms/system/listTmsRoleByPartnerNo
    '''
    __slots__ = ('__roleDeleteApiUrl','partnerNo', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__roleDeleteApiUrl = 'https://{0}:{1}{2}/api/tms/system/listTmsRoleByPartnerNo'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.partnerNo = config['partnerNo']
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def role_company_get(self):
         '''获取公司所有角色'''
         try:
             payload = {
                 'partnerNo': self.partnerNo,
             }
             response = HttpClient().get(self.__roleDeleteApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('获取公司所有角色发生异常:{0}'.format(e))
             return None