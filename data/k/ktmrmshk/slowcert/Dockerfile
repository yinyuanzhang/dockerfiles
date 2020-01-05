# 
#
# $ docker run --rm -d -v${PWD}:/cred -p5000:7749 slowcert 

FROM python:3.6-slim
COPY requirements.txt requirements.txt

RUN apt update && apt -y install vim dnsutils git \
      && apt clean \
      && rm -rf /var/lib/apt/lists/* \
      && pip install -r requirements.txt \
      && rm -rf /root/.cache \
      && mkdir kitapylib \
      && cd kitapylib \
      && git clone https://github.com/ktmrmshk/kitopen.git \
      && git clone https://github.com/ktmrmshk/ssl_flash.git 

RUN mkdir -p /slowcert/
COPY . /slowcert/

ENV CREDFILE /cred/.edgerc
ENV CREDSECTION default
ENV PYTHONPATH /kitapylib/:$PYTHONPATH

WORKDIR /slowcert
#CMD python3 slowcert_web.py
CMD ["gunicorn", "--workers=4", "-k", "gevent", "-b", "0.0.0.0:7749", "--timeout", "150", "slowcert_web:app"]



