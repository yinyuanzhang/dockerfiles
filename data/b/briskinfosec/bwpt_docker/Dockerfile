FROM ubuntu:latest
MAINTAINER Briskinfosec Technology and Consulting Pvt Ltd (contact@briskinfosec.com)
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y wget python-pip python python-docutils perl sslscan apt-utils sqlmap \
    nmap dnsrecon dnswalk whois wapiti dirb nikto host git whatweb wafw00f


RUN git clone https://github.com/golismero/golismero.git /golismero && \
    cd golismero && pip install -r requirements.txt && pip install -r requirements_unix.txt && \
    ln -s /golismero/golismero.py /usr/bin/golismero

RUN pip install --upgrade setuptools && pip install --upgrade sslyze

RUN git clone https://github.com/laramies/theHarvester.git /theharvester && \
    cd /theharvester && pip install -r requirements.txt && chmod +x theHarvester.py

RUN git clone https://github.com/skavngr/rapidscan.git /rapidscan && \
    cd /rapidscan && chmod +x rapidscan.py

RUN git clone https://github.com/w-digital-scanner/w9scan.git /w9scan && \
    cd /w9scan && python w9scan.py --update

RUN git clone https://github.com/zdresearch/OWASP-Nettacker.git /OWASP-Nettacker && \
    cd OWASP-Nettacker && pip install -r requirements.txt

RUN git clone https://github.com/s0md3v/Striker.git /Striker && \
    cd Striker && pip install -r requirements.txt

WORKDIR /root/
RUN mkdir /root/webdocker
COPY rapidscan.sh /root/webdocker/rapidscan.sh
COPY w9scan.sh /root/webdocker/w9scan.sh
COPY sqlmap.sh /root/webdocker/sqlmap.sh
COPY OWASP-nettacker.sh /root/webdocker/OWASP-nettacker.sh
COPY striker.sh /root/webdocker/striker.sh

EXPOSE 80
