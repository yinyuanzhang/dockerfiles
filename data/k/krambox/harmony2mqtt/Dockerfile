
 
#
# ---- Dependencies ----
FROM mhart/alpine-node:8 AS dependencies
WORKDIR /root/app
COPY package.json .
COPY package-lock.json .
RUN apk add --no-cache  python build-base git
# install node packages
RUN npm set progress=false && npm config set depth 0
RUN npm install --only=production 
# copy production node_modules aside
RUN cp -R node_modules prod_node_modules

#
# ---- Release ----
FROM mhart/alpine-node:base-8
WORKDIR /root/app
# copy production node_modules
COPY --from=dependencies /root/app/prod_node_modules ./node_modules
# copy app sources
COPY package.json .
COPY config.js .
COPY index.js .
CMD ./index.js 