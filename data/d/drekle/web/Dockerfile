FROM golang:latest AS build
WORKDIR /build
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=arm go build -a -installsuffix cgo -o web .

FROM scratch
WORKDIR /
COPY --from=build /build/web /
COPY http/* /
EXPOSE 80
ENTRYPOINT ["/web"]