import os
import unittest
from util.log.log import Log
from util.file.fileutil import FileUtil
from interface.waybill.waybill_temp_select import WayBillTempSelect
from bvt.common.settings import Settings
from bvt.common.create_waybill import CreateWayBill

class TestWayBillTempSelect(unittest.TestCase):
    '''查询临时运单列表'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('##################### TestWayBillTempSelect START #####################')
        Settings().system_params_update()
        file = FileUtil.getProjectObsPath() + os.path.sep + 'file' + os.path.sep + 'waybill_temp_import.xlsx'
        self.logger.info('批量导入运单的文件是：{0}'.format(file))
        self.temp_waybillId = CreateWayBill().create_temp_waybill(file, '德邦物流', '德邦集团', 'DB20171101100')

    def tearDown(self):
        self.logger.info('##################### TestWayBillTempSelect END #######################')

    def test_waybill_temp_select_success(self):
        '''查询临时运单列表'''
        response = WayBillTempSelect().waybill_temp_select(searchMode='general',globalCondition='德邦物流')
        temp_waybill_list = response.json()['content']['dataList']
        if temp_waybill_list != None:
            L = []
            for temp_waybill in temp_waybill_list:
                L.append(temp_waybill['id'])
            self.assertIn(self.temp_waybillId, L, '查询临时运单列表失败!')
        else:
            self.logger.error('查询临时运单列表失败!')

if __name__ == '__main__':
    unittest.main()