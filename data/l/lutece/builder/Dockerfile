FROM debian:stretch as builder

# install needed apps
RUN echo 'mysql-server mysql-server/root_password password motdepasse' | debconf-set-selections && \
    echo 'mysql-server mysql-server/root_password_again password motdepasse' | debconf-set-selections && \
    apt-get update && apt-get dist-upgrade -y && \
    apt-get install -y mysql-server mysql-client default-jdk ant maven git tomcat8 --no-install-recommends
