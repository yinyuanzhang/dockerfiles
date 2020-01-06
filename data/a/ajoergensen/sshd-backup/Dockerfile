FROM ajoergensen/openssh-server

RUN \
	apk -U upgrade && \
	apk add rsync libacl lz4-libs python3 py3-lz4 py3-msgpack && \
	apk add --virtual=.builddeps libressl-dev lz4-dev acl-dev build-base py-pip py-setuptools python3-dev linux-headers && \
	pip3.6 install borgbackup && \
	apk del .builddeps && \
	rm -rf /var/cache/apk/*
