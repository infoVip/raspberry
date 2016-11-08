# -*- coding:utf-8 -*-

'''
required:
	mplayer
'''

from urllib import request
import json
import subprocess




def get_weather(city):
	url = 'https://free-api.heweather.com/v5/forecast?key=755a9e2d69da47df9cde15162ccc0d83&city=' + city

	response = request.urlopen(url)

	result = json.loads(response.read().decode('utf8'))

	if 'ok' == result['HeWeather5'][0]['status']:
		return result['HeWeather5'][0]['daily_forecast'][0]
	else:
		raise Exception('找不到结果')


def format_weather(weather):
	return "白天%s,夜间%s,最低温度%s度,最高温度%s度" % (weather['cond']['txt_d'],weather['cond']['txt_n'],weather['tmp']['min'],weather['tmp']['max'])

def play(txt):
	url = 'http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&spd=2&text=' + txt
	cmd = 'mplayer "%s"' % (url,)

	a = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	a.wait()
	

txt = format_weather(get_weather('shanghai'))

play(txt)