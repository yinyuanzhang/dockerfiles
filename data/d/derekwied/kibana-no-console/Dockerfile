
FROM centos:7
LABEL maintainer "Cailen <cailen@me.com>"
EXPOSE 5601

ARG PHANTOM_JS_VERSION
ENV PHANTOM_JS_VERSION ${PHANTOM_JS_VERSION:-2.1.1-linux-x86_64}

# Add Reporting dependencies.
RUN yum update -y && yum install -y fontconfig freetype nodejs bzip2 && yum clean all

RUN mkdir /tmp/phantomjs \
    && curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOM_JS_VERSION}.tar.bz2 \
    | tar -xj --strip-components=1 -C /tmp/phantomjs \
    && mv /tmp/phantomjs/bin/phantomjs /usr/local/bin

WORKDIR /usr/share/kibana
RUN curl -Ls https://artifacts.elastic.co/downloads/kibana/kibana-6.2.4-linux-x86_64.tar.gz | tar --strip-components=1 -zxf - && \
    ln -s /usr/share/kibana /opt/kibana

ENV PATH=/usr/share/kibana/bin:$PATH
ENV ELASTIC_CONTAINER=true \
    CONSOLE_ENABLED=false \
    XPACK_APM_ENABLED=false \
    XPACK_ML_ENABLED=false \
    XPACK_GRAPH_ENABLED=false \
    XPACK_GROKDEBUGGER_ENABLED=false \
    XPACK_SECURITY_ENABLED=false

# Set some Kibana configuration defaults.
COPY config/kibana.yml /usr/share/kibana/config/kibana.yml

# Add the launcher/wrapper script. It knows how to interpret environment
# variables and translate them to Kibana CLI options.
COPY bin/kibana-docker /usr/local/bin/

# Provide a non-root user to run the process.
RUN groupadd --gid 1000 kibana && \
    useradd --uid 1000 --gid 1000 \
    --home-dir /usr/share/kibana --no-create-home \
    kibana
USER kibana

RUN kibana-plugin install x-pack
RUN kibana-plugin install https://github.com/sirensolutions/sentinl/releases/download/tag-6.2.3-3/sentinl-v6.2.4.zip


CMD ["/bin/bash", "/usr/local/bin/kibana-docker"]
