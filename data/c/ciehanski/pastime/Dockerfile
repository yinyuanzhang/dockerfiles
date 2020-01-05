FROM golang:1.11.1 AS builder
MAINTAINER Ryan Ciehanski "ryan@ciehanski.com"
ENV ENV "prod"
RUN mkdir /pastime && apt-get install git -y
WORKDIR /pastime
COPY . ./
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix nocgo -o pastimebin

FROM scratch
COPY --from=builder /pastime/pastimebin ./
COPY --from=builder /pastime ./
ENTRYPOINT ["./pastimebin"]