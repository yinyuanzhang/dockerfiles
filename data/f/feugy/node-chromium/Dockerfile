# https://github.com/DevExpress/testcafe-browser-provider-saucelabs/issues/17
FROM frolvlad/alpine-glibc

# Install chromium to run tests, 
RUN apk --update --no-cache add chromium \
  # for test code (do not run on latest (12) either: node-canvas fails to build)
  nodejs=10.16.0-r0 npm=10.16.0-r0

# to build node-canvas 
RUN apk --update --no-cache add --virtual build-dependencies \
  build-base python g++ cairo-dev jpeg-dev pango-dev bash imagemagick

ENTRYPOINT ["/bin/sh"]
