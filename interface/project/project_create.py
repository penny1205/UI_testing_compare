#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class ProjectCreate(object):
    '''
    新增项目
   /api/tms/customer/addProject
    '''
    __slots__ = ('__selectProjectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__selectProjectApiUrl = "https://{0}:{1}{2}/api/tms/customer/addProject".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def project_create(self,projectName='',custId='',startTime ='',endTime=''):
         '''新增项目'''
         try:
             payload ={
                 'projectName': projectName,
                 'custId': custId,
                 'startTime': startTime,
                 'endTime': endTime,
             }
             response = HttpClient().post_json(self.__selectProjectApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None