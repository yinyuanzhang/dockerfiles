# Pull the fork of the official kali image ;)
FROM pidof/kalister:booya

# Metadata params
ARG BUILD_DATE
ARG VERSION
ARG VCS_URL
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url=$VCS_URL \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.version=$VERSION \
      org.label-schema.name='Kali Linux' \
      org.label-schema.description='Kinda Offical Kali Linux docker image' \
      org.label-schema.usage='https://www.kali.org/news/official-kali-linux-docker-images/' \
      org.label-schema.url='https://www.kali.org/' \
      org.label-schema.vendor='Offensive Security' \
      org.label-schema.schema-version='1.0' \
      org.label-schema.docker.cmd='docker run --rm pidof/kali' \
      org.label-schema.docker.cmd.devel='docker run --rm -ti pidof/kali' \
      org.label-schema.docker.debug='docker logs $CONTAINER' \
      io.github.offensive-security.docker.dockerfile="Dockerfile" \
      io.github.offensive-security.license="GPLv3" \
      MAINTAINER="pidof <pidof@mexican.name>"
RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list && \
    echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list
ENV DEBIAN_FRONTEND noninteractive

RUN set -x \
    && apt-get -yqq update \
    && apt-get -yqq upgrade \
    && apt-get -yqq dist-upgrade \
    && apt-get clean

RUN apt-get install -y metasploit-framework

RUN sed -i 's/systemctl status ${PG_SERVICE}/service ${PG_SERVICE} status/g' /usr/bin/msfdb && \
    service postgresql start && \
    msfdb reinit
# Establish a working directory
RUN apt-get install -y git \
    && cd /root \
    && git clone --recursive git://github.com/anoncam/Sn1per.git \
    && cd /root/Sn1per \
    && bash /root/Sn1per/install.sh
# Add the following to run the professional version.
# cd /usr/share/sniper/
# wget https://xerosecurity.com/pro/6.0/[YOURCUSTOMLICENSEKEYHERE]/pro.sh -O pro.sh
# If you did that: you need to configure the entrypoint and config/expose the web service.
CMD ["/bin/bash"]