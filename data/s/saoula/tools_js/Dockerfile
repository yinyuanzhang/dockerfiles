FROM node:9.2-alpine
MAINTAINER Michel Saoula <michel@saoula.com>
LABEL com.saoula.toolsjs.name="JS Dev Tools"
LABEL com.saoula.toolsjs.description="set of js tools, task runners, package managers for software development purposes, i.e: yeoman, plop, bower, grunt, gulp..."
LABEL com.saoula.toolsjs.maintainer "michel@saoula.com"
LABEL com.saoula.toolsjs.node="9.2.X"

# install GIT
RUN apk --no-cache add git curl tar yarn

# npm install yo and the generators
RUN yarn global add yo \
		bower \
		grunt-cli \
		gulp \
    plop \
    generator-webapp \
    generator-generator \
    generator-fountain-webapp

USER node
WORKDIR /home/node
ENV HOME /home/node

# remove yeoman request for anonymous analytics on the first launch
RUN mkdir -p ${HOME}/.config/configstore && echo '{ "optOut": false }' >> ${HOME}/.config/configstore/insight-yo.json

CMD ["node"]