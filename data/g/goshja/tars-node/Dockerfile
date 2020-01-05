FROM goshja/tars-node:php
MAINTAINER goshja goshja <goshja@qq.com>
RUN yum install -y npm
RUN npm install -g socketlog-server
RUN socketlog-server > /dev/null &
ENTRYPOINT socketlog-server > /dev/null & /sbin/entrypoint.sh && /sbin/entrypoint.sh start