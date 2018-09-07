#!/bin/sh
# Energized - Formats
# Energized TXT, Domains List, DNSMasq, IPV6 DNSMasq, Unbound Conf & RPZ
# Starts

# Variables
# Directory
basic=../basic/formats
blu=../blu/formats
bGo=../bluGo/formats
porn=../porn/formats
ultimate=../ultimate/formats
unified=../unified/formats
# Headers
header=../assets/header/header.txt
rpzheader=../assets/header/rpz-header.txt
# Temp
tmp=../assets
tempConf=../assets

echo "[+] Building Diff Formats"
# TXT
echo "[+] Creating TXT..."
cp $basic/hosts $basic/hosts.txt
cp $blu/hosts $blu/hosts.txt
cp $bGo/hosts $bGo/hosts.txt
cp $porn/hosts $porn/hosts.txt
cp $ultimate/hosts $ultimate/hosts.txt
cp $unified/hosts $unified/hosts.txt

# DNSMasq 
echo "[+] Creating DNSMasq..."
# Basic
cp $basic/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "address=/"$2"/0.0.0.0/"}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > dnsmasq.conf
mv -f dnsmasq.conf $basic/dnsmasq.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Blu
cp $blu/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "address=/"$2"/0.0.0.0/"}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > dnsmasq.conf
mv -f dnsmasq.conf $blu/dnsmasq.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Blu Go
cp $bGo/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "address=/"$2"/0.0.0.0/"}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > dnsmasq.conf
mv -f dnsmasq.conf $bGo/dnsmasq.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Porn
cp $porn/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "address=/"$2"/0.0.0.0/"}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > dnsmasq.conf
mv -f dnsmasq.conf $porn/dnsmasq.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Ultimate
cp $ultimate/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "address=/"$2"/0.0.0.0/"}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > dnsmasq.conf
mv -f dnsmasq.conf $ultimate/dnsmasq.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Unified
cp $unified/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "address=/"$2"/0.0.0.0/"}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > dnsmasq.conf
mv -f dnsmasq.conf $unified/dnsmasq.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# DNSMasq IPV6
echo "[+] Creating DNSMasq IPV6..."
# Basic
cp $basic/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "address=/"$2"/::1/"}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > dnsmasq-ipv6.conf
mv -f dnsmasq-ipv6.conf $basic/dnsmasq-ipv6.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Blu
cp $blu/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "address=/"$2"/::1/"}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > dnsmasq-ipv6.conf
mv -f dnsmasq-ipv6.conf $blu/dnsmasq-ipv6.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Blu Go
cp $bGo/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "address=/"$2"/::1/"}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > dnsmasq-ipv6.conf
mv -f dnsmasq-ipv6.conf $bGo/dnsmasq-ipv6.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Porn
cp $porn/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "address=/"$2"/::1/"}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > dnsmasq-ipv6.conf
mv -f dnsmasq-ipv6.conf $porn/dnsmasq-ipv6.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Ultimate
cp $ultimate/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "address=/"$2"/::1/"}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > dnsmasq-ipv6.conf
mv -f dnsmasq-ipv6.conf $ultimate/dnsmasq-ipv6.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Unified
cp $unified/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "address=/"$2"/::1/"}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > dnsmasq-ipv6.conf
mv -f dnsmasq-ipv6.conf $unified/dnsmasq-ipv6.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Unbound
echo "[+] Creating UNBOUND..."
# Basic
cp $basic/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "local-zone: \""$2"\" redirect\nlocal-data: \""$2" A 0.0.0.0\""}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > unbound.conf
mv -f unbound.conf $basic/unbound.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Blu
cp $blu/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "local-zone: \""$2"\" redirect\nlocal-data: \""$2" A 0.0.0.0\""}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > unbound.conf
mv -f unbound.conf $blu/unbound.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Blu Go
cp $bGo/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "local-zone: \""$2"\" redirect\nlocal-data: \""$2" A 0.0.0.0\""}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > unbound.conf
mv -f unbound.conf $bGo/unbound.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Porn
cp $porn/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "local-zone: \""$2"\" redirect\nlocal-data: \""$2" A 0.0.0.0\""}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > unbound.conf
mv -f unbound.conf $porn/unbound.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Ultimate
cp $ultimate/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "local-zone: \""$2"\" redirect\nlocal-data: \""$2" A 0.0.0.0\""}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > unbound.conf
mv -f unbound.conf $ultimate/unbound.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"
# Unified

cp $unified/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print "local-zone: \""$2"\" redirect\nlocal-data: \""$2" A 0.0.0.0\""}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > unbound.conf
mv -f unbound.conf $unified/unbound.conf
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Domains List
echo "[+] Creating Domain Lists..."
# Basic
cp $basic/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print ""$2" "}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > domains.txt
mv -f domains.txt $basic/domains.txt
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Blu
cp $blu/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print ""$2" "}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > domains.txt
mv -f domains.txt $blu/domains.txt
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Blu Go
cp $bGo/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print ""$2" "}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > domains.txt
mv -f domains.txt $bGo/domains.txt
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Porn
cp $porn/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print ""$2" "}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > domains.txt
mv -f domains.txt $porn/domains.txt
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Ultimate
cp $ultimate/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print ""$2" "}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > domains.txt
mv -f domains.txt $ultimate/domains.txt
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Unified
cp $unified/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print ""$2" "}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $header $tempConf/conf.tmp > domains.txt
mv -f domains.txt $unified/domains.txt
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# RPZ
echo "[+] Creating RPZ..."
# Basic
cp $basic/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print ""$2" CNAME ."}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $rpzheader $tempConf/conf.tmp > rpz.txt
mv -f rpz.txt $basic/rpz.txt
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Blu
cp $blu/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print ""$2" CNAME ."}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $rpzheader $tempConf/conf.tmp > rpz.txt
mv -f rpz.txt $blu/rpz.txt
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Blu Go
cp $bGo/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print ""$2" CNAME ."}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $rpzheader $tempConf/conf.tmp > rpz.txt
mv -f rpz.txt $bGo/rpz.txt
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Porn
cp $porn/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print ""$2" CNAME ."}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $rpzheader $tempConf/conf.tmp > rpz.txt
mv -f rpz.txt $porn/rpz.txt
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Ultimate
cp $ultimate/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print ""$2" CNAME ."}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $rpzheader $tempConf/conf.tmp > rpz.txt
mv -f rpz.txt $ultimate/rpz.txt
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

# Unified
cp $unified/hosts $tmp/temp.tmp
awk '$1 == "0.0.0.0"  { print ""$2" CNAME ."}' $tmp/temp.tmp  > $tempConf/conf.tmp
cat $rpzheader $tempConf/conf.tmp > rpz.txt
mv -f rpz.txt $unified/rpz.txt
rm -f "$tmp/temp.tmp" "$tempConf/conf.tmp"

echo "[+] Done!..."
# Ends.