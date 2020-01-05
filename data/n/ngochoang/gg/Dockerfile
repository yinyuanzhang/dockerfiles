FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  apt-transport-https \
  gzip \
  curl \
  zip \
  build-essential

RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823

RUN apt-get update && apt-get install -y \
  git \
  openjdk-8-jdk \
  maven \
  gradle \
  openssh-client \
  python \
  sbt

# download sbt deps
RUN sbt compile

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
  && apt-get install -y nodejs

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"

RUN python3 get-pip.py

RUN pip install awscli

CMD /bin/bash  