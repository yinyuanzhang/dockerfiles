FROM maven:3.6.1-jdk-8

ARG ATLAS_VERSION=8.0.7
ARG BASE_URL=https://packages.atlassian.com/content/repositories/atlassian-public/com/atlassian/amps/atlassian-plugin-sdk/${ATLAS_VERSION}

RUN curl -fsSL -o /tmp/atlassian-plugin-sdk-${ATLAS_VERSION}.tar.gz ${BASE_URL}/atlassian-plugin-sdk-${ATLAS_VERSION}.tar.gz && \
    tar -xvzf /tmp/atlassian-plugin-sdk-${ATLAS_VERSION}.tar.gz -C /opt && \
    ln -s /opt/atlassian-plugin-sdk-${ATLAS_VERSION} /opt/atlassian-plugin-sdk

ENV PATH="/opt/atlassian-plugin-sdk/bin:${PATH}"

CMD ["atlas-version"]
