#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import re
def cutBetween(startword,endword,word,startindex=0,startend=10000000):
	index_start=word.find(startword,startindex,startend)
	len_startword=len(startword)
	between=word[index_start+len_startword:word.find(endword,index_start+len_startword)]
	return between
def maxPage(post_url):
	url = 'http://www.watthakhanun.com/webboard/showthread.php?t='+str(post_url)
	resp = urllib.request.urlopen(urllib.request.Request(url))
	respData = str(resp.read(30000))
	maxpage=cutBetween(r"\xa8\xd2\xa1\xb7\xd1\xe9\xa7\xcb\xc1\xb4 ",r" ",respData)#str
	return maxpage
print("page max : ",maxPage(5112))


post_url=5112
page_url=maxPage(post_url)
# page_url=2
# url = 'http://www.watthakhanun.com/webboard/showthread.php?t=4969'
url = 'http://www.watthakhanun.com/webboard/showthread.php?t='+str(post_url)+'&page='+str(page_url)
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = str(resp.read())
print("curent page :",page_url)

# indexPost=respData.find(r'\xa8\xd2\xa1\xb7\xd1\xe9\xa7\xcb\xc1\xb4')
# # postnow=respData[indexPost+8:respData.find('"',indexPost+10)]
# print(indexPost)



# indexPost=respData.find\xc3\xe8\xc7\xc1\xba\xd8\xad\xa1\xb0\xd4\xb9\xbb\xc5\xb4\xcb\xb9\xd5\xe9('post_message_170020')
# postnow=respData[indexPost+8:respData.find('"',indexPost+10)]
# print(respData[indexPost:indexPost+350])


index_wattu=respData.find('<font size="6"><font color="DarkGreen">')#respData.find(r'\xc3\xd2\xc2\xa1\xd2\xc3\xc7\xd1\xb5\xb6\xd8\xc1\xa7\xa4\xc5 \xc3\xe8\xc7\xc1\xba\xd8\xad\xa1\xb0\xd4\xb9\xbb\xc5\xb4\xcb\xb9\xd5\xe9')
if index_wattu > 0 :
	print("index_wattu",index_wattu)
	post_this=cutBetween("post_message_",'"',respData,index_wattu-100,index_wattu)
	print("id post this : ",post_this)
	file = open('notes.txt','r+')
	post_file=file.read()
	if post_file == post_this:
		print("dup post")
		print("exit")
	else:
		print("new post")
		print("send msg")
		a = open('notes.txt','w')
		a.write(str(post_this))

# a = open('notes.txt','w')


def findnalek(page,startsearch=0):

	url2 = url+'&page='+str(page)
	# url = 'http://www.watthakhanun.com/webboard/showthread.php?t=5112&page=2'
	req2 = urllib.request.Request(url2)
	resp2 = urllib.request.urlopen(req2)
	respData2 = resp2.read()
	respData2=str(respData2)
	p=respData2.find('u=220',startsearch)
	return p
	# print(p)
	# if p>-1:
	# 	# print("Find Na Lek")
	# 	return True
	# else:
	# 	# print("Not Found Na Lek")
	# 	return False


# # print(findnalek(maxpage))
# a = open('notes.txt','r+')
# file=a.read()
# print (file)
# post=file[file.find("post=[")+6:file.find("]")].split(",")
# # print(post[1])
# if post:#list empty
# 	indexNalek=findnalek(maxpage)
# else:
# 	findnalek(maxpage,post[-1])