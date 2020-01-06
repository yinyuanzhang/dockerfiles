FROM nginx:alpine
LABEL maintainer="Christoph Linse"
LABEL description="This is the docker image for the cm_front side of the cm"

COPY source/nginx/cm-site /etc/nginx/sites-available/
COPY source/nginx/default.conf /etc/nginx/conf.d/
COPY source/nginx/nginx.conf /etc/nginx/nginx.conf
COPY source/ /opt/cm_back

WORKDIR /opt/cm_back

RUN mkdir -p /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/cm-site  /etc/nginx/sites-enabled/cm-site

RUN apk add --update nodejs npm
RUN npm install -g @angular/cli
RUN ng build --prod --outputPath=/var/www/html
RUN rm -rf /opt/cm_back






