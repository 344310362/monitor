#!/usr/bin/env python
#coding=utf8
 
"""
使用socket方式来检查服务器的监控状况
"""
 
from optparse import OptionParser
from robot import *
import time
import socket
import sys
import re


reload(sys)
sys.setdefaultencoding('utf8')
# 机器人接口
#webhook = "https://oapi.dingtalk.com/robot/send?access_token=5ea8ca127a25dd6d742c871a28699b29b4def6c9c19ca43c7a45c5b864a9da3d"
webhook = "https://oapi.dingtalk.com/robot/send?access_token=5ea8ca127a25dd6d742c871a28699b29b4def6c9c19ca43c7a45c5b864a9da3d"

robot = DtalkRobot(webhook)

from StringIO import StringIO
 
class check_server:
  """
  该类主要是利用socket建立一个连接以后，发送一个http请求，然后根据返回的状态码，判断主机的健康状况
  """
  def __init__(self,address,port,resource):
    self.address = address
    self.port = port
    self.resource = resource
 
 
  def check(self):
    """
    该方法也是该类的主要方法，包括构建请求资源，解析返回结果等
    """
    if not self.resource.startswith('/'):
      self.resource = '/' + self.resource
 
    request = "GET %s HTTP/1.1\r\nHost:%s\r\n\r\n" %(self.resource,self.address)
 
    #建立一个socket连接
 
    s = socket.socket()
    #设置连接超时时间
    s.settimeout(10)
 
    print "现在开始对 %s 上的 %s 端口连接......" %(self.address,self.port)
 
    try:
      s.connect((self.address,self.port))
      print "连接 %s 上端口 %s 成功" %(self.address,self.port)
      robot.sendText("连接成功", False, ["18850341087"])
      s.send(request)
      response = s.recv(100)
 
    except socket.error,e:
      #robot.sendText("", False, ["18850341087"])
      print "连接%s 上端口 %s 失败 ,原因为:%s" %(self.address,self.port,e)
      message = "连接%s 上端口 %s 失败 ,原因为:%s" %(self.address,self.port,e)
      robot.sendText(message, False, ["18850341087"])
      return False
    finally:
      print "关闭连接"
      s.close()
 
 
    line = StringIO(response).readline()
 
    try:
      (http_version,status,messages) = re.split(r'\s+',line,2)
    except ValueError:
      print "分割响应码失败"
      return False
    print "返回的状态码是%s" %(status)
 
    if status in ['200','301','302']:
 
      print "服务器的监控状况良好"
    else:
 
      print "乖乖，赶快上线看看，咋回事"
 
 
if __name__ == '__main__':
  """
  处理参数
  """
  parser =OptionParser()
  parser.add_option("-a","--address",dest="address" ,default='localhost',help="要检查主机的地址或者主机名")
  parser.add_option('-p','--port',dest="port",type=int,default=80,help="要检查主机的端口")
  parser.add_option('-r','--resource',dest="resource",default="/",help="要检查的资源，比如")
  (options,args) = parser.parse_args()
 
  #开始检测鸟
  while 1==1:
    checks = check_server(options.address,options.port,options.resource) 
    checks.check()
    time.sleep(300)
