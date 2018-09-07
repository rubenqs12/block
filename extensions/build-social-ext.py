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

File = 'formats/ext-social-hosts'
Hostsv6 = 'formats/ext-social-hosts-ipv6.txt'
Domains = 'formats/ext-social-domains.txt'
Filter = 'formats/ext-social-filter'
Masq = 'formats/ext-social-dnsmasq.conf'
Ipv6 = 'formats/ext-social-dnsmasq-ipv6.conf'
Unbound = 'formats/ext-social-unbound.conf'
Rpz = 'formats/ext-social-rpz.txt'
List = []
# Thanks to all maintainers of hosts lists.
print('[+] Energized Social Extension - Building...')
Sources = [
    'https://raw.githubusercontent.com/Sinfonietta/hostfiles/master/social-hosts',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/converter/filter/adguard-social-filter.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/converter/filter/adguard-social-popups.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/converter/filter/adguard-social-trackers.txt',
    'https://raw.githubusercontent.com/EnergizedProtection/mirror/master/converter/filter/adversity-anti-social.txt',
    'https://raw.githubusercontent.com/AdroitAdorKhan/Energized/master/core/social'
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
r = urllib.request.urlopen('https://raw.githubusercontent.com/AdroitAdorKhan/Energized/master/core/filter/whitelist-extension')
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
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Social Extension\n# Format: hosts\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: EX50C14L-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/extensions/formats/ext-social-hosts\n# Mirror: https://nayemador.com/energized/exts/social\n# -------------------------------------------\n\n''')
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
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Social Extension\n# Format: hosts ipv6\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: EX50C14L-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/extensions/formats/ext-social-hosts-ipv6.txt\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# L O C A L  H O S T\n# -------------------------------------------\n127.0.0.1 localhost\n127.0.0.1 localhost.localdomain\n127.0.0.1 local\n255.255.255.255 broadcasthost\n::1 localhost\n::1 ip6-localhost\n::1 ip6-loopback\nfe80::1%lo0 localhost\nff00::0 ip6-localnet\nff00::0 ip6-mcastprefix\nff02::1 ip6-allnodes\nff02::2 ip6-allrouters\nff02::3 ip6-allhosts\n0.0.0.0 0.0.0.0\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# F E A T U R E S\n# -------------------------------------------\n# _hosts based: based on Hosts file.\n# _any device: compatible with all devices.\n# _blockings: strictly blocks web annoyances.\n# _formats: most used formats.\n# _speed: reduces page loading time.\n# _privacy: increases privacy.\n# _saves expense: decreases data consumption.\n# _clean: no extra abracadabra!\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# T E A M  B O L T Z - meet the team\n# -------------------------------------------\n# @AdroitAdorKhan - Head Developer & Maintainer\n# @AvinashReddy3108 - Developer\n# @badmojr - Maintainer\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# E N E R G I Z E D  B E G I N S\n# -------------------------------------------\n\n''')
	f.write('\n'.join(':: ' + url for url in List))
	f.write('''\n\n# -------------------------------------------\n# E N E R G I Z E D  E N D S\n# -------------------------------------------\n\n#               Stay Energized!\n#                   ------''')
	print('[+] Done!')

# Filter
if not os.path.exists(os.path.dirname(Filter)):
	os.makedirs(os.path.dirname(Filter))

with open(Filter, 'w') as f:
	print('[+] Writing Filter file...')
	f.write('''!    _____  _________  _____________  _______\n!   / __/ |/ / __/ _ \/ ___/  _/_  / / __/ _ \ \n!  / _// ,  / _// , _/ (_ // /  / /_/ _// // /\n! /___/_/|_/___/_/|_|\___/___/ /___/___/____/\n!\n!    P   R   O   T   E   C   T   I   O   N\n! -------------------------------------------\n!          ad.porn.malware blocking.\n!                   ------\n!      Merged collection of hosts from\n!             reputable sources.\n! -------------------------------------------\n!          nayemador.com/energized/\n!    github.com/EnergizedProtection/block\n! -------------------------------------------\n\n!        Let's make an annoyance free\n!      better open internet. Altogether.\n!                  ------\n\n''')
	f.write('''! -------------------------------------------\n! P A C K  D E T A I L S\n! -------------------------------------------\n! Title: Energized Social Extension\n! Format: filter\n! Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n! Release: ''' + time.strftime("%j", time.gmtime()) + '''\n! Entries: {}'''.format(str(len(List))) + '''\n! Pack Code: EX50C14L-P\n! License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n! Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n! RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/extensions/formats/ext-social-filter\n! -------------------------------------------\n\n''')
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
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Social Extension\n# Format: domain list\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: EX50C14L-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/extensions/formats/ext-social-domains.txt\n# -------------------------------------------\n\n''')
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
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Social Extension\n# Format: dnsmasq\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: EX50C14L-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/extensions/formats/ext-social-dnsmasq.conf\n# -------------------------------------------\n\n''')
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
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Social Extension\n# Format: dnsmasq ipv6\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: EX50C14L-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/extensions/formats/ext-social-dnsmasq-ipv6.conf\n# -------------------------------------------\n\n''')
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
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Social Extension\n# Format: unbound\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: EX50C14L-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/extensions/formats/ext-social-unbound.conf\n# -------------------------------------------\n\n''')
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
	f.write('''# -------------------------------------------\n# P A C K  D E T A I L S\n# -------------------------------------------\n# Package: Energized Social Extension\n# Format: rpz\n# Version: ''' + time.strftime("%y.%m.%j", time.gmtime()) + '''\n# Release: ''' + time.strftime("%j", time.gmtime()) + '''\n# Entries: {}'''.format(str(len(List))) + '''\n# Pack Code: EX50C14L-P\n# License: CC BY-NC-SA 4.0, https://nayemador.com/energized/license\n# Updated: {}'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
	f.write('''\n# RAW: https://raw.githubusercontent.com/EnergizedProtection/block/master/extensions/formats/ext-social-rpz.txt\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# F E A T U R E S\n# -------------------------------------------\n# _hosts based: based on Hosts file.\n# _any device: compatible with all devices.\n# _blockings: strictly blocks web annoyances.\n# _formats: most used formats.\n# _speed: reduces page loading time.\n# _privacy: increases privacy.\n# _saves expense: decreases data consumption.\n# _clean: no extra abracadabra!\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# R P Z\n# -------------------------------------------\n$TTL 2h\n@ IN SOA localhost. root.localhost. (1 6h 1h 1w 2h)\n  IN NS  localhost.\n# -------------------------------------------\n''')
	f.write('''\n# -------------------------------------------\n# T E A M  B O L T Z - meet the team\n# -------------------------------------------\n# @AdroitAdorKhan - Head Developer & Maintainer\n# @AvinashReddy3108 - Developer\n# @badmojr - Maintainer\n# -------------------------------------------\n\n''')
	f.write('''# -------------------------------------------\n# E N E R G I Z E D  B E G I N S\n# -------------------------------------------\n\n''')
	f.write('\n'.join(url + ' CNAME .' for url in List))
	f.write('''\n\n# -------------------------------------------\n# E N E R G I Z E D  E N D S\n# -------------------------------------------\n\n#               Stay Energized!\n#                   ------''')
	print('[+] Done!')
