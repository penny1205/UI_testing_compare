#__author__ = 'pan'
# -*- coding:utf-8 -*-

import random
from util.log.log import Log
from interface.permission.role_create import RoleCreate
from interface.permission.role_select import RoleSelect
from interface.permission.role_delete import RoleDelete
from interface.permission.user_select import UserSelect
from interface.permission.user_delete import UserDelete

class CreateRole(object):
    '''新增角色'''

    def __init__(self):
        self.logger = Log()

    @staticmethod
    def delete_role(roleId):
        response = RoleDelete().role_delete(roleId)
        if response.json()['code'] == 0:
            pass
        elif response.json()['code'] == 9110015:
            user_list = UserSelect().user_select(roleId=roleId).json()['content']['dataList']
            for user in user_list:
                UserDelete().user_delete(user['id'])

    def create_role(self,roleName,menuJson):
        '''新增角色'''
        try:
            response = RoleCreate().role_create(roleName,menuJson)
            if response.json()['code'] == 0:
                return response.json()['content']
            elif response.json()['code'] == 9110012:
                role_list = RoleSelect().role_select(roleName=roleName).json()['content']['dataList']
                self.delete_role(random.choice(role_list)['roleId'])
                roleId = RoleCreate().role_create(roleName,menuJson).json()['content']
                return roleId
            else:
                return None
        except Exception:
            return None