import unittest
from parameterized import parameterized
from util.log.log import Log
from interface.waybill.waybill_select import WayBillSelect

class TestWayBillSelect(unittest.TestCase):
    '''运单查询'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestWayBill START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestWayBill END ############################')
        pass

    @parameterized.expand([
        ('13077327043'),
    ])
    def test_waybill_select_success(self,mobile):
        waybill_list = WayBillSelect().waybill_select(normalCondition=mobile, searchStatus=True).json()['content'][
            'dataList']
        print(waybill_list)

if __name__ == '__main__':
    unittest.main()