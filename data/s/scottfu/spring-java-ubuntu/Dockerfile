FROM ubuntu:bionic
MAINTAINER  Scott Fu <scott.fu@outlook.com>

#get package list
RUN apt-get update

#default time zone
ENV TZ=UTC    
RUN echo $TZ > /etc/timezone && \
    apt-get install -y tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata
	
#java home
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# install java
RUN apt-get install -y openjdk-8-jdk

# show the java info
RUN java -version

# from spring boot guide https://spring.io/guides/gs/spring-boot-docker/#initial
VOLUME /tmp

# default direcoty for application
RUN mkdir /app
WORKDIR /app

# clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && apt-get autoremove

# environment variables
# jar name, can be passed from docker compose or docker lunch command
ENV JAR_NAME "spring-boot.jar"
ENV JAVA_OPTIONS=''

# entry point
ENTRYPOINT ["sh", "-c", "java ${JAVA_OPTIONS} -jar /app/${JAR_NAME}"]
