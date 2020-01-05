FROM python:3-alpine
MAINTAINER Juan Matias Kungfu de la Camara <juan.delacamara@3xmgroup.com&gt;

RUN mkdir -p /curator && chmod 777 /curator

COPY bootup.sh /curator/bootup.sh

RUN chmod ug+x /curator/bootup.sh

WORKDIR /curator

RUN pip install elasticsearch-curator==5.7.0

CMD /bin/sh -c '/curator/bootup.sh'
