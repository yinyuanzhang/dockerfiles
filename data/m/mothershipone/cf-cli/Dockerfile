FROM alpine
RUN apk add --no-cache curl
RUN curl -L "https://packages.cloudfoundry.org/stable?release=linux64-binary&source=github" | tar -zx
RUN mv cf /bin/cf
ENTRYPOINT ["sh"]
