import unittest
from parameterized import parameterized
from util.log.log import Log
from interface.waybill.waybill_select import WayBillSelect

class TestSelectWayBill(unittest.TestCase):
    '''运单查询'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestSelectWayBill START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestSelectWayBill END ############################')
        pass

    @parameterized.expand([
        ('13077327043'),
    ])
    def test_select_waybill_mobile_success(self,mobile):
        response = WayBillSelect().waybill_select(normalCondition=mobile, searchStatus=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        waybill_list = response.json()['content']['dataList']
        for waybill in waybill_list:
            self.assertEqual(waybill['mobile'],mobile)


if __name__ == '__main__':
    unittest.main()