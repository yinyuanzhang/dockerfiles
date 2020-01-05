# Build stage
FROM golang AS build-stage
ENV GO111MODULE on
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -ldflags="-w -s" -o app .

# Scratch stage
FROM scratch

COPY --from=build-stage /app/app /app/app
EXPOSE 80
ENTRYPOINT ["/app/app"]