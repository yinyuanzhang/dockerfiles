FROM jjmerelo/perl6-doccer:latest
LABEL version="1.1" maintainer="JJ Merelo <jjmerelo@GMail.com>"

RUN apk update && apk upgrade && apk add git openssh-client python jq bash

# Will run this
ENTRYPOINT P6_DOC_TEST_VERBOSE=1 prove -e perl6 t

# Repeating mother's env
ENV PATH="/root/.rakudobrew/bin:${PATH}"

