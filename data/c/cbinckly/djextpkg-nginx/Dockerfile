FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf

WORKDIR /usr/share/nginx/html

COPY *.html /usr/share/nginx/html/
COPY sitemap.xml /usr/share/nginx/html/
COPY robots.txt /usr/share/nginx/html/
COPY static/ /usr/share/nginx/html/static/
COPY packages/ /usr/share/nginx/html/packages/

CMD ["nginx", "-g", "daemon off;"]
