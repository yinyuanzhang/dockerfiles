FROM golang:1.13.3-stretch

WORKDIR /qhn

COPY . .

RUN make

CMD ["var/quiet-hacker-news"]

EXPOSE 9090
