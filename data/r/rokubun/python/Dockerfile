FROM rokubun/python:base-slim-stretch

RUN apt-get update \
 && apt-get install -y build-essential \
 && pip install --upgrade pip \
 && pip install numpy \
 && pip install uwsgi \
 && apt-get remove -y `grep Install /var/log/apt/history.log | tail -1 | sed 's/Install://g;s/), /\n/g' | cut -d: -f1 | paste -s -d " "`

CMD ["sh"]
