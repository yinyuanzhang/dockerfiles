FROM alpine:3.8

# Build arguments.
ARG VCS_REF
ARG BUILD_DATE

# Labels / Metadata.
LABEL maintainer="James Brink, brink.james@gmail.com" \
    decription="Logo Generator" \
    version="1.0.0" \
    org.label-schema.name="logo-generator" \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-url="https://github.com/jamesbrink/logo-generator/" \
    org.label-schema.schema-version="1.0.0-rc1"

# Create our group & user.
RUN addgroup -g 1000 -S logo \
    && adduser -u 1000 -S -h /logo -s /bin/sh -G logo logo

# Set our working directory.
WORKDIR /logo

# Copy our entrypoint into the container.
COPY ./ /logo

# Install deps.
RUN set -xe; \
    apk --update add --no-cache --virtual .runtime-deps \
        bash \
        cairo \
        libjpeg \
        nodejs \
        npm \
        pango; \
    apk add --no-cache --virtual .build-deps \
        alpine-sdk \
        jpeg-dev \
        pango-dev \
        python; \
    npm i; \
    chown -R logo:logo /logo;

# Setup our environment variables.
ENV PATH="/usr/local/bin:$PATH"

# Drop down to our unprivileged user.
USER logo

# Expose our HTTP port.
EXPOSE 8080

# Set the entrypoint.
ENTRYPOINT ["/usr/bin/npm"]

# Set the default command
CMD ["start"]

