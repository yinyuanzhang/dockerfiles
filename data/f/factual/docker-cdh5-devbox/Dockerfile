FROM factual/docker-cdh5-dev

RUN rm -f /etc/service/sshd/down
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh
ADD sshd_config /etc/ssh/

RUN mkdir -p /share /local

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" >> /etc/apt/sources.list.d/docker.list

RUN apt-get update && apt-get install -y \
    bash-completion \
    byobu \
    docker-engine \
    oozie-client \
    wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /etc/service/docker
ADD docker.sh /etc/service/docker/run

# Pass key environment variables to users
RUN echo "HADOOP_CONF_DIR=$HADOOP_CONF_DIR" >> /etc/environment && \
    echo "HIVE_HOME=$HIVE_HOME" >> /etc/environment && \
    echo "MAVEN_PATH=$MAVEN_PATH" >> /etc/environment && \
    echo "PATH=$PATH" >> /etc/environment && \
    echo "SPARK_HOME=$SPARK_HOME" >> /etc/environment

VOLUME ["/home","/share", "/local"]
