FROM python:alpine
RUN apk add --update --no-cache bash curl ffmpeg gcc git mercurial musl-dev nano python2 py-pip shadow supervisor tzdata vlc \
	&& pip install --upgrade pip \
	&& pip install timeshift youtube-dl \
	&& pip install -e hg+https://bitbucket.org/dbenamy/devcron#egg=devcron
	
RUN cp /usr/share/zoneinfo/America/New_York /etc/localtime \
	&& echo "America/New_York" > /etc/timezone \
	&& mkdir /cron \
	&& mkdir /output

ENV HOME /home/vlc
RUN adduser -D -u 1000 vlc && chown -R vlc:vlc $HOME && usermod -a -G audio,video vlc
WORKDIR $HOME
RUN cd $HOME \
	&& git clone https://github.com/streamlink/streamlink \
	&& cd streamlink && python setup.py install && cd .. && rm -R streamlink

RUN cd $HOME \
	&& git clone https://github.com/kurtmckee/feedparser.git \
	&& cd feedparser && python2 setup.py install && cd .. && rm -R feedparser
	
RUN cd $HOME \
	&& git clone https://github.com/svpino/rfeed.git \
	&& cd rfeed && python2 setup.py install && cd .. && rm -R rfeed
	
RUN apk del gcc musl-dev --no-cache \
	&& rm -Rf /tmp/*

ADD keepalive.conf /etc/supervisor/conf.d/
ADD supervisord.conf /etc/
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
