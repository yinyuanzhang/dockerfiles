FROM python:3.7

MAINTAINER Haijun (Navy) Su <navysu@gmail.com>

RUN mkdir -p /storage/wwwroot
WORKDIR /storage/wwwroot

COPY requirements.txt /storage/wwwroot
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -u 2000 worker
USER worker

ENTRYPOINT  ["/storage/wwwroot/worker.sh"]
