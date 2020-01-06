FROM iotsec/arm-alpine

ENV P0F_RELEASE "http://lcamtuf.coredump.cx/p0f3/releases/p0f-3.09b.tgz"

RUN apk --update add python3 python3-dev build-base \
            mariadb-dev \
            nmap \
            wget \
            libpcap-dev \
	    tcpdump \
	    bash
RUN cd tmp && wget $P0F_RELEASE &&\
  tar xvf p0f-3.09b.tgz

RUN  cd /tmp/p0f-3.09b/ && chmod +x ./build.sh && /bin/sh ./build.sh &&\
  mkdir /etc/p0f/ &&\
  cp p0f /bin && cp p0f.fp /etc/p0f

RUN pip3 install requests scapy p0f

COPY ./ioscan.py /usr/bin/ioscan.py
COPY ./api.py /usr/lib/python3.6/site-packages/api.py
COPY ./jwt.py /usr/lib/python3.6/site-packages/jwt.py
COPY ./run_ioscan /usr/bin/run_ioscan

CMD sh /usr/bin/run_ioscan
