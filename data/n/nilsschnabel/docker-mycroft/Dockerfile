#FROM debian:jessie-slim
FROM codingwell/rpi-raspbian-qemu

ENV TERM linux
ENV DEBIAN_FRONTEND noninteractive

RUN [ "cross-build-start" ]

# Set the locale
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV PYTHONPATH $PYTHONPATH:/mycroft/ai

# basic setup
RUN set -x \
	&& sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get -y install git locales sudo \
  && sudo ln -s /etc/locale.alias /usr/share/locale/locale.alias \
	&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen \
  # cleanup
	&& apt-get -y autoremove \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# build mimic
RUN set -x \
  && apt-get update \
  && apt-get install gcc make pkg-config automake libtool libasound2-dev wget unzip patch \
  && git config --global http.sslVerify false \
  && git config --global http.postBuffer 1000M \
	&& git config --global https.postBuffer 1000M \ 
  && git clone --depth 1 --quiet --progress https:#github.com/MycroftAI/mimic.git \
  && cd mimic \
  #&& apt-get install patch
  && ./dependencies.sh --prefix="/usr/local" \
  && ./autogen.sh \
  && ./configure  --with-audio=alsa --enable-shared --prefix="/usr/local" \
  && make -j8 && make install \
  && cd .. \
  # cleanup
  && rm -rf mimic \
  && apt-get remove libasound2-dev \
	&& apt-get -y autoremove \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Server Dependencies for Mycroft
RUN set -x \
  && apt-get update \
  && apt-get install  python3 python3-pip \
	# for some reason, this has to be done without 'sudo' 
	&& apt-get install -y dbus pulseaudio pulseaudio-utils git python3 python3-dev python-setuptools python-gobject-2-dev libtool libffi-dev libssl-dev autoconf automake bison swig libglib2.0-dev portaudio19-dev mpg123 screen flac curl libicu-dev pkg-config automake libjpeg-dev libfann-dev build-essential jq \
	&& pip3 install future msm \
	&& git config --global http.sslVerify false \
  && git config --global http.postBuffer 100M \
	&& git config --global https.postBuffer 100M \ 
	# Checkout Mycroft
  #&& export GIT_TRACE=1 && export GIT_CURL_VERBOSE=1
	&& git clone --depth 1 --quiet --progress https:#github.com/MycroftAI/mycroft-core.git /opt/mycroft \
	&& cd /opt/mycroft \
	&& mkdir /opt/mycroft/skills \
	&& /opt/mycroft/./dev_setup.sh --allow-root -sm \
	&& mkdir /opt/mycroft/scripts/logs \
	&& touch /opt/mycroft/scripts/logs/mycroft-bus.log \
	&& touch /opt/mycroft/scripts/logs/mycroft-voice.log \
	&& touch /opt/mycroft/scripts/logs/mycroft-skills.log \
	&& touch /opt/mycroft/scripts/logs/mycroft-audio.log \
  && curl -L http:#ftp.de.debian.org/debian/pool/main/libf/libfann/libfann2_2.2.0+ds-3_armhf.deb -o libfann2_2.2.0+ds-3_armhf.deb \
  && curl -L http:#ftp.de.debian.org/debian/pool/main/libf/libfann/libfann-dev_2.2.0+ds-3_armhf.deb -o libfann-dev_2.2.0+ds-3_armhf.deb \
  && dpkg -i libfann2_2.2.0+ds-3_armhf.deb libfann-dev_2.2.0+ds-3_armhf.deb && rm libfann2_2.2.0+ds-3_armhf.deb libfann-dev_2.2.0+ds-3_armhf.deb \
	&& apt-get -y autoremove \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
	&& /bin/bash -c "source /opt/mycroft/.venv/bin/activate" \
	&& chmod +x /opt/mycroft/start-mycroft.sh \
	&& /bin/bash /opt/mycroft/start-mycroft.sh all



WORKDIR /opt/mycroft
COPY startup.sh /opt/mycroft
RUN chmod +x /opt/mycroft/startup.sh

RUN [ "cross-build-end" ]

EXPOSE 8181

ENTRYPOINT ["/bin/bash", "/opt/mycroft/startup.sh"]
