FROM jenkins/jenkins:lts
MAINTAINER Meng Wei Jin mengweijin.work@foxmail.com

# 使用root用户安装
USER root

# 安装 maven
ARG MAVEN_VERSION=3.5.4
ARG MAVEN_NAME=maven.tar.gz 
ARG MAVEN_URL=https://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz

RUN apt-get update && apt-get install -y wget && \
	# 下载到当前目录
	wget -O ${MAVEN_NAME} ${MAVEN_URL} && \
	# 解压到/opt，解压后路径为：/opt/apache-maven-${MAVEN_VERSION}
	tar -zxvf ${MAVEN_NAME} -C /opt && \ 
	# 添加连接
	ln -s /opt/apache-maven-${MAVEN_VERSION} /opt/maven && \ 
	ln -s /opt/maven/bin/mvn /usr/local/bin && \ 
	# 删除压缩包 
	rm -f ${MAVEN_NAME}

# 环境变量 MAVEN_HOME
ENV MAVEN_HOME /opt/maven

# 设置镜像时区为东八区时区，上海
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Jenkins 插件
COPY resources/plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

# maven在jenkins中配置的位置
COPY resources/hudson.tasks.Maven.xml /var/jenkins_home/hudson.tasks.Maven.xml

# 切换回 jenkins 用户
USER jenkins

# EXPOSE/VOLUME 参考官方jenkins镜像的Dockerfile(默认：EXPOSE：8080，50000；VOLUME：/var/jenkins_home)
