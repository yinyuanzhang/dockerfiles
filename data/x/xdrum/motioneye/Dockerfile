FROM ubuntu:14.04

MAINTAINER Alessio Cassibba (x-drum) <swapon@gmail.com>

RUN echo "deb http://ppa.launchpad.net/mc3man/trusty-media/ubuntu trusty main" \
  > /etc/apt/sources.list.d/media.list \
  && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED8E640A \
  && apt-get update \
  && apt-get install -y \
  python-tornado \
  python-jinja2 \
  python-imaging \
  libcurl4-openssl-dev \
  libjpeg-dev \
  libssl-dev \
  motion \
  ffmpeg \
  v4l-utils \
  git

RUN git clone https://github.com/ccrisan/motioneye /motioneye \
  && cd /motioneye \
  && mv /motioneye/motioneye/* /motioneye \
  && rm -rf /motioneye/motioneye \
  && mkdir /etc/motioneye /var/lib/motioneye \
  && cp /motioneye/extra/motioneye.conf.sample /etc/motioneye/motion.conf
  
VOLUME ["/storage"]
WORKDIR /motioneye

EXPOSE 8765

CMD ["/usr/bin/python","/motioneye/meyectl.py", "startserver"]
