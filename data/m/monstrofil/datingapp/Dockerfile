FROM nginx:latest

RUN echo "/etc/nginx/modules/ngx_http_image_filter_module.so;" >> /etc/nginx/nginx.conf

ADD conf/default.conf /etc/nginx/conf.d/default.conf
ADD conf/nginx.conf /etc/nginx/nginx.conf
