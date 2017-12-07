#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class MenuRefresh(object):
    '''
    刷新全局菜单缓存
    /api/tms/system/refreshMenuJson
    '''
    __slots__ = ('__menuRefreshApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__menuRefreshApiUrl = 'https://{0}:{1}{2}/api/tms/system/refreshMenuJson'.format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def menu_refresh(self):
         '''刷新全局菜单缓存'''
         try:
             response = HttpClient().get(self.__menuRefreshApiUrl,self.__head_dict)
             return response
         except Exception as e:
             Log().error('刷新全局菜单缓存发生异常:{0}'.format(e))
             return None