FROM alexsuch/angular-cli:1.7

RUN apk --update add git bash openssh

WORKDIR /project

ADD . .

RUN npm i
RUN npm run build

FROM jonnybgod/alpine-nginx:master

WORKDIR /src

COPY --from=0 /project/dist/app/ .
ADD ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443

ENTRYPOINT ["nginx"]
