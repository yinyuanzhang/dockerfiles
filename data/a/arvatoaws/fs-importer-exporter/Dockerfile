FROM amazonlinux:2

RUN mkdir /efs

ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV BUCKET none
ENV DIRECTION export

ADD start.sh /
RUN chmod ugoa+rwx /start.sh
RUN yum upgrade -y && yum install -y awscli

CMD /start.sh
