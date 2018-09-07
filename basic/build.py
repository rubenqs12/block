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

File = 'formats/hosts'
Hostsv6 = 'formats/hosts-ipv6.txt'
Text = 'formats/hosts.txt'
Domains = 'formats/domains.txt'
Filter = 'formats/filter'
Masq = 'formats/dnsmasq.conf'
Ipv6 = 'formats/dnsmasq-ipv6.conf'
Unbound = 'formats/unbound.conf'
Rpz = 'formats/rpz.txt'
List = []
# Thanks to all maintainers of hosts lists.
print('[+] Energized Basic and Formats - Building...')
Sources = [
	'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/1hosts.cf.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/280blocker.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/adaway.org.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/ador-energized.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/adblock-nocoin-list.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/adguard-dns.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/adguard-domains.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/adguard-safari.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/adguard-spyware.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/airelle-rsk.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/antipopads.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/anudeep-adservers.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/better-fyi-trackers.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/ck-ad-tracker.txt',
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
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/hexxium-creations-threat-list.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/hosts-file.net-ats.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/hosts-file.net-emd.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/kadhosts.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/lightswitch-hosts-extended.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/malwaredomains.com-immortaldomains.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/malwaredomains.com-justdomains.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/moaab.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/mobile-ad-trackers.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/molinero-hblock.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/neohost.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/notracking.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/pgl.yoyo.org.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/someonewhocares.org.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/spam404.com-adblocklist.txt',
  'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/active/filter/sbc.txt',
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
r = urllib.request.urlopen('https://raw.githubusercontent.com/AdroitAdorKhan/Energized/master/core/filter/whitelist')
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
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Basic Protection\n# Format: hosts\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: E84S1C-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/basic/formats/hosts\n# Mirror: https://nayemador.com/energized/basic\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# L O C A L  H O S T\n# -------------------------------------------\n127.0.0.1 localhost\n127.0.0.1 localhost.localdomain\n127.0.0.1 local\n255.255.255.255 broadcasthost\n::1 localhost\n::1 ip6-localhost\n::1 ip6-loopback\nfe80::1%lo0 localhost\nff00::0 ip6-localnet\nff00::0 ip6-mcastprefix\nff02::1 ip6-allnodes\nff02::2 ip6-allrouters\nff02::3 ip6-allhosts\n0.0.0.0 0.0.0.0\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# F E A T U R E S\n# -------------------------------------------\n# _hosts based: based on Hosts file.\n# _any device: compatible with all devices.\n# _blockings: strictly blocks web annoyances.\n# _formats: most used formats.\n# _speed: reduces page loading time.\n# _privacy: increases privacy.\n# _saves expense: decreases data consumption.\n# _clean: no extra abracadabra!\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# T E A M  B O L T Z - meet the team\n# -------------------------------------------\n# @AdroitAdorKhan - Head Developer & Maintainer\n# @AvinashReddy3108 - Developer\n# @badmojr - Maintainer\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# E N E R G I Z E D  B E G I N S\n# -------------------------------------------\n\n''')
	f.write('\n'.join('0.0.0.0 ' + url for url in List))
	f.write('''\n\n# -------------------------------------------\n# E N E R G I Z E D  E N D S\n# -------------------------------------------\n\n#               Stay Energized!\n#                   ------''')
	print('[+] Done!')
  
# Hosts IPV6
if not os.path.exists(os.path.dirname(Hostsv6)):
	os.makedirs(os.path.dirname(Hostsv6))

with open(Hostsv6, 'w') as f:
	print('[+] Writing Hosts IPV6 file...')
	f.write('''#    _____  _________  _____________  _______\n#   / __/ |/ / __/ _ \/ ___/  _/_  / / __/ _ \ \n#  / _// ,  / _// , _/ (_ // /  / /_/ _// // /\n# /___/_/|_/___/_/|_|\___/___/ /___/___/____/\n#\n#    P   R   O   T   E   C   T   I   O   N\n# -------------------------------------------\n#          ad.porn.malware blocking.\n#                   ------\n#      Merged collection of hosts from\n#             reputable sources.\n# -------------------------------------------\n#          nayemador.com/energized/\n#    github.com/EnergizedProtection/block\n# -------------------------------------------\n\n#        Let's make an annoyance free\n#      better open internet. Altogether.\n#                  ------\n\n''')
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Basic Protection\n# Format: hosts ipv6\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: E84S1C-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/basic/formats/hosts-ipv6.txt\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# L O C A L  H O S T\n# -------------------------------------------\n127.0.0.1 localhost\n127.0.0.1 localhost.localdomain\n127.0.0.1 local\n255.255.255.255 broadcasthost\n::1 localhost\n::1 ip6-localhost\n::1 ip6-loopback\nfe80::1%lo0 localhost\nff00::0 ip6-localnet\nff00::0 ip6-mcastprefix\nff02::1 ip6-allnodes\nff02::2 ip6-allrouters\nff02::3 ip6-allhosts\n0.0.0.0 0.0.0.0\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# F E A T U R E S\n# -------------------------------------------\n# _hosts based: based on Hosts file.\n# _any device: compatible with all devices.\n# _blockings: strictly blocks web annoyances.\n# _formats: most used formats.\n# _speed: reduces page loading time.\n# _privacy: increases privacy.\n# _saves expense: decreases data consumption.\n# _clean: no extra abracadabra!\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# T E A M  B O L T Z - meet the team\n# -------------------------------------------\n# @AdroitAdorKhan - Head Developer & Maintainer\n# @AvinashReddy3108 - Developer\n# @badmojr - Maintainer\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# E N E R G I Z E D  B E G I N S\n# -------------------------------------------\n\n''')
	f.write('\n'.join(':: ' + url for url in List))
	f.write('''\n\n# -------------------------------------------\n# E N E R G I Z E D  E N D S\n# -------------------------------------------\n\n#               Stay Energized!\n#                   ------''')
	print('[+] Done!')

# Hosts.txt
if not os.path.exists(os.path.dirname(Text)):
	os.makedirs(os.path.dirname(Text))

with open(Text, 'w') as f:
	print('[+] Writing Hosts.txt file...')
	f.write('''#    _____  _________  _____________  _______\n#   / __/ |/ / __/ _ \/ ___/  _/_  / / __/ _ \ \n#  / _// ,  / _// , _/ (_ // /  / /_/ _// // /\n# /___/_/|_/___/_/|_|\___/___/ /___/___/____/\n#\n#    P   R   O   T   E   C   T   I   O   N\n# -------------------------------------------\n#          ad.porn.malware blocking.\n#                   ------\n#      Merged collection of hosts from\n#             reputable sources.\n# -------------------------------------------\n#          nayemador.com/energized/\n#    github.com/EnergizedProtection/block\n# -------------------------------------------\n\n#        Let's make an annoyance free\n#      better open internet. Altogether.\n#                  ------\n\n''')
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Basic Protection\n# Format: hosts\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: E84S1C-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/basic/formats/hosts.txt\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# L O C A L  H O S T\n# -------------------------------------------\n127.0.0.1 localhost\n127.0.0.1 localhost.localdomain\n127.0.0.1 local\n255.255.255.255 broadcasthost\n::1 localhost\n::1 ip6-localhost\n::1 ip6-loopback\nfe80::1%lo0 localhost\nff00::0 ip6-localnet\nff00::0 ip6-mcastprefix\nff02::1 ip6-allnodes\nff02::2 ip6-allrouters\nff02::3 ip6-allhosts\n0.0.0.0 0.0.0.0\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# F E A T U R E S\n# -------------------------------------------\n# _hosts based: based on Hosts file.\n# _any device: compatible with all devices.\n# _blockings: strictly blocks web annoyances.\n# _formats: most used formats.\n# _speed: reduces page loading time.\n# _privacy: increases privacy.\n# _saves expense: decreases data consumption.\n# _clean: no extra abracadabra!\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# T E A M  B O L T Z - meet the team\n# -------------------------------------------\n# @AdroitAdorKhan - Head Developer & Maintainer\n# @AvinashReddy3108 - Developer\n# @badmojr - Maintainer\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# E N E R G I Z E D  B E G I N S\n# -------------------------------------------\n\n''')
	f.write('\n'.join('0.0.0.0 ' + url for url in List))
	f.write('''\n\n# -------------------------------------------\n# E N E R G I Z E D  E N D S\n# -------------------------------------------\n\n#               Stay Energized!\n#                   ------''')
	print('[+] Done!')

# Filter
if not os.path.exists(os.path.dirname(Filter)):
	os.makedirs(os.path.dirname(Filter))

with open(Filter, 'w') as f:
	print('[+] Writing Filter file...')
	f.write('''!    _____  _________  _____________  _______\n!   / __/ |/ / __/ _ \/ ___/  _/_  / / __/ _ \ \n!  / _// ,  / _// , _/ (_ // /  / /_/ _// // /\n! /___/_/|_/___/_/|_|\___/___/ /___/___/____/\n!\n!    P   R   O   T   E   C   T   I   O   N\n! -------------------------------------------\n!          ad.porn.malware blocking.\n!                   ------\n!      Merged collection of hosts from\n!             reputable sources.\n! -------------------------------------------\n!          nayemador.com/energized/\n!    github.com/EnergizedProtection/block\n! -------------------------------------------\n\n!        Let's make an annoyance free\n!      better open internet. Altogether.\n!                  ------\n\n''')
	f.write('''! -------------------------------------------\n! P A C K  D E T A I L S\n! -------------------------------------------\n! Title: Energized Basic Protection\n! Format: filter\n! Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n! Release: ''' + time.strftime("%j", time.gmtime()) + '''\n! Entries: {}'''.format(str(len(List))) + '''\n! Pack Code: E84S1C-P\n! License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n! Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n! RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/basic/formats/filter\n! -------------------------------------------\n\n''')
	f.write('''! -------------------------------------------\n! F E A T U R E S\n! -------------------------------------------\n! _hosts based: based on Hosts file.\n! _any device: compatible with all devices.\n! _blockings: strictly blocks web annoyances.\n! _formats: most used formats.\n! _speed: reduces page loading time.\n! _privacy: increases privacy.\n! _saves expense: decreases data consumption.\n! _clean: no extra abracadabra!\n! -------------------------------------------\n''')
	f.write('''\n! -------------------------------------------\n! T E A M  B O L T Z - meet the team\n! -------------------------------------------\n! @AdroitAdorKhan - Head Developer & Maintainer\n! @AvinashReddy3108 - Developer\n! @badmojr - Maintainer\n! -------------------------------------------\n\n''')
	f.write('''! -------------------------------------------\n! E N E R G I Z E D  B E G I N S\n! -------------------------------------------\n\n''')
	f.write('\n'.join('||' + url for url in List))
	f.write('''\n\n! -------------------------------------------\n! E N E R G I Z E D  E N D S\n! -------------------------------------------\n\n!               Stay Energized!\n!                   ------''')
	print('[+] Done!')

# Domain List
if not os.path.exists(os.path.dirname(Domains)):
	os.makedirs(os.path.dirname(Domains))

with open(Domains, 'w') as f:
	print('[+] Writing Domain List file...')
	f.write('''#    _____  _________  _____________  _______\n#   / __/ |/ / __/ _ \/ ___/  _/_  / / __/ _ \ \n#  / _// ,  / _// , _/ (_ // /  / /_/ _// // /\n# /___/_/|_/___/_/|_|\___/___/ /___/___/____/\n#\n#    P   R   O   T   E   C   T   I   O   N\n# -------------------------------------------\n#          ad.porn.malware blocking.\n#                   ------\n#      Merged collection of hosts from\n#             reputable sources.\n# -------------------------------------------\n#          nayemador.com/energized/\n#    github.com/EnergizedProtection/block\n# -------------------------------------------\n\n#        Let's make an annoyance free\n#      better open internet. Altogether.\n#                  ------\n\n''')
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Basic Protection\n# Format: domain list\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: E84S1C-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/basic/formats/domains.txt\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# F E A T U R E S\n# -------------------------------------------\n# _hosts based: based on Hosts file.\n# _any device: compatible with all devices.\n# _blockings: strictly blocks web annoyances.\n# _formats: most used formats.\n# _speed: reduces page loading time.\n# _privacy: increases privacy.\n# _saves expense: decreases data consumption.\n# _clean: no extra abracadabra!\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# T E A M  B O L T Z - meet the team\n# -------------------------------------------\n# @AdroitAdorKhan - Head Developer & Maintainer\n# @AvinashReddy3108 - Developer\n# @badmojr - Maintainer\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# E N E R G I Z E D  B E G I N S\n# -------------------------------------------\n\n''')
	f.write('\n'.join(url for url in List))
	f.write('''\n\n# -------------------------------------------\n# E N E R G I Z E D  E N D S\n# -------------------------------------------\n\n#               Stay Energized!\n#                   ------''')
	print('[+] Done!')

# DNSMasq
if not os.path.exists(os.path.dirname(Masq)):
	os.makedirs(os.path.dirname(Masq))

with open(Masq, 'w') as f:
	print('[+] Writing DNSMasq file...')
	f.write('''#    _____  _________  _____________  _______\n#   / __/ |/ / __/ _ \/ ___/  _/_  / / __/ _ \ \n#  / _// ,  / _// , _/ (_ // /  / /_/ _// // /\n# /___/_/|_/___/_/|_|\___/___/ /___/___/____/\n#\n#    P   R   O   T   E   C   T   I   O   N\n# -------------------------------------------\n#          ad.porn.malware blocking.\n#                   ------\n#      Merged collection of hosts from\n#             reputable sources.\n# -------------------------------------------\n#          nayemador.com/energized/\n#    github.com/EnergizedProtection/block\n# -------------------------------------------\n\n#        Let's make an annoyance free\n#      better open internet. Altogether.\n#                  ------\n\n''')
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Basic Protection\n# Format: dnsmasq\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: E84S1C-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/basic/formats/dnsmasq.conf\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# F E A T U R E S\n# -------------------------------------------\n# _hosts based: based on Hosts file.\n# _any device: compatible with all devices.\n# _blockings: strictly blocks web annoyances.\n# _formats: most used formats.\n# _speed: reduces page loading time.\n# _privacy: increases privacy.\n# _saves expense: decreases data consumption.\n# _clean: no extra abracadabra!\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# T E A M  B O L T Z - meet the team\n# -------------------------------------------\n# @AdroitAdorKhan - Head Developer & Maintainer\n# @AvinashReddy3108 - Developer\n# @badmojr - Maintainer\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# E N E R G I Z E D  B E G I N S\n# -------------------------------------------\n\n''')
	f.write('\n'.join('address=/' + url + '/0.0.0.0/' for url in List))
	f.write('''\n\n# -------------------------------------------\n# E N E R G I Z E D  E N D S\n# -------------------------------------------\n\n#               Stay Energized!\n#                   ------''')
	print('[+] Done!')

# DNSMasq IPV6
if not os.path.exists(os.path.dirname(Ipv6)):
	os.makedirs(os.path.dirname(Ipv6))

with open(Ipv6, 'w') as f:
	print('[+] Writing DNSMasq IPV6 file...')
	f.write('''#    _____  _________  _____________  _______\n#   / __/ |/ / __/ _ \/ ___/  _/_  / / __/ _ \ \n#  / _// ,  / _// , _/ (_ // /  / /_/ _// // /\n# /___/_/|_/___/_/|_|\___/___/ /___/___/____/\n#\n#    P   R   O   T   E   C   T   I   O   N\n# -------------------------------------------\n#          ad.porn.malware blocking.\n#                   ------\n#      Merged collection of hosts from\n#             reputable sources.\n# -------------------------------------------\n#          nayemador.com/energized/\n#    github.com/EnergizedProtection/block\n# -------------------------------------------\n\n#        Let's make an annoyance free\n#      better open internet. Altogether.\n#                  ------\n\n''')
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Basic Protection\n# Format: dnsmasq ipv6\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: E84S1C-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/basic/formats/dnsmasq-ipv6.conf\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# F E A T U R E S\n# -------------------------------------------\n# _hosts based: based on Hosts file.\n# _any device: compatible with all devices.\n# _blockings: strictly blocks web annoyances.\n# _formats: most used formats.\n# _speed: reduces page loading time.\n# _privacy: increases privacy.\n# _saves expense: decreases data consumption.\n# _clean: no extra abracadabra!\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# T E A M  B O L T Z - meet the team\n# -------------------------------------------\n# @AdroitAdorKhan - Head Developer & Maintainer\n# @AvinashReddy3108 - Developer\n# @badmojr - Maintainer\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# E N E R G I Z E D  B E G I N S\n# -------------------------------------------\n\n''')
	f.write('\n'.join('address=/' + url + '/::1/' for url in List))
	f.write('''\n\n# -------------------------------------------\n# E N E R G I Z E D  E N D S\n# -------------------------------------------\n\n#               Stay Energized!\n#                   ------''')
	print('[+] Done!')

# Unbound
if not os.path.exists(os.path.dirname(Unbound)):
	os.makedirs(os.path.dirname(Unbound))

with open(Unbound, 'w') as f:
	print('[+] Writing Unbound file...')
	f.write('''#    _____  _________  _____________  _______\n#   / __/ |/ / __/ _ \/ ___/  _/_  / / __/ _ \ \n#  / _// ,  / _// , _/ (_ // /  / /_/ _// // /\n# /___/_/|_/___/_/|_|\___/___/ /___/___/____/\n#\n#    P   R   O   T   E   C   T   I   O   N\n# -------------------------------------------\n#          ad.porn.malware blocking.\n#                   ------\n#      Merged collection of hosts from\n#             reputable sources.\n# -------------------------------------------\n#          nayemador.com/energized/\n#    github.com/EnergizedProtection/block\n# -------------------------------------------\n\n#        Let's make an annoyance free\n#      better open internet. Altogether.\n#                  ------\n\n''')
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Basic Protection\n# Format: unbound\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: E84S1C-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/basic/formats/unbound.conf\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# F E A T U R E S\n# -------------------------------------------\n# _hosts based: based on Hosts file.\n# _any device: compatible with all devices.\n# _blockings: strictly blocks web annoyances.\n# _formats: most used formats.\n# _speed: reduces page loading time.\n# _privacy: increases privacy.\n# _saves expense: decreases data consumption.\n# _clean: no extra abracadabra!\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# T E A M  B O L T Z - meet the team\n# -------------------------------------------\n# @AdroitAdorKhan - Head Developer & Maintainer\n# @AvinashReddy3108 - Developer\n# @badmojr - Maintainer\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# E N E R G I Z E D  B E G I N S\n# -------------------------------------------\n\n''')
	f.write('\n'.join('local-zone: "' + url + '" redirect\nlocal-data: "' + url + ' A 0.0.0.0"' for url in List))
	f.write('''\n\n# -------------------------------------------\n# E N E R G I Z E D  E N D S\n# -------------------------------------------\n\n#               Stay Energized!\n#                   ------''')
	print('[+] Done!')

# RPZ
if not os.path.exists(os.path.dirname(Rpz)):
	os.makedirs(os.path.dirname(Rpz))

with open(Rpz, 'w') as f:
	print('[+] Writing RPZ file...')
	f.write('''#    _____  _________  _____________  _______\n#   / __/ |/ / __/ _ \/ ___/  _/_  / / __/ _ \ \n#  / _// ,  / _// , _/ (_ // /  / /_/ _// // /\n# /___/_/|_/___/_/|_|\___/___/ /___/___/____/\n#\n#    P   R   O   T   E   C   T   I   O   N\n# -------------------------------------------\n#          ad.porn.malware blocking.\n#                   ------\n#      Merged collection of hosts from\n#             reputable sources.\n# -------------------------------------------\n#          nayemador.com/energized/\n#    github.com/EnergizedProtection/block\n# -------------------------------------------\n\n#        Let's make an annoyance free\n#      better open internet. Altogether.\n#                  ------\n\n''')
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Basic Protection\n# Format: rpz\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: E84S1C-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/basic/formats/rpz.txt\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# F E A T U R E S\n# -------------------------------------------\n# _hosts based: based on Hosts file.\n# _any device: compatible with all devices.\n# _blockings: strictly blocks web annoyances.\n# _formats: most used formats.\n# _speed: reduces page loading time.\n# _privacy: increases privacy.\n# _saves expense: decreases data consumption.\n# _clean: no extra abracadabra!\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# R P Z\n# -------------------------------------------\n$TTL 2h\n@ IN SOA localhost. root.localhost. (1 6h 1h 1w 2h)\n  IN NS  localhost.\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# T E A M  B O L T Z - meet the team\n# -------------------------------------------\n# @AdroitAdorKhan - Head Developer & Maintainer\n# @AvinashReddy3108 - Developer\n# @badmojr - Maintainer\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# E N E R G I Z E D  B E G I N S\n# -------------------------------------------\n\n''')
	f.write('\n'.join(url + ' CNAME .' for url in List))
	f.write('''\n\n# -------------------------------------------\n# E N E R G I Z E D  E N D S\n# -------------------------------------------\n\n#               Stay Energized!\n#                   ------''')
	print('[+] Done!')