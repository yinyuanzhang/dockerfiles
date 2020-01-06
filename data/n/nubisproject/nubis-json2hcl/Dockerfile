FROM alpine:3.6
LABEL maintainer="Ed Lim <limed@mozilla.com>"

ENV Json2HclVersion=0.0.6

# Install build dependencies
#+ Cleanup apk cache files
RUN apk add --no-cache --virtual .build-dependencies \
    curl \
    && rm -f /var/cache/apk/APKINDEX.*

RUN [ "/bin/ash", "-c", "set -o pipefail \
    && curl -L --silent --show-error -o /usr/local/bin/json2hcl https://github.com/kvz/json2hcl/releases/download/v${Json2HclVersion}/json2hcl_v${Json2HclVersion}_linux_amd64 \
    && chmod +x /usr/local/bin/json2hcl" ]

# Remove build dependencies
RUN apk del .build-dependencies

ENTRYPOINT [ "/usr/local/bin/json2hcl" ]
