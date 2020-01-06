FROM debian:jessie
RUN apt-get update \
    && apt-get install -y beanstalkd \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && apt-get autoclean -y \
    && rm -rf /var/lib/apt/lists/*

VOLUME /var/lib/beanstalkd/data

EXPOSE 11300
CMD ["beanstalkd", "-p", "11300", "-b", "/var/lib/beanstalkd/data"]