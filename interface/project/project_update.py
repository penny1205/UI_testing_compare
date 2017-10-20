#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class ProjectUpdate(object):
    '''
    修改项目
    /api/tms/customer/updateProject
    '''
    __slots__ = ('__projectUpdateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__projectUpdateApiUrl = "https://{0}:{1}{2}/api/tms/customer/updateProject".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def project_update(self,projectId='',updateType='',projectName='',custId='',startTime ='',endTime=''):
         '''修改项目'''
         try:
             payload ={
                 'projectId':projectId,
                 'updateType':updateType,
                 'projectName': projectName,
                 'custId': custId,
                 'startTime': startTime,
                 'endTime': endTime,
             }
             response = HttpClient().post_json(self.__projectUpdateApiUrl,payload,self.__head_dict,payload)
             return response
         except Exception:
             return None