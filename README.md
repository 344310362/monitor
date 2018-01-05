## python编写的健康监控服务

>linux上面的服务检测，python脚本编写的心跳检测，发现异常后通知钉钉机器人进行报警。

钉钉机器人
--------
参考：
[钉钉开放平台文档](https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.karFPe&treeId=257&articleId=105735&docType=1)

python
--------
> python目录里面有4个文件

- robot.py 钉钉机器人通知封装类
- webhealth.py 心跳检测中心
- monitorpy.log 日志

 启动

```
python webhealth.py -p 80 -a www.baidu.com -r /aaa/bb.html
```

- a：监听地址
- p：监听端口
- r：监听地址下对应的详细路径（可以不用）

service
--------
>将我们的python脚本程序封装成linux系统服务，方便管理。
1. 将 service 下的 watchpy 拷贝到系统 /etc/init.d
2. chmod +x /etc/init.d/watchpy


* 开启监听服务
```
service watchpy start
```
* 重启监听服务
```
service watchpy start
```
* 停止监听服务
```
service watchpy start
```
* 日志查看
```
tail -f monitorpy.log
```


----
核心脚本是 webhealth.py ,可以自行改造以满足自己的需求。
交流添加微信：
![image](image/wx.jpg)