# PhyML-SMS
# 
# v1.8.1

# base image: ubuntu
FROM ubuntu:xenial

# File Author / Maintainer
MAINTAINER Frederic Lemoine <frederic.lemoine@pasteur.fr>

ENV PATH="/usr/local/sms-1.8.1/:${PATH}"

RUN apt-get update --fix-missing \
    && apt-get install -y wget gcc make bc unzip r-base\
    && apt-get autoremove
RUN cd /usr/local/ \
    && wget http://www.atgc-montpellier.fr/download/sources/sms/sms-1.8.1.zip \
    && unzip sms-1.8.1.zip \
    && rm -rf sms-1.8.1.zip \
    && cd sms-1.8.1 \
    && make \
    && find . -type f -exec sh -c 'chmod 644 {}' \; \
    && find . -type d -exec sh -c 'chmod 755 {}' \; \
    && find . -name "*.sh" -exec sh -c 'chmod 755 {}' \; \
    && find . -name "*.R" -exec sh -c 'chmod 755 {}' \; \
    && chmod +x phyml-src/phyml \
    && rm -rf phyml-src/phyml-20120412* \
    && cd /usr/local \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /pasteur

ENTRYPOINT ["/usr/local/sms-1.8.1/sms.sh"]
