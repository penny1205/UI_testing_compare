#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import unittest
from util.log.log import Log
from interface.permission.role_select import RoleSelect
from bvt.common.create_role import CreateRole

class TestRoleSelect(unittest.TestCase):
    '''角色列表查询'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestRoleSelect START ###########################')
        self.roleName = random.choice(['管理', '财务', '调度', '测试'])
        self.logger.info('新增角色的名称是:{0}'.format(self.roleName))
        menuJson = '[{"menuName":"首页","menuCode":10000},{"menuName":"首页-运单查询","menuCode":10001},{"menuName":"首页-运单查询-运输中运单","menuCode":10002},{"menuName":"首页-运单查询-昨日新增运单","menuCode":10003},{"menuName":"首页-运单查询-本月累计运单","menuCode":10004},{"menuName":"首页-运单支付","menuCode":10005},{"menuName":"首页-运单支付-待审批的运单","menuCode":10006},{"menuName":"首页-运单支付-尾款运费待支付","menuCode":10007},{"menuName":"首页-我的账户","menuCode":10008},{"menuName":"首页-我的账户-已申请笔数","menuCode":10009},{"menuName":"首页-我的账户-申请提款金额（元）","menuCode":10010}]'
        self.roleId = CreateRole().create_role(self.roleName, menuJson)

    def tearDown(self):
        self.logger.info('############################ TestRoleSelect END ############################')

    def test_role_select_success(self):
        '''角色列表查询'''
        response = RoleSelect().role_select(roleName=self.roleName)
        self.logger.info('角色列表查询返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('角色列表查询返回结果是：{0}'.format(response.json()))
        role_list = response.json()['content']['dataList']
        if role_list != []:
            L = []
            for loan in role_list:
                L.append((loan['roleId']))
            self.assertIn(self.roleId, L, 'Role selected fail!')
        else:
            self.logger.error('Please check the results of Role for empty')

if __name__ == '__main__':
    unittest.main()