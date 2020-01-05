FROM hashicorp/terraform:light
FROM vault:latest
FROM hashicorp/packer:light
FROM alpine:latest

COPY --from=0 /bin/terraform /bin/terraform
COPY --from=1 /bin/vault /bin/vault
COPY --from=2 /bin/packer /bin/packer

RUN apk --no-cache add git
