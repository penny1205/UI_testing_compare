#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class LineUpdate(object):
    '''
    根据ID修改线路
    /api/tms/line/updateLine
    '''
    __slots__ = ('__lineUpdateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__lineUpdateApiUrl = "https://{0}:{1}{2}/api/tms/line/updateLine".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def line_update(self,id='',sendProvince='',sendCity='',arriveProvince ='',arriveCity ='',mileage='',arriveTime='',
                    projectId=''):
         '''根据ID修改线路'''
         try:
             payload ={
                 'id': id,
                 'sendProvince': sendProvince,
                 'sendCity': sendCity,
                 'arriveProvince': arriveProvince,
                 'arriveCity': arriveCity,
                 'mileage': mileage,
                 'arriveTime': arriveTime,
                 'projectId': projectId,
             }
             response = HttpClient().post_json(self.__lineUpdateApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None