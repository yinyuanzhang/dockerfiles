FROM ruby:2.2.0
MAINTAINER Frank Wang "eternnoir@gmail.com"

RUN apt-get update && apt-get install -y libcurl4-gnutls-dev make && apt-get clean
RUN gem install fluentd -v "~>0.12.3"
RUN mkdir /etc/fluent
RUN /usr/local/bin/gem install fluent-plugin-elasticsearch
ADD fluent.conf /etc/fluent/
RUN mkdir /var/config
VOLUME /var/config
EXPOSE 24224
ENV CONFIG_PATH = "/etc/fluent/fluent.conf"
CMD ["sh","-c","/usr/local/bundle/bin/fluentd", "-c", "$CONFIG_PATH"]
