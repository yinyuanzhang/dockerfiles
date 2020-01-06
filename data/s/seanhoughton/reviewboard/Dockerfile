FROM ubuntu:xenial
MAINTAINER sean.houghton@gmail.com

# This is needed in for xz compression in case you can't install EPEL.
# See https://github.com/ikatson/docker-reviewboard/issues/10
RUN apt-get -y -q update && apt-get -y -q install \
	libffi-dev \
	libjpeg8-dev \
	libssl-dev \
	libxml2-dev \
	libxslt1-dev \
	patch \
	postgresql \
	python-dev \
	python-ldap \
	python-pip \
	python-pip \
	uwsgi \
	uwsgi-plugin-python \
	zlib1g-dev

#https://kojipkgs.fedoraproject.org//packages/python-publicsuffix/1.1.0/1.el7/noarch/python2-publicsuffix-1.1.0-1.el7.noarch.rpm && \
#https://kojipkgs.fedoraproject.org//packages/python-djblets/0.9.4/3.el7/noarch/python-djblets-0.9.4-3.el7.noarch.rpm && \

# ReviewBoard runs on django 1.6, so we need to use a compatible django-storages
# version for S3 support.
RUN pip install ReviewBoard psycopg2 p4python

ADD start.sh /start.sh
ADD uwsgi.ini /uwsgi.ini
ADD shell.sh /shell.sh

RUN chmod +x start.sh shell.sh

VOLUME ["/root/.ssh", "/media/"]

EXPOSE 8000

CMD /start.sh
