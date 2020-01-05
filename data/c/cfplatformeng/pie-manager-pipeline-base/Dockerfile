FROM alpine:latest
RUN apk add curl && apk add git
RUN wget https://github.com/pivotal-cf/om/releases/download/4.2.1/om-linux-4.2.1 && mv om-linux-4.2.1 /usr/local/bin/om && chmod +x /usr/local/bin/om 
