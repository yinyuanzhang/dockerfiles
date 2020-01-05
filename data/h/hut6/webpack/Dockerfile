FROM node:9-alpine

# Needed to Ctrl-C when using --watch
RUN apk add --no-cache tini curl
ENTRYPOINT ["/sbin/tini", "--"]

WORKDIR /app

RUN npm install -g webpack@^4.0.0 webpack-cli
RUN npm install -g --unsafe-perm sass
#RUN npm install -g --unsafe-perm node-sass@4.9.1
RUN npm install -g typescript@~2.8 babel-loader @babel/core @babel/preset-env babel-preset-env ts-loader sass-loader style-loader css-loader postcss-loader autoprefixer resolve-url-loader file-loader url-loader html-webpack-plugin extract-text-webpack-plugin@^4.0.0-beta.0 clean-webpack-plugin webpack-manifest-plugin
RUN npm install -g webpack-dev-server
RUN npm install -g mini-css-extract-plugin
COPY ssl /etc/ssl

# global binary apps won't run without this
ENV NODE_PATH /usr/local/lib/node_modules

CMD ["webpack", "--color"]
