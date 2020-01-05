FROM jwilder/nginx-proxy
MAINTAINER Gavin Jones <gjones@powerfarming.co.nz>
RUN { \
      echo 'server_tokens off;'; \
      echo 'client_max_body_size 500m;'; \
    } > /etc/nginx/conf.d/publicweb_proxy.conf

#Reference commit id
ARG COMMIT_ID
RUN         echo $COMMIT_ID >> commitid.txt
