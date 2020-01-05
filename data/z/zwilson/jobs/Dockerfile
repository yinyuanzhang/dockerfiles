FROM python:3.6

WORKDIR /usr/src
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
  pip install --no-cache-dir -r requirements.txt
COPY ./configs/app/scrapyd.conf .
COPY ./configs/app/scrapy.cfg .
COPY  ./app ./app
CMD ["scrapyd-deploy"]
