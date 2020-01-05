FROM brumbrum/php-develop
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>

ADD bin/entrypoint.sh /entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]
