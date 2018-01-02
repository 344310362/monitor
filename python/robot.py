#!/usr/bin/env python
# coding=utf-8

"""
author：xiewq@linesum.com
"""

import urllib2
import json
import time

class DtalkRobot(object):
    webhook = ""

    def __init__(self, webhook):
        super(DtalkRobot, self).__init__()
        self.webhook = webhook

    # text类型
    def sendText(self, msg, isAtAll=False, atMobiles=[]):
        data = {"msgtype": "text", "text": {"content": msg}, "at": {"atMobiles": atMobiles, "isAtAll": isAtAll}}
        return self.post(data)

    # markdown类型
    def sendMarkdown(self, title, text):
        data = {"msgtype": "markdown", "markdown": {"title": title, "text": text}}
        return self.post(data)

    # link类型
    def sendLink(self, title, text, messageUrl, picUrl=""):
        data = {"msgtype": "link", "link": {"text": text, "title": title, "picUrl": picUrl, "messageUrl": messageUrl}}
        return self.post(data)

    # ActionCard类型
    def sendActionCard(self, actionCard):
        data = actionCard.getData();
        return self.post(data)

    # FeedCard类型
    def sendFeedCard(self, links):
        data = {"feedCard": {"links": links}, "msgtype": "feedCard"}
        return self.post(data)

    def post(self, data):
        post_data = json.JSONEncoder().encode(data)
        print post_data
        req = urllib2.Request(webhook, post_data)
        req.add_header('Content-Type', 'application/json')
        content = urllib2.urlopen(req).read()
        return content


# ActionCard类型消息结构
class ActionCard(object):
    """docstring for ActionCard"""
    title = ""
    text = ""
    singleTitle = ""
    singleURL = ""
    btnOrientation = 0
    hideAvatar = 0
    btns = []

    def __init__(self, arg=""):
        super(ActionCard, self).__init__()
        self.arg = arg

    def putBtn(self, title, actionURL):
        self.btns.append({"title": title, "actionURL": actionURL})

    def getData(self):
        data = {"actionCard": {"title": self.title, "text": self.text, "hideAvatar": self.hideAvatar,
                               "btnOrientation": self.btnOrientation, "singleTitle": self.singleTitle,
                               "singleURL": self.singleURL, "btns": self.btns}, "msgtype": "actionCard"}
        return data


# FeedCard类型消息格式
class FeedLink(object):
    """docstring for FeedLink"""
    title = ""
    picUrl = ""
    messageUrl = ""

    def __init__(self, arg=""):
        super(FeedLink, self).__init__()
        self.arg = arg

    def getData(self):
        data = {"title": self.title, "picURL": self.picUrl, "messageURL": self.messageUrl}
        return data


# 测试
webhook = "https://oapi.dingtalk.com/robot/send?access_token=5ea8ca127a25dd6d742c871a28699b29b4def6c9c19ca43c7a45c5b864a9da3d"
#webhook = "https://oapi.dingtalk.com/robot/send?access_token=9759a686ebd54562f15ed7d0f19de188e5d91f8b1a00a92812afad75f3a8c41d"
if __name__ == "__main__":
    robot = DtalkRobot(webhook)
    print robot.sendText("现在时间：[" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "]", False, ["18850341087","15705924625"])
