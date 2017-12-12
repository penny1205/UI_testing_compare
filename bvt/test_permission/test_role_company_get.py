#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
import unittest
from util.log.log import Log
from interface.permission.role_company_get import RoleCompanyGet
from bvt.common.create_role import CreateRole

class TestRoleCompanyGet(unittest.TestCase):
    '''获取公司所有角色'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('########################### TestRoleCompanyGet START ###########################')
        roleName = random.choice(['管理', '财务', '调度', '测试'])
        self.logger.info('新增角色的名称是:{0}'.format(roleName))
        menuJson = '[{"menuName":"首页","menuCode":10000},{"menuName":"首页-运单查询","menuCode":10001},{"menuName":"首页-运单查询-运输中运单","menuCode":10002},{"menuName":"首页-运单查询-昨日新增运单","menuCode":10003},{"menuName":"首页-运单查询-本月累计运单","menuCode":10004},{"menuName":"首页-运单支付","menuCode":10005},{"menuName":"首页-运单支付-待审批的运单","menuCode":10006},{"menuName":"首页-运单支付-尾款运费待支付","menuCode":10007},{"menuName":"首页-我的账户","menuCode":10008},{"menuName":"首页-我的账户-已申请笔数","menuCode":10009},{"menuName":"首页-我的账户-申请提款金额（元）","menuCode":10010}]'
        self.roleId = CreateRole().create_role(roleName, menuJson)

    def tearDown(self):
        self.logger.info('############################ TestRoleCompanyGet END ############################')

    def test_role_company_get_success(self):
        '''获取公司所有角色'''
        response = RoleCompanyGet().role_company_get()
        self.logger.info('获取公司所有角色返回状态码：{0}'.format(response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['code'], 0)
        self.logger.info('获取公司所有角色返回码code：{0}'.format(response.json()['code']))
        role_list = response.json()['content']
        if role_list != []:
            L = []
            for loan in role_list:
                L.append((str(loan['roleId'])))
            self.assertIn(self.roleId, L, '获取公司所有角色失败!')
        else:
            self.logger.error('Please check the results of Role for empty')

if __name__ == '__main__':
    unittest.main()