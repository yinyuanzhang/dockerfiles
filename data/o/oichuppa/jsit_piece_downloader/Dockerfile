FROM openjdk:12
COPY /run.sh /run.sh 
RUN chmod 777 /run.sh
RUN yum install wget -y
VOLUME /JSIT
VOLUME /Logs
VOLUME /Downloads
ENTRYPOINT /run.sh
