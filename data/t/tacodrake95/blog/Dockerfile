FROM alpine:latest

VOLUME /blog
RUN apk add --no-cache hugo ca-certificates
EXPOSE 1313
WORKDIR /blog
COPY . .
ENTRYPOINT ["hugo"]
CMD ["server", "--bind", "0.0.0.0"]
