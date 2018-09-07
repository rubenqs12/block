#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ---------------------------------------------------------
# ---------------------------------------------------------
# Energized - ad.porn.malware blocking.
# A merged collection of hosts from reputable sources.
# https://nayemador.com/energized
# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license
# ---------------------------------------------------------
# ---------------------------------------------------------

import urllib.request
import datetime
import os
import time

File = 'formats/ext-porn-hosts'
List = []
# Thanks to all maintainers of hosts lists.
print('[+] Energized Porn Extension - Building...')
Sources = [
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/ador-energized-porn.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/clefspeare-pornhosts.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/easylist-adult-adservers.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/easylist-adult-specific.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/easylist-adult-thirdparty.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/pornaway.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/porn-top1million.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/sinfonietta-porn.txt'
]

for Link in Sources:
	try:
		print('[+] Retrieving list from: {}'.format(Link))
		r = urllib.request.urlopen(Link)
		Host = r.readlines()
		Host = [x.decode('UTF-8') for x in Host]
		Host = [x.strip() for x in Host]
		Host = [z for z in Host if z != '' and z[0] != '#']
		Host = [h.split()[1] for h in Host if h.split()[0] in ['0.0.0.0', '127.0.0.1']]
		Host = [x for x in Host if x not in ['localhost', 'localhost.localdomain', 'locals']]
		print('[+] Found {} domains to block.'.format(str(len(Host))))
		r.close()
		List += Host
	except:
		print('[-] ERROR: I can\'t retrieve the list from: {}'.format(Link))

print('[+] Removing duplicates and sorting...')
List = sorted(list(set(List)))
print('[+] Applying whitelist...')
r = urllib.request.urlopen('https://raw.githubusercontent.com/AdroitAdorKhan/Energized/master/core/filter/whitelist-porn')
Whitelist = r.readlines()
Whitelist = [x.decode('utf-8') for x in Whitelist]
Whitelist = [x.strip() for x in Whitelist]
Whitelist = [z for z in Whitelist if z != '' and z[0] != '#']
r.close()

for i in range(0, len(Whitelist)):
	try:
		List.remove(Whitelist[i])
	except:
		pass

print('[+] Total domains count {}.'.format(str(len(List))))

# Hosts
if not os.path.exists(os.path.dirname(File)):
	os.makedirs(os.path.dirname(File))

with open(File, 'w') as f:
	print('[+] Writing Hosts file...')
	f.write('''#    _____  _________  _____________  _______\n#   / __/ |/ / __/ _ \/ ___/  _/_  / / __/ _ \ \n#  / _// ,  / _// , _/ (_ // /  / /_/ _// // /\n# /___/_/|_/___/_/|_|\___/___/ /___/___/____/\n#\n#    P   R   O   T   E   C   T   I   O   N\n# -------------------------------------------\n#          ad.porn.malware blocking.\n#                   ------\n#      Merged collection of hosts from\n#             reputable sources.\n# -------------------------------------------\n#          nayemador.com/energized/\n#    github.com/EnergizedProtection/block\n# -------------------------------------------\n\n#        Let's make an annoyance free\n#      better open internet. Altogether.\n#                  ------\n\n''')
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Porn Lite Extension\n# Format: hosts\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: EXP0R9-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/extensions/formats/ext-porn-hosts\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# L O C A L  H O S T\n# -------------------------------------------\n127.0.0.1 localhost\n127.0.0.1 localhost.localdomain\n127.0.0.1 local\n255.255.255.255 broadcasthost\n::1 localhost\n::1 ip6-localhost\n::1 ip6-loopback\nfe80::1%lo0 localhost\nff00::0 ip6-localnet\nff00::0 ip6-mcastprefix\nff02::1 ip6-allnodes\nff02::2 ip6-allrouters\nff02::3 ip6-allhosts\n0.0.0.0 0.0.0.0\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# F E A T U R E S\n# -------------------------------------------\n# _hosts based: based on Hosts file.\n# _any device: compatible with all devices.\n# _blockings: strictly blocks web annoyances.\n# _formats: most used formats.\n# _speed: reduces page loading time.\n# _privacy: increases privacy.\n# _saves expense: decreases data consumption.\n# _clean: no extra abracadabra!\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# T E A M  B O L T Z - meet the team\n# -------------------------------------------\n# @AdroitAdorKhan - Head Developer & Maintainer\n# @AvinashReddy3108 - Developer\n# @badmojr - Maintainer\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# E N E R G I Z E D  B E G I N S\n# -------------------------------------------\n\n''')
	f.write('\n'.join('0.0.0.0 ' + url for url in List))
	f.write('''\n\n# -------------------------------------------\n# E N E R G I Z E D  E N D S\n# -------------------------------------------\n\n#               Stay Energized!\n#                   ------''')
	print('[+] Done!')