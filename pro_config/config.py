# -*- coding: utf-8 -*-

DEBUG=False

SANDBOX=False

#接受apns证书变化的通知
CHAN_REDIS_HOST="10.168.188.86"
CHAN_REDIS_PORT=6380
CHAN_REDIS_DB=0
CHAN_REDIS_PASSWORD=""

REDIS_HOST="10.168.188.86"
REDIS_PORT=6380
REDIS_DB=0
REDIS_PASSWORD=""

MYSQL_HOST = "rdsme36vin2uqrn.mysql.rds.aliyuncs.com"
MYSQL_PORT = 3306
MYSQL_AUTOCOMMIT = True
MYSQL_CHARSET = 'utf8'

MYSQL_USER = "gobelieve"
MYSQL_PASSWD = "123456"


MYSQL_IM_DATABASE = "gobelieve"
MYSQL_GB_DATABASE = "gobelieve"


# host,port,user,password,db,auto_commit,charset
MYSQL_IM = (MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_IM_DATABASE, MYSQL_AUTOCOMMIT, MYSQL_CHARSET)

MYSQL = (MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_GB_DATABASE, MYSQL_AUTOCOMMIT, MYSQL_CHARSET)



SOCKS5_PROXY = 'socks5://127.0.0.1:7778'
