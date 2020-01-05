FROM alpine

MAINTAINER kukam "kukam@freebox.cz"

RUN apk --update --no-cache add bash nginx \
    && mkdir /run/nginx \
    && rm -fr /var/cache/apk/*

    #&& mkdir -p /PWE/webapps/myproject \
    
COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
