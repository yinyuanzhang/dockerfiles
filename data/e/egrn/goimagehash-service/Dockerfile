FROM golang:1.11.12-stretch as build

ENV CGO_ENABLED 0

RUN go get github.com/corona10/goimagehash \
&& go get github.com/gin-gonic/gin \
&& go get github.com/Egrn/goimagehash-service \
&& go build github.com/Egrn/goimagehash-service \
&& chmod +x goimagehash-service



FROM alpine:latest as production

MAINTAINER Egrn <3786931+Egrn@users.noreply.github.com>
LABEL version="latest"
LABEL description="HTTP REST API app like net service for performance image perceptual hashing.\
Service designed for image the comparison and searchig the same by it fingerprints. \
GOIMAGEHASH-SERVICE designed on Go and based on library to compute fingerprint of image by \
https://github.com/Corona10/goimagehash. GOIMAGEHASH-SERVICE supports main image formats JPG PNG GIF. \
It is able to compute fingerprints of three hash kinds: Average hash, Difference hash and Perception hash."

COPY --from=build /go/goimagehash-service /bin/goimagehash-service

ENV GIN_MODE release

CMD /bin/goimagehash-service --listen 0.0.0.0:8080
