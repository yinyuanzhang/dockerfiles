FROM aguamala/centos:7
MAINTAINER "gabo" <aguamala@deobieta.com>

RUN yum install -y python-pip &&\
     pip install --upgrade pip &&\
     pip install awscli &&\
     yum clean all

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["aws","--version"]
ENTRYPOINT ["/entrypoint.sh"]
