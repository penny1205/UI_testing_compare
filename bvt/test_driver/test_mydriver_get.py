#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.driver.mydriver_get import MyDriverGet
from bvt.common.create_mydriver import CreateMyDriver

class TestMyDriverGet(unittest.TestCase):
    '''查看我的司机详情'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestMyDriverGet START ###########################')
        self.mobile = DataUtil().createmoble()
        self.name = '王师傅'
        self.idNo = DataUtil().genneratorIdNo()
        self.photoDriverCard = 'http://yudian.ufile.ucloud.com.cn/a0e806f9-c3d3-479d-bca4-e992a0c7412c.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=BOj9MjmPyxmvu0wzzlJVGoueyx8='
        self.frontIdCard = 'http://yudian.ufile.ucloud.com.cn/df03e2a2-6751-488e-9f1f-ec60a1da49fa.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=b3XzoIcs67/0D6ZExdG0fWbjUzc='
        self.backIdCard = 'http://yudian.ufile.ucloud.com.cn/4acb87e0-8c0d-44a9-a1b3-b8cb7ca103d1.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=XfbOAUgpkjIe1FJU/hxiMqfsWno='
        self.driverId = CreateMyDriver().create_my_driver(self.mobile, self.name, self.idNo, self.photoDriverCard,
                                                     self.frontIdCard, self.backIdCard)

    def tearDown(self):
        self.logger.info('############################ TestMyDriverGet END ############################')

    def test_my_driver_get_success(self):
        '''查看我的司机详情'''
        response = MyDriverGet().my_driver_get(self.driverId)
        self.logger.info('查看我的司机详情返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('查看我的司机详情是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()