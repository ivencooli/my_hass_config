#! usr/bin/python
#coding=utf-8
import json
import urllib
import math
import urllib.request
import urllib.parse
import sys
arg = sys.argv[1]
serchcontext = {'type':'search','s':arg}
serchcontext =  urllib.parse.urlencode(serchcontext)
ret = urllib.request.urlopen("%s?%s" % ("https://api.imjad.cn/cloudmusic", serchcontext))
print(ret.status)
res = ret.read().decode('utf-8')
json_obj = json.loads(res)
if not 'result' in json_obj:
	print("error")
songid = json_obj['result']['songs'][0]['id']

geturl = urllib.request.urlopen("https://api.imjad.cn/cloudmusic/?id=%s" %songid)
geturl = geturl.read().decode('utf-8')
json_objurl = json.loads(geturl)
musicurl = json_objurl['data'][0]['url']
f=open('/home/pi/.homeassistant/python_scripts/set_music_url.py','r')
flist=f.readlines()
flist[2]='musicurl='+'"'+musicurl+'"'+"\r\n"

f=open('/home/pi/.homeassistant/python_scripts/set_music_url.py','w')
f.writelines(flist)


f.close()
