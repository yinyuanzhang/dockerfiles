FROM docker

LABEL maintainer_name="Roi Avidan"
LABEL maintainer_email="roiavidan@gmail.com"

RUN apk --no-cache add make curl ca-certificates openssh bash git py-pip jq gzip
RUN pip install --upgrade pip docker-compose awscli
