FROM openjdk:8-jdk
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823
RUN apt-get update
RUN apt-get install -y nodejs sbt make gcc g++ build-essential
RUN npm install --unsafe-perm -g truffle@5.0.17 ganache-cli@6.4.3
RUN mkdir -m 777 /usr/lib/node_modules/truffle/node_modules/.cache
RUN apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
RUN groupadd -g 497 docker
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
RUN apt-get update
RUN apt-get install -y docker-ce docker-ce-cli containerd.io
RUN useradd -u 500 -m ec2-user -G docker
