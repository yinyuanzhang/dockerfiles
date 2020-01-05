FROM hashicorp/terraform:0.11.14
FROM debian

COPY --from=0 /bin/terraform /bin/terraform

RUN apt-get -y update && \
    apt-get -y install git openssh-client awscli && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["terraform"] 