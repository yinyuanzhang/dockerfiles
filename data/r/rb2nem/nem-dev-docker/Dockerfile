FROM fedora:22
MAINTAINER rb2
RUN dnf -y install java-1.8.0-openjdk-headless.x86_64 tar tmux gnupg.x86_64 git unzip which findutils java-1.8.0-openjdk-devel vim
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
ENV JAVA_HOME=/usr
RUN curl -s get.sdkman.io | bash
RUN source "$HOME/.sdkman/bin/sdkman-init.sh" && sdk install maven
RUN source "$HOME/.sdkman/bin/sdkman-init.sh" && sdk install groovy
WORKDIR /root/ 
RUN git clone https://github.com/NewEconomyMovement/nem.core.git
WORKDIR /root/nem.core
RUN source "$HOME/.sdkman/bin/sdkman-init.sh" && mvn clean compile install -DskipTests=true
RUN mkdir /root/.groovy/lib/ -p
# place dependencies in /root/nem.core/target
RUN source "$HOME/.sdkman/bin/sdkman-init.sh" && mvn dependency:copy-dependencies -DoutputDirectory=/root/.groovy/lib/
RUN cp /root/nem.core/target/nem-core-0.6.73-BETA.jar /root/.groovy/lib/
COPY test.groovy /root/

