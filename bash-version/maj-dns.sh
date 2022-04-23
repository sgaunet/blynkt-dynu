#!/bin/bash

export login=your_login_on_dynu.net
export password=your_password
export dyndns=yourdomain.dynu.net

ping -c 1 ${dyndns} | head -n 1 | awk -F"(" '{ print $2 }' | awk -F")" '{ print $1 }'

ip_dns=$(dig @8.8.8.8 ANY bkl.dynu.net +short | grep -v ":" | head -n1)
real_ip=$(dig @ns1-1.akamaitech.net ANY whoami.akamai.net +short)

echo "IP_DNS=$ip_dns"
echo "REAL_IP=$real_ip"

if [ "$ip_dns" != "$real_ip" ]
then
	echo "MAJ DNS"
	curl "https://${login}:${password}@api.dynu.com/nice/updadte?hostname=${dyndns}"
else
	echo "No Need"
fi
