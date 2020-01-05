FROM nginx:alpine

ENTRYPOINT ["/bin/entrypoint.sh"]
EXPOSE 80 443

ADD entrypoint.sh /bin/entrypoint.sh
RUN rm -v /etc/nginx/conf.d/*.conf

RUN apk add --update unzip && rm -rf /var/cache/apk/*
ADD https://releases.hashicorp.com/consul-template/0.15.0/consul-template_0.15.0_linux_amd64.zip /usr/bin/consul-template.zip
RUN unzip /usr/bin/consul-template.zip -d /usr/bin/
