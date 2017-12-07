#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.log.log import Log

class StatementSelect(object):
    '''
    客户/供应商对账单分页查询
    /api/tms/finance/verificationBillList
    '''
    __slots__ = ('__statementSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__statementSelectApiUrl = "https://{0}:{1}{2}/api/tms/finance/verificationBillList".format(
            config['tms_api_host'],config['tms_api_port'],config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH'],
        }

    def statement_select(self,currentPage='1',rows='10000',billType='',searchStatus ='',normalCondition='',
                         applyDateFirst='',applyDateLast='',verificDateStart='',verificDateEnd='',
                         sendCity='',arriveCity='',driver='',client='',project='',supplier='',verificStatus=''):
         '''客户/供应商对账单分页查询'''
         try:
             payload ={
                 'currentPage': currentPage,
                 'rows': rows,
                 'billType': billType,                  # 对账单类型，1-客户对账单；2-供应商对账单
                 'searchStatus': searchStatus,          # 查询方式：true:普通查询，false:高级查询,必填
                 'normalCondition': normalCondition,    # 普通查询的查询条件，包括：运单号、上游单号、车牌号、司机姓名、手机号
                 'applyDateFirst': applyDateFirst,
                 'applyDateLast': applyDateLast,
                 'verificDateStart': verificDateStart,  # 核销开始日期，格式：yy-MM-dd
                 'verificDateEnd': verificDateEnd,      # 核销结束日期，格式：yy-MM-dd，必大于核销开始日期
                 'sendCity': sendCity,
                 'arriveCity': arriveCity,
                 'driver': driver,
                 'client': client,
                 'project': project,
                 'supplier': supplier,
                 'verificStatus': verificStatus,   #核销状态，非必填。0：未核销，1：已核销;非必填
             }
             response = HttpClient().get(self.__statementSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception as e:
             Log().error('客户/供应商对账单查询发生异常:{0}'.format(e))
             return None