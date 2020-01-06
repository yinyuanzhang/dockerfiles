#
# 自定义的docker-compose 镜像
# 增加到当前项目目录下启动的功能
#

FROM dduportal/docker-compose

MAINTAINER Dennis Zou <denniszou@gmail.com>

COPY run-docker-compose /usr/local/bin/run-docker-compose

WORKDIR /app

ENTRYPOINT ["/usr/local/bin/run-docker-compose"]
CMD ["--version"]


