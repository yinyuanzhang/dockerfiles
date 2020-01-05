FROM alpine

RUN apk add -U nginx
RUN apk add curl
RUN apk add bash
#RUN echo 'alex for president' > /usr/share/nginx/html/index.html

ADD start.sh /bin/
CMD /bin/start.sh
#CMD nginx -g "daemon off;"
