#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class ProjectSelect(object):
    '''
    查询项目列表
   /api/tms/customer/listProjects
    '''
    __slots__ = ('__projectSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__projectSelectApiUrl = "https://{0}:{1}{2}/api/tms/customer/listProjects".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def project_select(self,currentPage='1',rows='10',projectStatus ='',projectName=''):
         '''我的外请车列表'''
         try:
             payload ={
                 'currentPage': currentPage,
                 'rows': rows,
                 'projectStatus': projectStatus,
                 'projectName': projectName,
             }
             response = HttpClient().get(self.__projectSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None