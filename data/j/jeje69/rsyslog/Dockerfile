FROM rsyslog/syslog_appliance_alpine
RUN apk --no-cache update && apk --no-cache add openssh openssl expect zip tzdata \
&& cp /usr/share/zoneinfo/Europe/Paris /etc/localtime && apk del tzdata \
# Ajout pour lancer crond au démarrage du container
&& sed -i '2icrond' starter.sh \
# Ajout pour FIX (CVE-2019-5021) alpine
&& sed -i -e 's/^root::/root:!:/' /etc/shadow
