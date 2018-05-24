#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开




def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # return [b'<h1>Hello, web!</h1>']
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
