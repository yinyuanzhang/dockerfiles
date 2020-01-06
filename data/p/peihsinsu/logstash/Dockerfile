FROM debian

RUN apt-get update
RUN apt-get install apache2 -y
RUN apt-get install gnuplot -y

RUN apt-get install openjdk-7-jre -y
RUN apt-get install curl -y

RUN cd / && curl -O https://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.tar.gz &&\
  tar zxvf logstash-1.4.2.tar.gz &&\
  cd logstash-1.4.2 
RUN cd /logstash-1.4.2 && ./bin/plugin install contrib
RUN echo -e '\n# logstash\nexport PATH="/logstash-1.4.2/bin:$PATH"' >> /root/.bashrc

RUN rm /logstash-1.4.2.tar.gz

WORKDIR /data
