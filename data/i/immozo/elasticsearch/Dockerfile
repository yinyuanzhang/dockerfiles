FROM sebp/elk

RUN apt-get install -y libmysql-java
RUN mkdir /etc/logstash/conf.d/lastrun
RUN chown logstash:logstash /etc/logstash/conf.d/lastrun
