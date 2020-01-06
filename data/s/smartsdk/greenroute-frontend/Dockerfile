### STAGE 1: Build ###

FROM node:6.14.4 as builder

RUN mkdir /ng-app
COPY package.json /ng-app/package.json
COPY package-lock.json /ng-app/package-lock.json

WORKDIR /ng-app
RUN cd /ng-app
RUN npm i

COPY . /ng-app

RUN $(npm bin)/ng build --env prod

### STAGE 2: Setup ###

FROM nginx:1.13.6-alpine
COPY --from=builder /ng-app/dist /usr/share/nginx/html
COPY start_front.sh /tmp
EXPOSE 80

# Override these two with the correct urls at runtime :)
ENV GR_BACKEND_URL "http://smartsdk-back:8080/back-sdk"
ENV GR_GRAFANA_URL "http://grafana-back:3000/dashboard/db/airquality-dashboard"
ENV GR_ALERTS_URL "http://alerts-back:8081/#"
ENV GR_ROUTINGMAP_URL "http://map-back:4200/"
ENV GR_DOMAIN_URL "greenroutesdk.com.mx"

CMD ["sh", "/tmp/start_front.sh"]
