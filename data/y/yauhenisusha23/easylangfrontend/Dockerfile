FROM nginx:1.16.1-alpine

WORKDIR /etc
COPY docker/nginx.conf nginx/

WORKDIR /var/www/context-tutor
COPY . /var/www/context-tutor/
RUN apk add npm && yes | npm i ionic -g && npm i && \
    sed -i 's|https://easy4learn.com|http://localhost:3000|g' src/environments/environment.prod.ts && \
    ionic build --prod && \
    cd .. && \
    rm -rf html && \
    mkdir html && \
    cp -r context-tutor/www/* html && \
    rm -rf context-tutor

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]