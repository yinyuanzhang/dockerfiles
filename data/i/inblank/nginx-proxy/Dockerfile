FROM nginx:stable-alpine
RUN echo "server {" > /etc/nginx/conf.d/site.conf \
    && echo "   listen 80;" >> /etc/nginx/conf.d/site.conf \
    && echo "   server_name www.develop.dev develop.dev;" >> /etc/nginx/conf.d/site.conf \
    && echo "   location / {" >> /etc/nginx/conf.d/site.conf \
    && echo "       proxy_pass http://apache:80;" >> /etc/nginx/conf.d/site.conf \
    && echo "   }" >> /etc/nginx/conf.d/site.conf \
    && echo "   location ~* \.(html|jpeg|jpg|gif|png|css|js|pdf|txt|tar|ico)$ {" >> /etc/nginx/conf.d/site.conf \
    && echo "       root /usr/share/nginx/html;" >> /etc/nginx/conf.d/site.conf \
    && echo "       expires 1h;" >> /etc/nginx/conf.d/site.conf \
    && echo "   }" >> /etc/nginx/conf.d/site.conf \
    && echo "}" >> /etc/nginx/conf.d/site.conf \
    && echo "proxy_redirect              off;" > /etc/nginx/conf.d/proxy.conf \
    && echo "proxy_set_header            Host \$host;" >> /etc/nginx/conf.d/proxy.conf \
    && echo "proxy_set_header            X-Real-IP \$remote_addr;" >> /etc/nginx/conf.d/proxy.conf \
    && echo "proxy_set_header            X-Forwarded-For \$proxy_add_x_forwarded_for;" >> /etc/nginx/conf.d/proxy.conf