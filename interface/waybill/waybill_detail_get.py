#__author__ = 'pan'
# -*- coding:utf-8 -*-

from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WayBillDetailGet(object):
    '''
    获取运单详情
    /api/tms/wayBill/getWayBillDetail
    '''
    __slots__ = ('__getWayBillDetailApiUrl', '__head_dict')

    def __init__(self):

        config = ReadYaml( FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__getWayBillDetailApiUrl = "https://{0}:{1}{2}/api/tms/wayBill/getWayBillDetail".format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token']}

    def waybill_detail_get(self,wayBillId=''):
        '''获取运单详情'''
        try:
            payload = {'wayBillId': wayBillId}
            response = HttpClient().post_form(self.__getWayBillDetailApiUrl,payload,self.__head_dict)
            return response
        except Exception:
            return None