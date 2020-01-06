FROM hotio/suitarr:nzbget

WORKDIR /tmp/.sbm4a_setup

RUN apt -yq update && \ 
  apt -yq upgrade && \ 
  apt -yq install \ 
    wget \ 
    git \ 
    curl \ 
    nano \ 
    xz-utils \ 
    python-setuptools \
    python-pip && \
  pip install --no-cache-dir \
    requests \
    requests[security] \
    requests-cache \
    babelfish \
    'guessit<2' \
    'subliminal<2' \
    stevedore==1.19.1 \
    python-dateutil \
    qtfaststart && \
  pip install --no-cache-dir --upgrade \
    pip \
    setuptools \
    requests \
    requests[security] \
    requests-cache \
    babelfish \
    'guessit<2' \
    'subliminal<2' \
    stevedore==1.19.1 \
    python-dateutil \
    qtfaststart && \
  rm -rf /tmp/*

# Get ffmpeg static release
RUN curl https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-static.tar.xz -o ffmpeg-release-64bit-static.tar.xz
RUN tar -xf ffmpeg-release-64bit-static.tar.xz
RUN rm ffmpeg-release-64bit-static.tar.xz
#RUN cd ffmpeg-*-static
RUN cp ffmpeg-*-static/ffmpeg /usr/bin
RUN cp ffmpeg-*-static/ffprobe /usr/bin
RUN chmod 0777 /usr/bin/ffmpeg
RUN chmod 0777 /usr/bin/ffprobe

RUN mkdir /sickbeard_mp4_automator
RUN mkdir /var/log/sickbeard_mp4_automator

COPY ./shortcuts/sbm4a /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a

COPY ./shortcuts/sbm4a-dvd /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a-dvd

COPY ./shortcuts/sbm4a-hd /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a-hd

COPY ./shortcuts/sbm4a-fullhd /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a-fullhd

COPY ./shortcuts/sbm4a-avcmini /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a-avcmini

COPY ./shortcuts/sbm4a-hevcmini /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a-hevcmini

COPY ./shortcuts/sbm4a-tag /usr/local/bin
RUN chmod 0777 /usr/local/bin/sbm4a-tag

RUN chmod 0777 -R /sickbeard_mp4_automator
RUN chmod 0777 -R /var/log/sickbeard_mp4_automator

VOLUME ["/sickbeard_mp4_automator"]
