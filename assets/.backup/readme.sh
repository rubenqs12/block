#!/bin/sh
# Energized Blu - Readme Creator
# make time stamp update
TIMESTAMP=`date +'%b %d, %Y'`
VERSION=`date +'%y.%m.%j'`
# Directory
bsc=../../basic/formats
hblu=../../blu/formats
bGo=../../bluGo/formats
prn=../../porn/formats
ulm=../../ultimate/formats
unf=../../unified/formats

# Entries Count
basict=$(egrep 'Total Domains:' $bsc/hosts)
blut=$(egrep 'Total Domains: ' $hblu/hosts)
blugot=$(egrep 'Total Domains: ' $bGo/hosts)
pornt=$(egrep 'Total Domains: ' $prn/hosts)
ultimatet=$(egrep 'Total Domains: ' $ulm/hosts)
unifiedt=$(egrep 'Total Domains: ' $unf/hosts)
# RAW & TXT Size
basics=$(ls -lah $bsc/hosts | awk '{print $5}')
blus=$(ls -lah $hblu/hosts | awk '{print $5}')
blugos=$(ls -lah $bGo/hosts | awk '{print $5}')
porns=$(ls -lah $prn/hosts | awk '{print $5}')
ultimates=$(ls -lah $ulm/hosts | awk '{print $5}')
unifieds=$(ls -lah $unf/hosts | awk '{print $5}')
# Domains List Size
basicds=$(ls -lah $bsc/domains.txt | awk '{print $5}')
bluds=$(ls -lah $hblu/domains.txt | awk '{print $5}')
blugods=$(ls -lah $bGo/domains.txt | awk '{print $5}')
pornds=$(ls -lah $prn/domains.txt | awk '{print $5}')
ultimateds=$(ls -lah $ulm/domains.txt | awk '{print $5}')
unifiedds=$(ls -lah $unf/domains.txt | awk '{print $5}')
# DNSMasq Size
basiccs=$(ls -lah $bsc/dnsmasq.conf | awk '{print $5}')
blucs=$(ls -lah $hblu/dnsmasq.conf | awk '{print $5}')
blugocs=$(ls -lah $bGo/dnsmasq.conf | awk '{print $5}')
porncs=$(ls -lah $prn/dnsmasq.conf | awk '{print $5}')
ultimatecs=$(ls -lah $ulm/dnsmasq.conf | awk '{print $5}')
unifiedcs=$(ls -lah $unf/dnsmasq.conf | awk '{print $5}')
# DNSMasq IPV6 Size
basicc6s=$(ls -lah $bsc/dnsmasq-ipv6.conf | awk '{print $5}')
bluc6s=$(ls -lah $hblu/dnsmasq-ipv6.conf | awk '{print $5}')
blugoc6s=$(ls -lah $bGo/dnsmasq-ipv6.conf | awk '{print $5}')
pornc6s=$(ls -lah $prn/dnsmasq-ipv6.conf | awk '{print $5}')
ultimatec6s=$(ls -lah $ulm/dnsmasq-ipv6.conf | awk '{print $5}')
unifiedc6s=$(ls -lah $unf/dnsmasq-ipv6.conf | awk '{print $5}')
# Unbound Size
basicus=$(ls -lah $bsc/unbound.conf | awk '{print $5}')
bluus=$(ls -lah $hblu/unbound.conf | awk '{print $5}')
blugous=$(ls -lah $bGo/unbound.conf | awk '{print $5}')
pornus=$(ls -lah $prn/unbound.conf | awk '{print $5}')
ultimateus=$(ls -lah $ulm/unbound.conf | awk '{print $5}')
unifiedus=$(ls -lah $unf/unbound.conf | awk '{print $5}')
# RPZ Size
basicrs=$(ls -lah $bsc/unbound.conf | awk '{print $5}')
blurs=$(ls -lah $hblu/unbound.conf | awk '{print $5}')
blugors=$(ls -lah $bGo/unbound.conf | awk '{print $5}')
pornrs=$(ls -lah $prn/unbound.conf | awk '{print $5}')
ultimaters=$(ls -lah $ulm/unbound.conf | awk '{print $5}')
unifiedrs=$(ls -lah $unf/unbound.conf | awk '{print $5}')
# add to readme
sed -e "s/_timestamp_/$TIMESTAMP/g" -e "s/_version_/$VERSION/g" -e "s/_basict_/$basict/g" -e "s/_blut_/$blut/g" -e "s/_blugot_/$blugot/g" -e "s/_pornt_/$pornt/g" -e "s/_ultimatet_/$ultimatet/g" -e "s/_unifiedt_/$unifiedt/g" -e "s/_basics_/$basics/g" -e "s/_blus_/$blus/g" -e "s/_blugos_/$blugos/g" -e "s/_porns_/$porns/g" -e "s/_ultimates_/$ultimates/g" -e "s/_unifieds_/$unifieds/g" -e "s/_basicds_/$basicds/g" -e "s/_bluds_/$bluds/g" -e "s/_blugods_/$blugods/g" -e "s/_pornds_/$pornds/g" -e "s/_ultimateds_/$ultimateds/g" -e "s/_unifiedds_/$unifiedds/g" -e "s/_basiccs_/$basiccs/g" -e "s/_blucs_/$blucs/g" -e "s/_blugocs_/$blugocs/g" -e "s/_porncs_/$porncs/g" -e "s/_ultimatecs_/$ultimatecs/g" -e "s/_unifiedcs_/$unifiedcs/g" -e "s/_basicc6s_/$basicc6s/g" -e "s/_bluc6s_/$bluc6s/g" -e "s/_blugoc6s_/$blugoc6s/g" -e "s/_pornc6s_/$pornc6s/g" -e "s/_ultimatec6s_/$ultimatec6s/g" -e "s/_unifiedc6s_/$unifiedc6s/g" -e "s/_basicus_/$basicus/g" -e "s/_bluus_/$bluus/g" -e "s/_blugous_/$blugous/g" -e "s/_pornus_/$pornus/g" -e "s/_ultimateus_/$ultimateus/g" -e "s/_unifiedus_/$unifiedus/g" -e "s/_basicrs_/$basicrs/g" -e "s/_blurs_/$blurs/g" -e "s/_blugors_/$blugors/g" -e "s/_pornrs_/$pornrs/g" -e "s/_ultimaters_/$ultimaters/g" -e "s/_unifiedrs_/$unifiedrs/g" readme.template > ../readme.tmp
echo >> ../readme.tmp
# add to file
cat ../readme.tmp  > ../../README.md
echo "- Adding Date"
echo "- Adding Version"
echo "- Adding Total Entries"
echo "- Adding Sizes"

# remove tmp file
rm -rf ../*.tmp

# remove extra text
echo "- Removing Extras"
sed -i -e 's/# Total Domains: //g' ../../README.md

echo "[+] Done !"

