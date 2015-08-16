__author__ = 'jack'
# -*- coding:utf-8 -*-
import requests
import re
import bs4
import getpass
import string
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class Stu:
    def __init__(self):
        self.User_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36"
        # 登录网址
        self.loginUrl = "http://jwc.wyu.edu.cn/student/logon.asp"
        # 验证码网址
        self.radomUrl = "http://jwc.wyu.edu.cn/student/rndnum.asp"
        # 获取分数网址
        self.socreUrl = "http://jwc.wyu.edu.cn/student/f4_myscore11.asp"

        LogonHeader={
                    "User-agent":self.User_agent,
                    "Referer":"http://jwc.wyu.edu.cn/student/body.htm"
                }

        # 创建会话
        self.s = requests.session()
        # 获取验证码
        rLogon = self.s.get(url=self.radomUrl, params=None, headers=LogonHeader)
        for k in rLogon.cookies:
            if k.name == "LogonNumber":
                global LogonNumber
                try:
                    LogonNumber = k.value
                except KeyError:
                    print "验证码获取失败！"
                    break;



    def getPage(self):
        status=1
        # 取得分数的请求头部
        loginHeader={
            "Host":"jwc.wyu.edu.cn",
            "Origin":"http://jwc.wyu.edu.cn",
            "Referer":"http://jwc.wyu.edu.cn/student/body.htm",
            "User-agent":self.User_agent
        }
        while status:
            # 用户数据构建
            stuNumber=raw_input("学号:")
            #stuPassword=raw_input("密码:")
            stuPassword=getpass.getpass("密码:")
            values={
                "UserCode":stuNumber,
                "UserPwd":stuPassword,
                "Validate":LogonNumber
            }

            rLogin = self.s.post(url=self.loginUrl,data=values,headers=loginHeader)
            if rLogin.status_code==200:
                status=0
            else:
                status=1
                print "密码错误，请重新输入"

        scoreHeader={
            "Referer":"http://jwc.wyu.edu.cn/student/menu.asp",
            "User-agent":self.User_agent
        }

        self.rScore = self.s.get(url=self.socreUrl,headers=scoreHeader)
        # 查看一下网页的编码，比如是gbk的话，就r.encoding='gbk'。一下内容摘自requests文档
        # Requests会自动解码来自服务器的内容。大多数unicode字符集都能被无缝地解码。
        # 请求发出后，Requests会基于HTTP头部对响应的编码作出有根据的推测。当你访问 r.text 之时，Requests会使用其推测的文本编码。你可以找出Requests使用了什么编码，并且能够使用 r.encoding 属性来改变它:
        self.rScore.encoding="gb2312"

    def getGrade(self):
        # 课程
        self.course=[]
        # 科目类型
        self.category=[]
        #学分list
        self.credit = []
        #成绩list
        self.grades = []
        page = self.getPage()
        # 模式匹配
        patten = re.compile(r"""<tr.*?
                            <td.*?<p.*?>.*?</p>.*?</td>.*?
                            <td.*?<p.*?<span.*?>(.*?)</span>.*?</p>.*?</td>.*?
                            <td.*?<p.*?<span.*?>(.*?)</span>.*?</p>.*?</td>.*?
                            <td.*?<p.*?<span.*?>(.*?)</span>.*?</p>.*?</td>.*?
                            <td.*?<p.*?<span.*?>(.*?)</span>.*?</p>.*?</td>
                             .*?</tr>
                            """,re.I|re.S|re.X)
        match = patten.findall(self.rScore.text)
        for item in match:
            print item[0]+item[1]+item[2]+item[3]
            self.course.append(item[0])
            self.category.append(item[1])
            self.credit.append(item[2])
            self.grades.append(item[3])
        self.Grade()

    def Grade(self):
        #计算总绩点
        sum = 0.0
        weight = 0.0
        count = 0
        for i in range(len(self.credit)):
            if self.category[i] == "必修":
                count=count+1
                if self.grades[i].isdigit() and string.atof(self.grades[i]) >= 60:
                    sum += (string.atof(self.grades[i])-60)*0.1*string.atof(self.credit[i])
                            # sum += string.atof(self.credit[i])*string.atof(self.grades[i])
                    # global weight
                    weight=sum/count
        print weight

sdu = Stu()
sdu.getGrade()