#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil

class StatementExport(object):
    '''
    客户/供应商对账单导出
    /api/tms/finance/exportVerificBill
    '''
    __slots__ = ('__statementExportApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__statementExportApiUrl = "https://{0}:{1}{2}/api/tms/finance/exportVerificBill".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def statement_export(self,billType='',applyDateFirst='',applyDateLast='',verificDateStart='',verificDateEnd='',
                         sendCity='',arriveCity='',driver='',project='',supplier='',verificStatus=''):
         '''客户/供应商对账单导出'''
         try:
             payload ={
                 'billType': billType,  # 对账单类型，1-客户对账单；2-供应商对账单
                 'applyDateFirst': applyDateFirst,
                 'applyDateLast': applyDateLast,
                 'verificDateStart': verificDateStart,
                 'verificDateEnd': verificDateEnd,
                 'sendCity': sendCity,
                 'arriveCity': arriveCity,
                 'driver': driver,
                 'project': project,
                 'supplier': supplier,
                 'verificStatus': verificStatus,   #核销状态，非必填。0：未核销，1：已核销;非必填
             }
             response = HttpClient().post_form(self.__statementExportApiUrl,payload,self.__head_dict)
             return response
         except Exception:
             return None