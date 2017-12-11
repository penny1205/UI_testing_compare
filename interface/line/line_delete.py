#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log


class LineDelete(object):
    '''
    根据ID删除线路
    /api/tms/line/deleteLineById
    '''
    __slots__ = ('__lineDeleteApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__lineDeleteApiUrl = "https://{0}:{1}{2}/api/tms/line/deleteLineById".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def line_delete(self,id=''):
         '''根据ID删除线路'''
         try:
             payload ={
                 'id': id,
             }
             response = HttpClient().post_form(self.__lineDeleteApiUrl,payload,self.__head_dict)
             return response
         except Exception as e:
             Log().error('根据ID删除线路发生异常:{0}'.format(e))
             return None