#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开

#利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：

from xml.parsers.expat import ParserCreate
from urllib import request
import ssl


class WeatherModel(object):
    def __init__(self):
        self.city = ''
        self.forecast = []

class WeatherXMLHandler(object):
    def __init__(self, model):
        self.model = model

    def start_element(self, name, attrs):
        if name == 'yweather:condition' or name == 'yweather:forecast':
            self.model.forecast.append(attrs)
        elif name == 'yweather:location':
            self.model.city = attrs['city']

def parseXml(xml_str):
    print(xml_str)
    model = WeatherModel()
    handler = WeatherXMLHandler(model)
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element

    parser.Parse(xml_str)
    return {
        'city': model.city,
        'forecast': model.forecast,
    }




# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4,context = ssl._create_unverified_context()) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'

print('ok')