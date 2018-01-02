#!/usr/bin/env python
# coding=utf-8

from robot import *
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')
# 机器人接口
webhook = "https://oapi.dingtalk.com/robot/send?access_token=5ea8ca127a25dd6d742c871a28699b29b4def6c9c19ca43c7a45c5b864a9da3d"
robot = DtalkRobot(webhook)
while True:
    robot.sendText("各位老板好", False, ["18850341087"])

