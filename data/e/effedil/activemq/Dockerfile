#ActiveMQ 5.10.1

FROM webcenter/openjdk:jre-8-headless
MAINTAINER Davegraziosi <davide.graziosi@exprivia.it>

# Update distro and install some packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install curl -y && \
    apt-get install supervisor -y && \
    apt-get install logrotate -y && \
    apt-get install locales -y && \
    update-locale LANG=C.UTF-8 LC_MESSAGES=POSIX && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales && \
    rm -rf /var/lib/apt/lists/*

# Copy the app setting
COPY assets/config/ /app/setup/config/
COPY assets/bin/ /app/setup/bin/
COPY assets/init /app/init
RUN chmod 755 /app/init
RUN chmod 775 /app/setup/bin/*


# Lauch app install
COPY assets/setup/ /app/setup/
RUN chmod 755 /app/setup/install
RUN /app/setup/install

# Expose all port
EXPOSE 8161 
EXPOSE 61616 
EXPOSE 5672
EXPOSE 61613
EXPOSE 1883 
EXPOSE 61614

# Expose some folders
VOLUME ["/data/activemq"]
VOLUME ["/var/log/activemq"]
VOLUME ["/opt/activemq/conf"]

#WORKDIR /opt/activemq

#ENTRYPOINT ["/app/init"]
CMD ["/app/init", "start"]

