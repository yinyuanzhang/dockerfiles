FROM bwainstock/python:2.4-centos
VOLUME /app
WORKDIR /app
RUN find /etc/yum.repos.d/ -name "*.repo" | xargs -n1 sed -i 's/gpgcheck=1/gpgcheck=0/g'
CMD ["nosetests", "-v"]
