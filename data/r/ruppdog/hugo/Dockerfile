FROM ruppdog/base:0.0.1

# Install Java
RUN apk --update add openjdk8-jre

# Install Hugo
ENV HUGO_VERSION 0.16
RUN \
    wget https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_linux-64bit.tgz && \
    tar -C /usr/sbin -xzvf hugo_${HUGO_VERSION}_linux-64bit.tgz && \
    rm hugo_${HUGO_VERSION}_linux-64bit.tgz

# Copy templates
COPY templates /app/templates

# Set up entrypoint
ADD entrypoint.sh /sbin/entrypoint.sh
ENTRYPOINT ["/sbin/entrypoint.sh"]

# Run command
CMD [ "hugo", "server", "--bind=0.0.0.0" ]
