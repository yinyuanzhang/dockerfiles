FROM alpine:3.6
MAINTAINER shkawan@microsoft.com

RUN apk update && apk add tzdata py-pip dcron
ENV TZ Asia/Tokyo

COPY check.py ./
COPY entry.sh ./
COPY requirements.txt ./
COPY root /etc/crontabs/root
RUN pip install -r requirements.txt

CMD ["./entry.sh"]
