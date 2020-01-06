FROM alpine:3.10
LABEL maintainer="Antiarchitect <voronkovaa@gmail.com>"

RUN apk add --no-cache postgresql-client

CMD ["/bin/sh", "-c", "while sleep 60; do echo 'Hi...'; done"]
