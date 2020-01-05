# 基础镜像
FROM tomcat:8
# 维护者信息
MAINTAINER Meng Wei Jin mengweijin.work@foxmail.com

# 设置镜像时区为东八区时区，上海
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
