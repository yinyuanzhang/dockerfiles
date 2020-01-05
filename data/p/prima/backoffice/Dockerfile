FROM prima/nginx:1.12.2-3

# aws cli
RUN apk -Uuv add python py-pip curl zip rsync && \
  	pip install --upgrade pip && \
  	pip install awscli && \
    aws configure set s3.signature_version s3v4 && \
  	apk --purge -v del py-pip && \
  	rm -rf /var/cache/apk/* && \
    mkdir /code && \
    rm -f /etc/nginx/conf.d/*

COPY files/bo.conf /etc/nginx/conf.d/bo.conf
COPY files/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]
