#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class ProjectGet(object):
    '''
    获取项目详情
    /api/tms/customer/getProject
    '''
    __slots__ = ('__projectGetApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__projectGetApiUrl = "https://{0}:{1}{2}/api/tms/customer/getProject".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def project_get(self,projectId=''):
         '''获取项目详情'''
         try:
             payload ={
                 'projectId': projectId,
             }
             response = HttpClient().get(self.__projectGetApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None