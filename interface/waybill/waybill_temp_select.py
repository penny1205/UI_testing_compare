#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillTempSelect(object):
    '''
    查询临时运单列表
    /api/tms/tmpWayBill/tmpWayBillList
    '''
    __slots__ = ('__wayBillTempSelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillTempSelectApiUrl = 'https://{0}:{1}{2}/api/tms/tmpWayBill/tmpWayBillList'.format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_temp_select(self,currentPage='1',rows='10',searchMode='',globalCondition='',applyDateFirst='',
                            applyDateLast='',sendCity='',arriveCity='',name='',carNo='',tmpBillStatus=''):
         '''查询临时运单列表'''
         try:

             payload = {
                 'currentPage': currentPage,         # 当前页面，必须为大于0的整数，必填
                 'rows': rows,                       # 每页显示的条数，必须为大于0的整数，必填
                 'searchMode': searchMode,           # global:全部字段模糊查询general：普通条件查询，不传为高级查询
                 'globalCondition': globalCondition, # 全部字段模糊查询条件
                 'applyDateFirst': applyDateFirst,   # 发车日期区间，日期格式为（yyyy - MM - dd）
                 'applyDateLast': applyDateLast,     # 发车日期区间，日期格式为（yyyy - MM - dd）, 结束日期必须大于开始日期
                 'sendCity': sendCity,               # 发货城市，模糊查询, 最大长度10；
                 'arriveCity': arriveCity,           # 到达城市，模糊查询, 最大长度10；
                 'name': name,                       # 司机姓名，模糊查询, 最大长度10；
                 'carNo': carNo,                     # 车牌号，模糊查询, 最大长度7；
                 'tmpBillStatus':tmpBillStatus       # 开单状态：0，未开单；1，开单失败；，必填，只有这两个值；
             }
             response = HttpClient().get(self.__wayBillTempSelectApiUrl,self.__head_dict,payload)
             return response
         except Exception:
             return None

