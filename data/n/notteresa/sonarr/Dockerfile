FROM linuxserver/sonarr

RUN \
  apt-get update && \
  apt-get install -y \
  ffmpeg \
  wget \
  unrar \
  git \
  python-pip \
  openssl \
  python-dev \
  libffi-dev \
  libssl-dev \
  libxml2-dev \
  libxslt1-dev \
  zlib1g-dev

RUN \
  pip install --upgrade pip && \
  hash -r pip && \
  pip install wget && \
  pip install requests && \
  pip install requests[security] && \
  pip install requests-cache && \
  pip install babelfish && \
  pip install 'guessit<2' && \
  pip install 'subliminal<2' && \
  pip install stevedore==1.19.1 && \
  pip install python-dateutil && \
  pip install qtfaststart && \
  git clone git://github.com/mdhiggins/sickbeard_mp4_automator.git /sickbeard_mp4_automator/ && \
  wget https://raw.githubusercontent.com/NotTeresa/PlexGuide/WCKD/scripts/realdebrid/autoProcess.ini -O /sickbeard_mp4_automator/autoProcess.ini && \
  wget https://raw.githubusercontent.com/NotTeresa/PlexGuide/WCKD/scripts/realdebrid/RealDebrid.py -P /app && \
  touch /sickbeard_mp4_automator/info.log && \
  chmod a+rwx -R /sickbeard_mp4_automator && \
  chmod a+rwx -R /app && \
  chown -R abc:abc /downloads && \
  rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*
