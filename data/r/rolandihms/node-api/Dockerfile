FROM node:8-alpine
LABEL maintainer="Roland Ihms roland@ihmsmedia.com>"

#Install core deps
RUN set -xe \
    && apk add --no-cache bash git

ARG CACHEBUST=1

ADD https://fa109fcdb5dfa3e3700ce781870512702d6815a6:x-oauth-basic@api.github.com/repos/rolandihms/node-api/compare/master...HEAD /dev/null

# Clone our private GitHub Repository
RUN git clone -b master https://943088905e8ab81cff9f1a900b63a2a057086cf3:x-oauth-basic@github.com/rolandihms/node-api.git /home/app/

WORKDIR /home/app

# Install pm2
RUN npm install pm2@3.5.1 -g && \
    npm install -g


RUN chmod -R 0777 /home/app

# Expose ports needed to use Keymetrics.io
# EXPOSE 3000

#HealthCheck
HEALTHCHECK --interval=10s --timeout=10s --start-period=15s \  
    CMD node /home/app/healthcheck.js

# Start pm2.json process file
CMD pm2 start --no-daemon  processes.json