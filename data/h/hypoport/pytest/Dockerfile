FROM python:3.7.4

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app

RUN pip install pytest

COPY ./docker_entrypoint.sh /

ENTRYPOINT ["/docker_entrypoint.sh"]