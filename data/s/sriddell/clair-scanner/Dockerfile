FROM golang:1.11.2-alpine as builder

RUN apk --update add git
RUN go get -d github.com/sriddell/klar
RUN cd ./src/github.com/sriddell/klar && git checkout 1.1.0
RUN go build ./src/github.com/sriddell/klar

FROM python:3.7.1-alpine3.8

RUN apk add --no-cache python3 py-pip ca-certificates \
  && pip install virtualenv

WORKDIR /app

COPY . /app
RUN virtualenv -p python3 /env && /env/bin/pip install -r /app/requirements.txt
COPY --from=builder /go/klar /app/klar
RUN chmod +x /app/klar

EXPOSE 8080
CMD ["/env/bin/python", "-u", "/app/handler.py"]