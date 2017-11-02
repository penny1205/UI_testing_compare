import os
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_temp_select import WayBillTempSelect
from bvt.common.settings import Settings
from bvt.common.create_waybill import CreateWayBill

class TestWayBillTempImport(unittest.TestCase):
    '''批量导入运单'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('##################### TestWayBillTempImport START #####################')
        Settings().system_params_update()

    def tearDown(self):
        self.logger.info('##################### TestWayBillTempImport END #######################')

    def test_waybill_temp_import_success(self):
        '''批量导入运单'''
        file = FileUtil.getProjectObsPath() + os.path.sep + 'file' + os.path.sep + 'waybill_temp_import.xlsx'
        self.logger.info('批量导入运单的文件是：{0}'.format(file))
        temp_waybillId = CreateWayBill().create_temp_waybill( file, '德邦物流', '德邦集团', 'DB20171101100')
        temp_waybill_list = WayBillTempSelect().waybill_temp_select(searchMode='general',globalCondition='德邦物流'
                                                                    ).json()['content']['dataList']
        if temp_waybill_list != None:
            L = []
            for temp_waybill in temp_waybill_list:
                L.append(temp_waybill['id'])
            self.assertIn(temp_waybillId, L, '批量运单导入失败!')
        else:
            self.logger.error('批量运单导入失败!')

if __name__ == '__main__':
    unittest.main()