# build stage
FROM golang:1.13-alpine AS builder

# RUN wget -O dep https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-amd64
# RUN mv dep /usr/bin/dep
# RUN chmod +x /usr/bin/dep

WORKDIR /go/src/sapic

# Copy only vendor files
COPY go.mod go.sum ./
RUN go mod download

# Copy and build everything else
COPY . .
COPY conf.example.json conf.json
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags "-s -w" -a -installsuffix cgo -o sapic-go

FROM alpine:latest
RUN apk --no-cache add ca-certificates

WORKDIR /root/

COPY --from=builder /go/src/sapic/sapic-go /go/src/sapic/conf.json /go/src/sapic/bg.json ./
ENTRYPOINT ["./sapic-go"]
