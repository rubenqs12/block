#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Energized - Magisk Prop Creator

import urllib.request
import datetime
import os
import time

version='../VERSION.md'

if not os.path.exists(os.path.dirname(version)):
	os.makedirs(os.path.dirname(version))

with open(version, 'w') as f:
	print('[+] Versioning...')
	print('[+] Writing to file...')
	f.write('''Name=Energized Protection''')
	f.write('''\nVersion: 1.''' + time.strftime("%m.%j", time.gmtime()) + '''''')
	f.write('''\nVersion Code=''' + time.strftime("%j", time.gmtime()) + '''''')
	f.write('''\nAuthor=Team Boltz''')
	f.write('''\nDescription=ad.porn.malware blocking.''')
	f.write('''\nllLicense: MIT''')
	print('[+] Done!')