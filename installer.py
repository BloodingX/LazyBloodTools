#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
import time, os, sys

print '\033[94m'"  _         _        _ _         "
print '\033[94m'" (_)_ _  __| |_ __ _| | |___ _ _ "
print '\033[94m'" | | ' \(_-<  _/ _` | | / -_) '_|"
print '\033[94m'" |_|_||_/__/\__\__,_|_|_\___|_|  "
print '\033[94m\033[1m'"                of LazyBLoodTools"   

print ("")
print ("")
print ("")

ques = input ("Do you wanna install the tools used in the LazyBloodTool ? 1=yes , 2=no : ")
if ques == 1:
	print'\033[0m''\033[94m'"Installing hping3 ..."
	time.sleep(2)
	os.system("apt-get install hping3")
	time.sleep(2)
	os.system("apt-get update")
	print ("")
	print ("")
	print ("")
	print ("-------")
	print ("-done!-")
	print ("-------")
	print ("")
	print ("")
	print ("info----------->tape in the folder /LazyBloodTools/ (sudo python Tools.py) to start the tools bye.")
	exit()
if ques == 2:
	print'\033[0m''\033[94m'"ok."
	time.sleep(2)
	exit()

else:
	print'\033[1m''\033[92m'"Error quit the installer"
	exit()
    
