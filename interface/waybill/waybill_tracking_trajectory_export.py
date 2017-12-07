from util.config.yaml.readyaml import ReadYaml
from util.http.httpclient import HttpClient
from util.file.fileutil import FileUtil
from util.log.log import Log


class WayBillTrackingTrajectoryExport(object):
    '''
    运单跟踪定位信息批量导出
    /api/tms/wayBill/listExportMessage
    '''
    __slots__ = ('__wayBillTrackingTrajectoryCreateApiUrl', '__head_dict')

    def __init__(self):
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.__wayBillTrackingTrajectoryCreateApiUrl = 'https://{0}:{1}{2}/api/tms/wayBill/listExportMessage'.\
            format(config['tms_api_host'], config['tms_api_port'], config['tms_api_path'])
        self.__head_dict = {
            'token': config['tms_api_token'],
            'YD_OAUTH': config['tms_api_YD_OAUTH']
        }

    def waybill_tracking_trajectory_export(self, normalCondition='',billStatus='',carNo='',sendCity='',arriveCity='',
                                           sendDateFirst='',sendDateLast=''):
        '''运单跟踪定位信息批量导出'''
        try:
            payload = {
                'normalCondition': normalCondition,
                'billStatus': billStatus,
                'carNo': carNo,
                'sendCity': sendCity,
                'arriveCity': arriveCity,
                'sendDateFirst': sendDateFirst,
                'sendDateLast': sendDateLast,
            }
            response = HttpClient().post_json(self.__wayBillTrackingTrajectoryCreateApiUrl, None, self.__head_dict,payload)
            return response
        except Exception as e:
            Log().error('添加跟踪备注信息发生异常:{0}'.format(e))
            return None