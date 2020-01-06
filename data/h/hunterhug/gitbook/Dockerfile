FROM node:10.13.0

MAINTAINER hunterhug <gdccmcm14@live.com>

ARG VERSION=3.2.3

LABEL version=$VERSION

WORKDIR /srv/gitbook

RUN npm install  --global gitbook-cli
RUN gitbook install {VERSION}

COPY package.json /srv/gitbook/
RUN npm install  gitbook-plugin-advanced-emoji@^0.2.1
RUN npm install  gitbook-plugin-search-plus@^1.0.3
RUN npm install  gitbook-plugin-prism@^2.4.0
RUN npm install  gitbook-plugin-prism-themes@^0.0.2
RUN npm install  gitbook-plugin-simple-page-toc@^0.1.2
RUN npm install  gitbook-plugin-anchors@^0.7.1
RUN npm install  gitbook-plugin-anchor-navigation-ex@0.1.8
RUN npm install  gitbook-plugin-include-codeblock@^3.0.2
RUN npm install  gitbook-plugin-ace@^0.3.2
RUN npm install  gitbook-plugin-katex@^1.1.4
RUN npm install  gitbook-plugin-splitter@^0.0.8
RUN npm install  gitbook-plugin-tbfed-pagefooter@^0.0.1
RUN npm install  gitbook-plugin-sectionx@^3.1.0
RUN npm install  gitbook-plugin-local-video@^1.0.1
RUN npm install  gitbook-plugin-versions-select@^0.1.1
RUN npm install  gitbook-plugin-sharing-plus@^0.0.2
RUN npm install  gitbook-plugin-expandable-chapters-small@^0.1.7
RUN npm install  gitbook-plugin-toggle-chapters@^0.0.3
RUN npm install  gitbook-plugin-expandable-chapters@^0.2.0
RUN npm install  gitbook-plugin-disqus@^0.1.0
EXPOSE 4000 35729

CMD /usr/local/bin/gitbook serve