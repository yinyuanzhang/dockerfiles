FROM mongo

RUN apt update && apt install -y python python-pip && pip install awscli

COPY entrypoint.sh /

RUN chmod a+x /entrypoint.sh && mkdir /backup

ENTRYPOINT /entrypoint.sh