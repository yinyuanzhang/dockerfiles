FROM asgard/base:ubuntu1604

# Python 2.7
RUN apt-get install -y \
  python2.7 \
  python2.7-dev \
  python-pip \
  python-setuptools

# package
RUN pip install \
  luigi \
  python-daemon \
  sqlalchemy

# Luigi setup
RUN mkdir /etc/luigi /var/log/luigid /etc/service/luigid
ADD ./luigi/luigi.cfg /etc/luigi/client.cfg
ADD ./luigi/logrotate.cfg /etc/logrotate.d/luigid
ADD ./luigi/luigid.sh /etc/service/luigid/run
VOLUME /var/log/luigid

EXPOSE 8082

ENTRYPOINT ["/sbin/my_init"]
