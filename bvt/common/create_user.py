#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
from util.log.log import Log
from interface.permission.user_create import UserCreate
from interface.permission.user_select import UserSelect
from interface.permission.user_delete import UserDelete
from interface.permission.role_company_get import RoleCompanyGet
from bvt.common.create_role import CreateRole

class CreateUser(object):
    '''新增账号'''

    def __init__(self):
        self.logger = Log()

    def create_user(self,roleName,menuJson,username,loginId,mobile):
        '''新增账号'''
        try:
            role_list = RoleCompanyGet().role_company_get().json()['content']
            if role_list == []:
                roleId = CreateRole().create_role(roleName,menuJson)
                self.logger.info('公司没有角色时新增角色,新增角色名称是:{0}'.format(roleName))
            else:
                roleId = random.choice(role_list)['roleId']
                self.logger.info('新增账号的角色ID是:{0}'.format(roleId))
            response = UserCreate().user_create(roleId,username,loginId,mobile)
            if response.json()['code'] == 0:
                return response.json()['content'],roleId
            elif response.json()['code'] == 9110028:
                user_list = UserSelect().user_select().json()['content']['dataList']
                for user in user_list:
                    if user['loginId'] == loginId:
                        UserDelete().user_delete(user['id'])
                userId = UserCreate().user_create(roleId, username, loginId, mobile).json()['content']
                return userId,roleId
            elif response.json()['code'] == 9110029:
                user_list = UserSelect().user_select().json()['content']['dataList']
                for user in user_list:
                    if user['mobile'] == mobile:
                        UserDelete().user_delete(user['id'])
                userId = UserCreate().user_create(roleId, username, loginId, mobile).json()['content']
                return userId,roleId
            else:
                self.logger.info('新增账号返回错误:{0}'.format(response.json()))
                return None,None
        except Exception:
            self.logger.info('新增账号发生异常:{0}'.format(Exception))
            return None