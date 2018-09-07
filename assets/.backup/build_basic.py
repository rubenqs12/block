#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ---------------------------------------------------------
# ---------------------------------------------------------
# Energized - ad.porn.malware blocking.
# A merged collection of hosts from reputable sources.
# https://nayemador.com/energized
# License: MIT, https://opensource.org/licenses/MIT       
# ---------------------------------------------------------
# ---------------------------------------------------------

import urllib.request
import datetime
import os
import time

File = 'formats/hosts'
List = []
# Thanks to all maintainers of hosts lists.
print('[+] Energized - Building...')
Sources = [
	'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/1hosts.cf.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/adaway.org.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/adzhosts.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/ador-energized.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/adblock-nocoin-list.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/adguard-dns.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/adguard-spyware.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/airelle-rsk.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/antipopads.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/ck-ad-tracker.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/ck-web-rtc.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/disconnect.me-ad.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/disconnect.me-malware.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/dshield.org-low.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/easylist.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/easylist-adservers.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/easyprivacy.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/fademind-add.2o7net.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/fademind-add.dead.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/fademind-add.risk.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/fademind-add.spam.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/hosts-file.net-ats.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/hosts-file.net-emd.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/hosts-file.net-wrz.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/kadhosts.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/lightswitch-hosts-extended.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/malwaredomains.com-immortaldomains.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/malwaredomains.com-justdomains.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/moaab.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/molinero-hblock.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/neohost.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/notracking.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/nsa-blocklist.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/pgl.yoyo.org.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/someonewhocares.org.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/spam404.com-adblocklist.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/sbc.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/sbc-fakenews-gambling.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/streaming-ads.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/unchecky-ads.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/vokins-yhosts.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/windows-spy-blocker.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/winhelp2002.mvps.org.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/zerodot1-coinblockerlists.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/zeustracker.abuse.ch.txt'
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
r = urllib.request.urlopen('https://raw.githubusercontent.com/AdroitAdorKhan/Energized/master/EnergizedHosts/EnergizedWhites')
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

if not os.path.exists(os.path.dirname(File)):
	os.makedirs(os.path.dirname(File))

with open(File, 'w') as f:
	print('[+] Writing to file...')
	f.write('''# Energized - ad.porn.malware blocking.\n# A merged collection of hosts from reputable sources.\n# https://nayemador.com/energized\n\n# Energized Basic Protection\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Project Git: https://github.com/EnergizedProtection/block\n# Source: https://nayemador.com/energized/basic\n# RAW Source: https://raw.githubusercontent.com/EnergizedProtection/block/master/basic/formats/hosts\n# Last updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# Total Domains: {}\n\n'''.format(str(len(List))))
	f.write('''\n# -===============-Team Boltz-================-\n# @adroitadorkhan | @badmojr | @AvinashReddy3108\n# Telegram - https://t.me/EnergizedProtection\n# Email - mail.energized@protonmail.com\n# -=========================================-\n\n''')
	f.write('''\n127.0.0.1 localhost\n127.0.0.1 localhost.localdomain\n127.0.0.1 local\n255.255.255.255 broadcasthost\n::1 localhost\n::1 ip6-localhost\n::1 ip6-loopback\nfe80::1%lo0 localhost\nff00::0 ip6-localnet\nff00::0 ip6-mcastprefix\nff02::1 ip6-allnodes\nff02::2 ip6-allrouters\nff02::3 ip6-allhosts\n0.0.0.0 0.0.0.0\n\n\n# -====================-Features-====================-\n#\n# - Based on Hosts file, all the bad stuff blocked with 0.0.0.0 \n# - Compatible with all devices, regardless of OS. \n# - Strictly blocks all advertisements, malwares, spams, statistics, trackers on both web browsing and applications. \n# - YouTube, Spotify, UC and Shareit Ads Blocking. \n# - Reduces page loading time. \n# - Reduces data consumption. Saves data expense. \n# - Increases privacy. \n# - No extra abracadabra!\n#\n# -==================================================-\n\n\n''')
	f.write('''\n# Energized Protection Starts\n''')
	f.write('\n'.join('0.0.0.0 ' + url for url in List))
	f.write('''\n# Energized Protection Ends.\n# Pack Code: E84S1C-P\n# Stay Energized Mate!''')
	print('[+] Done!')