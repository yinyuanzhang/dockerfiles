FROM python:3.7.3

LABEL maintainer="mabeple <cymapu@gmail.com>"

WORKDIR /srv/docker/scrapy

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["scrapy", "crawl", "qzone_spider"]
