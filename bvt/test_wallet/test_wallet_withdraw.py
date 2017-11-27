# #__author__ = 'pan'
# # -*- coding:utf-8 -*-
#
# import random
# import unittest
# from util.log.log import Log
# from interface.wallet.wallet_withdraw import WalletWithdraw
# from interface.wallet.wallet_withdraw_status_get import WalletWithdrawStatusGet
#
# class TestWalletWithdraw(unittest.TestCase):
#     '''钱包提现申请'''
#     def setUp(self):
#         self.logger = Log()
#         self.logger.info('########################### TestWalletWithdraw START ###########################')
#         self.status = WalletWithdrawStatusGet().wallet_withdraw_status_get().json()['content']
#         self.pwdPay = '123321'
#
#     def tearDown(self):
#         self.logger.info('############################ TestWalletWithdraw END ############################')
#
#
#     def test_wallet_withdraw_success(self):
#         '''钱包提现申请'''
#         if self.status == 3:
#             moneyOrder = round(random.uniform(0,0.01),2)
#             self.logger.info('钱包提现金额：{0}'.format(moneyOrder))
#             response = WalletWithdraw().wallet_withdraw(self.pwdPay,moneyOrder)
#             self.logger.info('钱包提现申请返回状态码：{0}'.format(response))
#             self.assertEqual(response.status_code, 200)
#             self.assertEqual(response.json()['code'], 0)
#             self.logger.info('钱包提现申请返回结果是：{0}'.format(response.json()))
#         else:
#             self.logger.info('钱包提现状态：{0}, 今日不可再次提现'.format(self.status))
#
#
# if __name__ == '__main__':
#     unittest.main()