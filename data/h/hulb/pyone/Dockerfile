FROM python:2.7.12
Maintainer hulb@live.cn
WORKDIR /root/PyOne

COPY . /root/PyOne

RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn","-k", "eventlet", "-b", "0.0.0.0:34567","run:app"]
