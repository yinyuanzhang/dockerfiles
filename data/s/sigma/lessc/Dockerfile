FROM node:9.6.1-alpine
LABEL maintainer="yann.hodique@gmail.com"

RUN yarn global add less@2.7.3 less-plugin-clean-css

ENTRYPOINT ["/usr/local/bin/lessc"]
