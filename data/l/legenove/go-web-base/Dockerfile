FROM legenove/amazonlinux-go-1-11:v0.06

WORKDIR /go/src/app

COPY go/web1.11/glide.lock ./
COPY go/web1.11/glide.yaml ./
RUN glide install
RUN rm -rf ./*

CMD ["go", "run", "main.go"]