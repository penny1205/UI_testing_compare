from util.unittest.unittestutil import UnitTestUtil
from util.report.reporting import ReportUtil
from util.file.fileutil import FileUtil
from util.mail.sendmail import SendMail

import time

if __name__ == '__main__':
    try:
        bvtcases = UnitTestUtil().discover_pattern(FileUtil.getProjectObsPath() + '/bvt/waybill', '*.py', 'test_.*?')
        ReportUtil().generate_report(bvtcases, 'TMS第四迭代优化BVT测试报告 ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '#4 improve testing report', FileUtil.getProjectObsPath() + '/report/report.html')
        reader = open(FileUtil.getProjectObsPath() + '/report/report.html', 'rb')
        mail_body = reader.read()
        reader.close()
        SendMail().send_mail(['zhangdawei@keking.cn', 'liuxinyu@keking.cn', 'panyuanyuan@keking.cn', 'qihong@keking.cn'],
                             'ahkj@keking.cn', 'redmineonly','mail.keking.cn',
                             'TMS第四迭代优化BVT测试报告 ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), mail_body,
                             {FileUtil.getProjectObsPath() + '/report/report.html'})
    except Exception:
        print('BvtCase run fail!')