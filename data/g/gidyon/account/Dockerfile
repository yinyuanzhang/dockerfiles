FROM alpine
LABEL maintainer="gideonhacer@gmail.com"
RUN apk update && \
   apk add ca-certificates && \
   update-ca-certificates && \
   rm -rf /var/cache/apk/*
WORKDIR /app
COPY server .
COPY static static
COPY templates templates
COPY api api
EXPOSE 80
ENTRYPOINT [ "/app/server" ]