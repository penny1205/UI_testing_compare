#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class LineGet(object):
    '''
    根据ID获取线路
    /api/tms/line/getLineById
    '''
    __slots__ = ('__lineGetApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__lineGetApiUrl = "https://{0}:{1}{2}/api/tms/line/getLineById".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def line_get(self,id=''):
         '''根据ID获取线路'''
         try:
             payload ={
                 'id': id,
             }
             response = HttpClient().get(self.__lineGetApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('根据ID获取线路发生异常:{0}'.format(e))
             return None