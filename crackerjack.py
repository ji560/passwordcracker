#!/usr/bin/python
import crypt
import csv

with open('hash.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=':')
    for row in readCSV:
    	somehash = row[1]
with open('hash.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='$')
    for row in readCSV:
	somesalt = "$" + row[1]
	somesalt += "$" + row[2]
for entry in open("/home/jose/passwdlists/rockyou.txt") :
	entry = entry.rstrip("\n")
	curhash = crypt.crypt(entry, somesalt)
	if curhash == somehash :
		print "Hey Boss., I think I found your password\nANSWER: " + entry + " HASH: " + curhash
		break
	print "PASSWORD: " + entry + " HASH: " + curhash
