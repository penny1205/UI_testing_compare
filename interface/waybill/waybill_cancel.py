from util.config.yaml.readyaml import ReadYaml
from util.http.httpclient import HttpClient
from util.file.fileutil import FileUtil

class WayBillCancel(object):
    __slots__ = ('__cancelWayBillApiUrl', '__token_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__cancelWayBillApiUrl =  'http://{0}:{1}{2}/payment/tmsDelWayBill'.format(config['app_api_host'],config['app_api_port'],config['app_api_path'])
        self.__token_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_cancel(self, wayBillId):
        try:
            cancel_data_dict = {'billId': wayBillId, 'cancleReason': 'CancelByQaPythonTesting'}
            response = HttpClient().post_json(self.__cancelWayBillApiUrl, cancel_data_dict, self.__token_dict)
            return response
        except Exception:
            return None