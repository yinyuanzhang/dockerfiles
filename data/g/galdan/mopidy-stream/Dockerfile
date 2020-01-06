FROM phusion/baseimage:latest
MAINTAINER Thomas Beyer <beyer.thomas@gmail.com>

##########################################################################################
# baseimage specific stuff
ENV HOME /root

RUN set -ex \
# Disable SSH
&& rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh \
# Install Software
&& apt-get update \
&& apt-get install -y \
    wget \
    software-properties-common \
    sudo \
    git \
    python-cffi \
    mpc \
    nano \
    curl \
    icecast2 \
&& wget -q -O - http://apt.mopidy.com/mopidy.gpg | apt-key add - \
&& wget -q -O /etc/apt/sources.list.d/mopidy.list http://apt.mopidy.com/mopidy.list \
&& apt-get -qq update \
&& apt-get install -y \
    mopidy \
    python-spotify \
&& curl -L https://bootstrap.pypa.io/get-pip.py | python - \
&& git clone https://github.com/kingosticks/mopidy-spotify.git \
&& cd mopidy-spotify \
&& git checkout "fix/web_api_playlists" \
&& python2.7 setup.py build install \
&& pip install \
    Mopidy-Moped \
    Mopidy-Iris \
    Mopidy-YouTube \
## Clean Up
&& apt-get purge --auto-remove -y \
    curl \
    gcc \
    git \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ~/.cache

# Add configurations
ADD cfg/mopidy.conf /etc/mopidy/mopidy.conf
ADD cfg/icecast.xml /etc/icecast2/icecast.xml
ADD silence.mp3 /usr/share/icecast2/web/silence.mp3

# Add init scripts
RUN mkdir /etc/service/00-icecast
ADD run/icecast.sh /etc/service/00-icecast/run
RUN chmod +x /etc/service/00-icecast/run

RUN mkdir /etc/service/01-mopidy
ADD run/mopidy.sh /etc/service/01-mopidy/run
RUN chmod +x /etc/service/01-mopidy/run

EXPOSE 6680
EXPOSE 6600
EXPOSE 8000

CMD ["/sbin/my_init"]