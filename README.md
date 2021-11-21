# NsfocusUpdate
NSFOCUS升级站点爬取升级包


## 1 概述

由于 [update.nsfocus.com](http://update.nsfocus.com) 升级站点下载升级包有速率限制，为了在急需升级包的时候能最快速度下载升级包，因此搭建了本地离线升级站点。

## 2 技术栈

- python 3.8.5

## 3 部署环境

- 基于ubuntu 18.04.6 LTS版本

### 3.1 下载NsfocusUpdate

```shell
root@miki:~# cd /opt/
root@miki:/opt# git clone https://github.com/mik1th0n/NsfocusUpdate.git
```

### 3.2 安装依赖包

```shell
root@miki:/opt# cd NsfocusUpdate/
root@miki:/opt/NsfocusUpdate# pip3 install requests
```

## 4 运行程序

### 4.1 运行单个程序

```
python3 
```













## 其他安装说明（未整理）

xadmin 

验证码模块：https://github.com/mbi/django-simple-captcha

dash: https://gitlab.com/k3oni/pydash-django-app/tree/master

安全过滤初步想法：通过重载 SessionMiddleware 中间件来实现 或者自定义中间件

排行榜性能优化：signals实现缓存  或者 字段添加索引

邮箱验证注册功能

WP提交功能

## 注意事项

最后部署生产环境要更改 SECRET_KEY 

## 补充

DjangoCon 2008: Reusable Apps： https://www.youtube.com/watch?v=A-S0tqpPga4&feature=youtu.be

测试工具：coverage

API View: GenericAPIView

数据填充：Django  fixture

api验证： JWT  ： http://getblimp.github.io/django-rest-framework-jwt/

CORS实现：django-cors-headers

日志记录：logging


手机（邮箱）验证码方式进行登陆：

界面1： 手机号 验证码  用户名  密码

界面2： 跳转登陆界面后 -> 完善用户名、学号、班级、年级等信息


## 附加工具

redis监控： http://www.treesoft.cn/dms.html

sentry: https://github.com/getsentry/sentry
