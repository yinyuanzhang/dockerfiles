FROM openjdk:8-jre-alpine
#Add necessary packages to default image
RUN apk add --no-cache bash nano curl
ARG ACLI=atlassian-cli-9.1.0
ADD https://marketplace.atlassian.com/download/plugins/org.swift.atlassian.cli/version/9100  /opt/${ACLI}.zip
RUN unzip /opt/${ACLI}.zip -d /opt
RUN rm /opt/${ACLI}.zip
ENV PATH="/opt/${ACLI}:${PATH}"
WORKDIR /opt/${ACLI}
