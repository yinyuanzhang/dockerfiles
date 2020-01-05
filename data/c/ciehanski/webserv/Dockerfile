FROM nginx:alpine
MAINTAINER Ryan Ciehanski "ryan@ciehanski.com"
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && rm -v /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY public_html /usr/share/nginx/html/
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
