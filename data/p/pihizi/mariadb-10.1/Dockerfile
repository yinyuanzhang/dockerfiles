FROM mariadb:10.1
MAINTAINER PiHiZi <pihizi@msn.com>

RUN mkdir /app && echo 'export PATH="/app/bin:$PATH"'>/etc/profile.d/docker
ADD bin /app/bin

VOLUME ["/etc/mysql", "/var/lib/mysql", "/var/log/mysql"]
WORKDIR /app

EXPOSE 3306

ENV PATH=/app/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

CMD "/app/bin/run"
