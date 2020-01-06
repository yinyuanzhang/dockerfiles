FROM amazonlinux

MAINTAINER ein.gelehrte@gmail.com

RUN yum update -y && \
	yum install git vim -y && \
	yum install nginx -y && \
	yum install python35 python35-dev python35-setuptools python35-devel -y && \
	yum install gcc -y && \
	yum install python26-setuptools -y && \
	easy_install-2.6 supervisor

ADD . /home/docker/
RUN easy_install-3.5 virtualenv

WORKDIR /home/docker/
RUN virtualenv --no-site-packages .
RUN /bin/bash -c "source /home/docker/bin/activate"
RUN /home/docker/bin/pip3.5 install uwsgi
RUN /home/docker/bin/pip3.5 install flask
	
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN echo_supervisord_conf > /etc/supervisord.conf
RUN echo "[include]" >> /etc/supervisord.conf
RUN echo "files = supervisord.d/*.conf" >> /etc/supervisord.conf
RUN mkdir /etc/supervisord.d
RUN mkdir /var/log/uwsgi
RUN ln -s /home/docker/uwsgi.conf /etc/nginx/conf.d/
RUN ln -s /home/docker/supervisor.conf /etc/supervisord.d/

expose 8080
cmd ["supervisord", "-n"]
