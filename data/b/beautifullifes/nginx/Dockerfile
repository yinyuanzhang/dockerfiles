FROM tangchen2018/nginx:1.6.2-centos7

RUN rm -rf /usr/local/nginx/conf/nginx.conf /usr/local/nginx/conf/conf.d 
COPY ./nginx.conf /usr/local/nginx/conf/
COPY ./vhost /usr/local/nginx/conf/vhost

CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]
