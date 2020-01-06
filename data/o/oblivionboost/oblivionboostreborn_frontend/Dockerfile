
FROM node:12.9 as builder

WORKDIR /app

RUN npm install -g npm yarn

# try to make good use of docker cache: don't copy our source files until after install
# because there is no need to bust the "npm install" cache layer if only the app source files have changed
COPY package.json angular.json tsconfig.json tslint.json ./
# COPY .docker/rm.optional.deps.js ./.docker/rm.optional.deps.js

# before switching to non-root user, change ownership of home
# RUN chown -R node:node .
# USER node

# NB: this is a workaround due to the fact that npm '--no-optional' flag doesn't work (open script below for more)
# RUN node .docker/rm.optional.deps.js

RUN yarn install --no-cache --non-interactive --ignore-optional --link-duplicates --ignore-scripts

COPY projects/ob-portal-state ./projects/ob-portal-state

RUN yarn run setup-state
# COPY .docker/rm.optional.types.js ./.docker/rm.optional.types.js

# temporarily switch back to root user to fix ownership of the newly added files
# USER root
# RUN chown -R node:node src .docker/rm.optional.types.js
# USER node

# RUN node .docker/rm.optional.types.js
# RUN mkdir /app/dist

COPY projects ./projects/

RUN yarn run build

FROM nginx:1.17
COPY --from=builder /app/dist/ob-portal /var/www/dist
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
