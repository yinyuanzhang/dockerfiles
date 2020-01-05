FROM docker:19-dind
RUN apk -v --update add python3 py3-cryptography rsync jq wget unzip zip bash git make
RUN pip3 install --no-cache-dir --upgrade pip && pip3 install --no-cache-dir --upgrade awscli s3cmd aws-encryption-sdk-cli
