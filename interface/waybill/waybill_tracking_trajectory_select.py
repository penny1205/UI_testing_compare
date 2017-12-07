from util.config.yaml.readyaml import ReadYaml
from util.http.httpclient import HttpClient
from util.file.fileutil import FileUtil
from util.log.log import Log


class WayBillTrackingTrajectorySelect(object):
    '''
    查询手动运单跟踪轨迹
    /api/tms/wayBill/listManualTrajectory
    '''
    __slots__ = ('__wayBillTrackingTrajectorySelectApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillTrackingTrajectorySelectApiUrl = 'https://{0}:{1}{2}/api/tms/wayBill/listManualTrajectory'.\
            format(config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_tracking_trajectory_select(self, wayBillId=''):
        '''查询手动运单跟踪轨迹'''
        try:
            payload = {
                'wayBillId': wayBillId,
            }
            response = HttpClient().get(self.__wayBillTrackingTrajectorySelectApiUrl,self.__head_dict,payload)
            return response
        except Exception as e:
            Log().error('查询手动运单跟踪轨迹发生异常:{0}'.format(e))
            return None