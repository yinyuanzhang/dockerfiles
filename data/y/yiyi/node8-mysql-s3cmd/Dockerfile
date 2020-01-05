FROM iwashi/docker-node8-mysql-client

# install s3cmd
RUN apt update && apt install -y \
  python-dev \
  python-pip \
  wget \
  && pip install s3cmd \
  && apt-get -y autoremove \
  && apt-get clean \
  && apt-get autoclean

# install dockerize
ENV DOCKERIZE_VERSION v0.3.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz