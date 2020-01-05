FROM deshboard/go:1.7

RUN mkdir -p /go/src/app
WORKDIR /go/src/app

# this will ideally be built by the ONBUILD below ;)
CMD ["go-wrapper", "run"]

ONBUILD COPY glide.yaml glide.lock /go/src/app/
ONBUILD RUN glide install

ONBUILD COPY . /go/src/app
ONBUILD RUN go-wrapper install
