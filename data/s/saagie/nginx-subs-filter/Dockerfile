FROM nginx:1.16.1

RUN apt-get update && \
    apt-get install -y curl gnupg2 ca-certificates lsb-release git gcc libpcre3 libpcre3-dev zlib1g zlib1g-dev build-essential

RUN echo "deb http://nginx.org/packages/debian `lsb_release -cs` nginx" \
    | tee /etc/apt/sources.list.d/nginx.list

RUN curl -fsSL https://nginx.org/keys/nginx_signing.key | apt-key add -

WORKDIR /tmp

RUN git clone git://github.com/yaoweibin/ngx_http_substitutions_filter_module.git

RUN curl https://nginx.org/download/nginx-1.16.1.tar.gz -o nginx-1.16.1.tar.gz && \
    tar -xzvf nginx-1.16.1.tar.gz

RUN cd nginx-1.16.1 && ./configure --with-compat --add-dynamic-module=../ngx_http_substitutions_filter_module && make modules

FROM nginx:1.16.1

COPY --from=0 /tmp/nginx-1.16.1/objs/ngx_http_subs_filter_module.so /etc/nginx/modules/



