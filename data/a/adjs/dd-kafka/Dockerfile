FROM datadog/docker-dd-agent
ADD conf/kafka.yaml /etc/dd-agent/conf.d/kafka.yaml

RUN apt-get update && apt-get install -y software-properties-common && apt-add-repository -y ppa:webupd8team/java  && apt-get update

RUN echo oracle-java-8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
       && apt-get install -y oracle-java8-installer oracle-java8-set-default mysql-server supervisor git curl

