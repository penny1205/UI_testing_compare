# __author__ = 'pan'
# -*- coding:utf-8 -*-

import string
import random
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.permission.user_update import UserUpdate
from bvt.common.create_user import CreateUser


class TestUserUpdate(unittest.TestCase):
    '''修改账号'''

    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestUserGet START ###########################')
        roleName = random.choice(['管理', '财务', '调度', '测试'])
        menuJson = '[{"menuName":"首页","menuCode":10000},{"menuName":"首页-运单查询","menuCode":10001},{"menuName":"首页-运单查询-运输中运单","menuCode":10002},{"menuName":"首页-运单查询-昨日新增运单","menuCode":10003},{"menuName":"首页-运单查询-本月累计运单","menuCode":10004},{"menuName":"首页-运单支付","menuCode":10005},{"menuName":"首页-运单支付-待审批的运单","menuCode":10006},{"menuName":"首页-运单支付-尾款运费待支付","menuCode":10007},{"menuName":"首页-我的账户","menuCode":10008},{"menuName":"首页-我的账户-已申请笔数","menuCode":10009},{"menuName":"首页-我的账户-申请提款金额（元）","menuCode":10010}]'
        self.username = random.choice(['蔡志伟', '刘新宇', 'penny'])
        self.loginId = random.choice(string.ascii_letters)
        self.mobile = DataUtil().createmoble()
        self.userId,self.roleId = CreateUser().create_user(roleName, menuJson, self.username, self.loginId, self.mobile)

    def tearDown(self):
        self.logger.info('############################ TestUserGet END ############################')

    def test_user_update_mobile_success(self):
        '''修改账号的手机号'''
        mobile_update = DataUtil().createmoble()
        response = UserUpdate().user_update(self.userId,self.roleId,self.username,self.loginId,mobile_update)
        self.logger.info('修改账号的手机号返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('修改账号的手机号返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()