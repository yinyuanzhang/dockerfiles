FROM golang:1.12.4 as build
WORKDIR /build
ADD go.mod /build/go.mod
ADD go.sum /build/go.sum
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app

FROM alpine:latest as app
COPY ./pb/health/health.swagger.json /swagger.json
COPY ./third_party/swagger-ui /swagger-ui
COPY --from=build /build/app /app
ENTRYPOINT [ "/app" ]
