#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开


from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('handle_starttag <%s>' % tag )
        print('attrs:',attrs)

    def handle_endtag(self, tag):
        print('handle_endtag </%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('handle_startendtag:<%s/>' % tag)

    def handle_data(self, data):
        print('handle_data:%s' % data)

    def handle_comment(self, data):
        print('handle_comment:<!--', data, '-->')

    def handle_entityref(self, name):
        print('handle_entityref:&%s;' % name)

    def handle_charref(self, name):
        print('handle_charref:&#%s;' % name)



parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\" aa=32>html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')