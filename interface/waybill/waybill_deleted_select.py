#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillDeletedSelect(object):
    '''
    回收站运单列表查询
    /api/tms/wayBill/getDelWayBillList
    '''
    __slots__ = ('__wayBillDeletedSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillDeletedSelectApiUrl = "https://{0}:{1}{2}/api/tms/wayBill/getDelWayBillList".format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_deleted_select(self,currentPage='1',rows='10',delDateFirst='',delDateLast='', delOperator=''):
         '''回收站运单列表查询'''
         try:
             payload ={
             'currentPage': currentPage,
             'rows': rows,
             'delDateFirst': delDateFirst,
             'delDateLast': delDateLast,
             'delOperator':delOperator,
             }
             response = HttpClient().get(self.__wayBillDeletedSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None

