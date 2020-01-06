FROM docker:stable

RUN apk add --no-cache tree nodejs npm curl

RUN npm install -g surge 

RUN surge --version

WORKDIR /root

RUN touch .netrc

ADD .netrc ./
ADD update_netrc.sh ./ 
ADD healthcheck.sh ./
