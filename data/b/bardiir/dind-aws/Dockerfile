FROM docker:stable

RUN apk add -q --no-cache bash build-base ca-certificates curl git libffi-dev linux-headers make musl-dev openldap-dev openssh-client python py-pip rsync tzdata
RUN pip -q install pip==18.1
RUN pip -q install awscli boto3 PyYAML
