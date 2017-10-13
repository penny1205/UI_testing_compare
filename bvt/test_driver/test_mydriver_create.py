#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.driver.mydriver_select import MyDriverSelect
from bvt.common.create_mydriver import CreateMyDriver

class TestMyDriverCreate(unittest.TestCase):
    '''新增司机'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestMyDriverCreate START ###########################')
        self.mobile = DataUtil().createmoble()
        self.name = '王师傅'
        self.idNo = DataUtil().genneratorIdNo()
        self.photoDriverCard = 'http://yudian.ufile.ucloud.com.cn/a0e806f9-c3d3-479d-bca4-e992a0c7412c.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=BOj9MjmPyxmvu0wzzlJVGoueyx8='
        self.frontIdCard = 'http://yudian.ufile.ucloud.com.cn/df03e2a2-6751-488e-9f1f-ec60a1da49fa.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=b3XzoIcs67/0D6ZExdG0fWbjUzc='
        self.backIdCard = 'http://yudian.ufile.ucloud.com.cn/4acb87e0-8c0d-44a9-a1b3-b8cb7ca103d1.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=XfbOAUgpkjIe1FJU/hxiMqfsWno='

    def tearDown(self):
        self.logger.info('############################ TestMyDriverCreate END ############################')

    def test_my_driver_create_success(self):
        '''新增司机'''
        driverId = CreateMyDriver().create_my_driver(self.mobile,self.name,self.idNo,self.photoDriverCard,
                                                     self.frontIdCard,self.backIdCard)
        my_driver_list = MyDriverSelect().my_driver_select(mobile=self.mobile).json()['content']['dataList']
        if my_driver_list != []:
            L = []
            for my_driver in my_driver_list:
                L.append(str(my_driver['driverId']))
            self.assertIn(driverId, L, 'MyDriver created fail!')
        else:
            self.logger.error('Please check the results of the myDriver for empty!')

if __name__ == '__main__':
    unittest.main()