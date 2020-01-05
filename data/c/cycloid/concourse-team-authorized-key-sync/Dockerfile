FROM python:3.7

RUN mkdir /datas

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY sync.py /
COPY entrypoint.sh /

WORKDIR /
ENTRYPOINT ["/entrypoint.sh"]
