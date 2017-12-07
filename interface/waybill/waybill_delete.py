from util.config.yaml.readyaml import ReadYaml
from util.http.httpclient import HttpClient
from util.file.fileutil import FileUtil
from util.log.log import Log


class WayBillDelete(object):
    __slots__ = ('__deleteWayBillApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__deleteWayBillApiUrl = 'https://{0}:{1}{2}/api/tms/wayBill/deleteWayBill'.format(
            config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_delete(self, waybillid):
        try:
            delete_data_dict = {'billId': waybillid}
            response = HttpClient().post_form(self.__deleteWayBillApiUrl, delete_data_dict, self.__head_dict)
            return response
        except Exception as e:
            Log().error('删除运单发生异常:{0}'.format(e))
            return None

