#__author__ = 'pan'
# -*- coding:utf-8 -*-

import unittest
from util.log.log import Log
from interface.permission.menu_refresh import MenuRefresh

class TestMenuRefresh(unittest.TestCase):
    '''刷新全局菜单缓存'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestMenuRefresh START ###########################')

    def tearDown(self):
        self.logger.info('############################ TestMenuRefresh END ############################')

    def test_menu_refresh_success(self):
        '''刷新全局菜单缓存'''
        response = MenuRefresh().menu_refresh()
        self.logger.info('刷新全局菜单缓存返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('刷新全局菜单缓存返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()