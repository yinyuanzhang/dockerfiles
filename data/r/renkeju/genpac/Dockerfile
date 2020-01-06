FROM python:3.5-buster

ENV PYPI_REPO=https://pypi.tuna.tsinghua.edu.cn/simple SQUID_HTTP_PORT=8080

WORKDIR /usr/src/app

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i ${PYPI_REPO} &&\
    mkdir -p pac dnsmasq.d

ADD entrypoint.sh .
ADD config.ini.j2 .
ADD action.yaml .
COPY rules rules

CMD [ "/bin/bash", "entrypoint.sh" ]
