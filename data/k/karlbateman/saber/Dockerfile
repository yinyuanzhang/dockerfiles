FROM golang AS golang
WORKDIR /usr/local/go/src/github.com/karlbateman/saber
COPY . ./
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix nocgo -o /saber .
# We need a regular DNS server to resolve the HTTPS api
RUN echo "1.1.1.1" > /resolv.conf

FROM scratch
COPY --from=golang /saber /
COPY --from=golang /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=golang /resolv.conf /etc/resolv.conf
EXPOSE 53
ENTRYPOINT ["/saber"]
CMD ["-host", "0.0.0.0", "-port", "53"]
