FROM resin/armv7hf-debian

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install libssl-dev gcc libffi-dev python-openssl python-dev python-pip python-cheetah python-lxml wget && rm -rf /var/lib/apt/lists/* && pip install setuptools --upgrade && pip install pyopenssl --upgrade && pip install enum 

RUN wget --no-check-certificate https://github.com/CouchPotato/CouchPotatoServer/tarball/master -O couchpotato.tar.gz && tar -xzvf couchpotato.tar.gz && mv CouchPotato-CouchPotatoServer-* CouchPotato

VOLUME /data
VOLUME /config

EXPOSE 5050

RUN [ "cross-build-end"]

CMD python /CouchPotato/CouchPotato.py --data_dir /config --console_log
