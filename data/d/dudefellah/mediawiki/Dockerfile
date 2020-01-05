FROM mediawiki:1.31 as builder

RUN apt-get update && apt-get -y install gawk git rsync sed

RUN	for ext in mediawiki-extensions-LdapAuthentication:REL1_31 \
		mediawiki-extensions-PluggableAuth:5.4 \
		mediawiki-extensions-SimpleSAMLphp:4.1; do \
		cd /tmp && \
			extension_name=$(echo $ext | awk -F':' '{print $1}') && \
			extension_branch=$(echo $ext | awk -F':' '{print $2}') && \
			install_dirname=$(echo $extension_name | sed 's/^mediawiki-extensions-//') && \
			git clone https://github.com/wikimedia/$extension_name && \
			cd $extension_name && \
			git checkout $extension_branch && \
			cd .. && \
			rsync -avz --exclude=.git $extension_name /var/www/html/extensions/$install_dirname \
	; done

RUN for mod in ldap remoteip; do \
		a2enmod $mod \
	; done

FROM builder as cleanup

RUN rm -rf /tmp/mediawiki-extensions-* && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*
