#__author__ = 'pan'
# -*- coding:utf-8 -*-

import string
import random
import unittest
from util.log.log import Log
from util.data.datautil import DataUtil
from interface.permission.user_delete import UserDelete
from bvt.common.create_user import CreateUser

class TestUserDelete(unittest.TestCase):
    '''删除账号'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestUserDelete START ###########################')
        roleName = random.choice(['管理', '财务', '调度', '测试'])
        menuJson = '[{"menuName":"首页","menuCode":10000},{"menuName":"首页-运单查询","menuCode":10001},{"menuName":"首页-运单查询-运输中运单","menuCode":10002},{"menuName":"首页-运单查询-昨日新增运单","menuCode":10003},{"menuName":"首页-运单查询-本月累计运单","menuCode":10004},{"menuName":"首页-运单支付","menuCode":10005},{"menuName":"首页-运单支付-待审批的运单","menuCode":10006},{"menuName":"首页-运单支付-尾款运费待支付","menuCode":10007},{"menuName":"首页-我的账户","menuCode":10008},{"menuName":"首页-我的账户-已申请笔数","menuCode":10009},{"menuName":"首页-我的账户-申请提款金额（元）","menuCode":10010}]'
        name = random.choice(['子君','唐晶','贺涵','penny'])
        username = random.choice(['zijun','tangjin','hehan','penny'])
        mobile = DataUtil().createmoble()
        isLoginApp = random.choice([0,1])
        carType=random.choice(['','1','2'])
        self.userId = CreateUser().create_user(roleName,menuJson,name,username,mobile,isLoginApp,carType)[0]

    def tearDown(self):
        self.logger.info('############################ TestUserDelete END ############################')

    def test_user_delete_success(self):
        '''删除账号'''
        response = UserDelete().user_delete(self.userId)
        self.logger.info('删除账号返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('删除账号返回结果是：{0}'.format(response.json()))

if __name__ == '__main__':
    unittest.main()