FROM linuxserver/sonarr:preview
MAINTAINER mdhiggins <mdhiggins23@gmail.com> & kahooli <kahooli@cavanaghs.id.au>

# get python3 and git, and install python libraries
RUN \
  apt-get update && \
  apt-get install -y \
    cron \
    git \
    wget \
    python3 \
    python3-pip && \
# install pip, venv, and set up a virtual self contained python environment
  python3 -m pip install --user --upgrade pip && \
  python3 -m pip install --user virtualenv && \
  mkdir /usr/local/bin/sma && \
  python3 -m virtualenv /usr/local/bin/sma/env && \
  /usr/local/bin/sma/env/bin/pip install requests \
    requests[security] \
    requests-cache \
    babelfish \
    'guessit<2' \
    'subliminal<2' \
    'stevedore==1.19.1' \
    python-dateutil \
    qtfaststart && \
# download repo
  git clone https://github.com/mdhiggins/sickbeard_mp4_automator.git /usr/local/bin/sma/sickbeard_mp4_automator && \
# create logging directory
  mkdir /var/log/sickbeard_mp4_automator && \
  touch /var/log/sickbeard_mp4_automator/index.log && \
  chgrp -R users /var/log/sickbeard_mp4_automator && \
  chmod -R g+w /var/log/sickbeard_mp4_automator && \
# ffmpeg
  wget https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz -O /tmp/ffmpeg.tar.xz --no-check-certificate && \
  mkdir /usr/local/bin/ffmpeg && \
  tar -xJf /tmp/ffmpeg.tar.xz -C /usr/local/bin/ffmpeg --strip-components 1 && \
  chgrp -R users /usr/local/bin/ffmpeg && \
  chmod g+x /usr/local/bin/ffmpeg/ffmpeg && \
  chmod g+x /usr/local/bin/ffmpeg/ffprobe && \
  echo "PATH=\"\$PATH:/usr/local/bin/ffmpeg\"" >> /etc/environment && \
  PATH="$PATH:/usr/local/bin/ffmpeg" && \
# cleanup
  apt-get clean && \
  rm -rf \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

# Modify postSonarr.py script to use the Python3 Virtual Environment setup for SMA
  RUN sed -i "s|#!/usr/bin/env python|#!/usr/local/bin/sma/env/bin/python3|g" /usr/local/bin/sma/sickbeard_mp4_automator/postSonarr.py

# Modify manual.py script to use the Python3 Virtual Environment setup for SMA
  RUN sed -i "s|#!/usr/bin/env python|#!/usr/local/bin/sma/env/bin/python3|g" /usr/local/bin/sma/sickbeard_mp4_automator/manual.py

# update script
  RUN printf "#!/bin/bash \
    \n# Updating installed packages \
    \napt-get update \
    \napt-get upgrade \
    \n# Updating MP4 Automator script \
    \ngit -C /usr/local/bin/sma/sickbeard_mp4_automator/ reset HEAD --hard \
    \ngit -C /usr/local/bin/sma/sickbeard_mp4_automator/ pull \
    \n# Updating Pyton dependancies \
    \npip install --upgrade PIP \
    \npip install --upgrade requests \
    \npip install --upgrade requests[security] \
    \npip install --upgrade requests-cache \
    \npip install --upgrade babelfish \
    \npip install --upgrade 'guessit<2' \
    \npip install --upgrade 'subliminal<2' \
    \npip install --upgrade python-dateutil \
    \npip install --upgrade qtfaststart \
    \npip uninstall --yes stevedore \
    \npip install stevedore==1.19.1 \
    \n# Updating FFMPEG \
    \nwget https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz -O /tmp/ffmpeg.tar.xz --no-check-certificate \
    \ntar -xJf /tmp/ffmpeg.tar.xz -C /usr/local/bin/ffmpeg --strip-components 1 \
    \nchgrp -R users /usr/local/bin/ffmpeg \
    \nchmod g+x /usr/local/bin/ffmpeg/ffmpeg \
    \nchmod g+x /usr/local/bin/ffmpeg/ffprobe\n" > /usr/local/bin/updatescript
  RUN chmod 0644 /usr/local/bin/updatescript
  RUN echo '00 00  *  *  *    /usr/local/bin/updatescript' > /etc/cron.d/update-chron
  RUN chmod 0644 /etc/cron.d/update-chron
  #CMD ['cron', '-l 2', '-f']
