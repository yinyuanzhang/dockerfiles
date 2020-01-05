FROM alpine:3.10
LABEL description="GitLab-CI Terraform" \
      maintainer="Djerfy <djerfy@gmail.com>"

ENV TERRAFORM_VERSION=0.12.18
ENV TERRAFORM_FILENAME=terraform_${TERRAFORM_VERSION}_linux_amd64.zip
ENV TERRAFORM_BASEURL=https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}

RUN apk add -U git bash wget
RUN wget -q ${TERRAFORM_BASEURL}/${TERRAFORM_FILENAME} && \
    wget -qO- ${TERRAFORM_BASEURL}/terraform_${TERRAFORM_VERSION}_SHA256SUMS | grep "terraform_${TERRAFORM_VERSION}_linux_amd64.zip" | awk '{print $1}' > ${TERRAFORM_FILENAME}.sha256sum
RUN echo "$(cat ${TERRAFORM_FILENAME}.sha256sum)  ${TERRAFORM_FILENAME}" | sha256sum -c && \
    unzip ${TERRAFORM_FILENAME} -d /bin && \
    rm -f ${TERRAFORM_FILENAME}

CMD ["/bin/terraform", "--version"]
