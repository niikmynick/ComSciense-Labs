from json2xml import json2xml
from json2xml.utils import readfromjson
import time

start_time = time.time()
data = readfromjson('timetable.json')

with open('timetable_lib.xml', 'w', encoding='utf8') as file:
    file.write(json2xml.Json2xml(data).to_xml())

print('%s seconds' % (time.time() - start_time))
