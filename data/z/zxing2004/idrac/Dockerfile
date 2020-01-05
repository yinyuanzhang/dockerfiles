FROM nginx:1.16.1

# RUN mkdir -p /etc/nginx/ssl/ && \
#     apt update && \
#     apt install -y openssl net-tools vim lsof curl telnet && \
#     sed -i 's/CipherString = DEFAULT@SECLEVEL=2/CipherString = DEFAULT@SECLEVEL=1/' /etc/ssl/openssl.cnf
# COPY nginx.conf /etc/nginx/nginx.conf
# COPY ssl/ /etc/nginx/ssl/

COPY conf.d/ /etc/nginx/conf.d/