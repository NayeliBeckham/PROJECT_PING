#! /usr/bin python2.7

import subprocess
import time
import os


def mainProcess():

	try:
		os.system("clear")
		isWorking = True
		GimmeIP = raw_input("Enter a valid IP address: ")

		while(isWorking):
			process1 = subprocess.Popen("ping -q -c 1 %s"%GimmeIP, stdout = subprocess.PIPE, shell = True).stdout.read()
			process2 = process1.split()
			process3 = len(process2)

			#PingTo
			if process3 == 27:
				os.system("clear")
				#1
				print("[Ping to %s]"%GimmeIP)
				print("Sending ping.")
				time.sleep(1)
				os.system("clear")
				#2
				print("[Ping to %s]"%GimmeIP)
				print("Sending ping..")
				time.sleep(1)
				os.system("clear")
				#3
				print("[Ping to %s]"%GimmeIP)
				print("Sending ping...")
				###############NoAddThis###############
				print("\n############################################################")
				print process1
				print("############################################################")
				###############NoAddThis###############
				time.sleep(1)

			#ShowHostErrorUnavailable
			if process3 == 24:
				os.system("clear")
				print("[.....ERROR.....]")
				print("Host unavailable")
				time.sleep(3)
				return mainProcess()

			#ShowHostErrorUnknown
			if process3 == 22:
				os.system("clear")
				print("[.....ERROR.....]")
				print("Host unknown")
				time.sleep(3)
				return mainProcess()

			#SHowConnectionRefused
			if process3 == 0:
				os.system("clear")
				print("[.....FATAL ERROR.....]")
				print("Connection refused, try again")
				time.sleep(3)
				return mainProcess()


	except KeyboardInterrupt:
		os.system("clear")
		#1
		print("[Exiting.]")
		time.sleep(1)
		os.system("clear")
		#2
		print("[Exiting..]")
		time.sleep(1)
		os.system("clear")
		#3
		print("[Exiting...]")
		time.sleep(1)
		os.system("clear")

mainProcess()