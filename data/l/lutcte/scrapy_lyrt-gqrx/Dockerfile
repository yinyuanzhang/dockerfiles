FROM python:3.5

WORKDIR /scrapy_lyrt_gqrx

RUN pip install -v Scrapy==1.4.0
RUN pip install -v pymongo==3.5.0
RUN pip install -v Pillow==5.0.0
RUN pip install -v scrapyd==1.2.0
RUN pip install -v scrapyd-client==1.2.0a1

ADD . /scrapy_lyrt_gqrx

COPY ./scrapyd.conf /etc/scrapyd/

EXPOSE 6800

CMD scrapyd 