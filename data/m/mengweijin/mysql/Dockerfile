# 基础镜像
FROM mysql:8.0
# 维护者信息
MAINTAINER Meng Wei Jin mengweijin.work@foxmail.com

# 设置镜像时区为东八区时区，上海
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 将mysql.cnf拷贝到容器的/etc/mysql/conf.d/目录下，/etc/mysql/conf.d/必须带有后边的"/"（表示目录）
# mysql.cnf主要是修改mysql编码为utf8mb4
COPY mysql.cnf /etc/mysql/conf.d/
