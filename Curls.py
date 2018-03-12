#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import pycurl
import json

from io import BytesIO, StringIO

class Curl(object):
 def __init__(self,url):
  self.url=url

 def Curl_site(self):
  c=pycurl.Curl()
  #url="www.luoan.com.cn"
  #indexfile=open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
  c.setopt(c.URL,self.url)
  c.setopt(c.VERBOSE,1)
  c.setopt(c.ENCODING,"gzip")
  #模拟火狐浏览器
  c.setopt(c.USERAGENT,"Mozilla/5.0 (Windows NT 6.1; rv:35.0) Gecko/20100101 Firefox/35.0")
  return c

 def Curl_https_site(self):
   c = pycurl.Curl()
   b = BytesIO()
   c.setopt(pycurl.URL, self.url)
   c.setopt(c.VERBOSE, 0)   #是否状态回显，0为否
   c.setopt(pycurl.WRITEFUNCTION, b.write)
   c.setopt(pycurl.SSL_VERIFYPEER, 0)
   c.setopt(pycurl.SSL_VERIFYHOST, 0)
   #c.setopt(pycurl.CAINFO, r"C:\ca-bundle.crt")
   #c.perform()
   #print(b.getvalue())   #打印网站内容
   #backinfo = ''
   return c

