FROM golang:1.8

WORKDIR /go/src/app
COPY . .

RUN go get github.com/namsral/flag
RUN go get github.com/imkira/gcp-iap-auth

RUN go install

#ENV GCP_IAP_AUTH_LISTEN_ADDR=0.0.0.0
#ENV GCP_IAP_AUTH_LISTEN_PORT=80
#ENV GCP_IAP_AUTH_AUDIENCES=YOUR_AUDIENCE
#ENV GCP_IAP_AUTH_PUBLIC_KEYS=/path/to/public_keys_file
#ENV GCP_IAP_AUTH_TLS_CERT=/path/to/tls_cert_file
#ENV GCP_IAP_AUTH_TLS_KEY=/path/to/tls_key_file

EXPOSE 80 443

CMD ["gcp-iap-auth"]
