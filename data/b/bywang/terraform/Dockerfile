FROM alpine
ENV TF_VERSION=0.12.12
ENV TFLINT_VERSION=0.12.1
RUN apk update && apk add --no-cache --virtual .build-deps wget
WORKDIR /app
RUN wget https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip -q -O terraform.zip
RUN wget https://github.com/wata727/tflint/releases/download/v${TFLINT_VERSION}/tflint_linux_amd64.zip -q -O tflint.zip
RUN unzip terraform.zip -d /usr/local/bin/ && \
    unzip tflint.zip -d /usr/local/bin/ && \
    rm -rf terraform.zip tflint.zip
RUN apk del .build-deps
CMD [ "terraform", "-v"]