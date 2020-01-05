FROM node:12-alpine AS builder

ADD package*.json ./
RUN npm ci
ADD . ./

RUN npm run build

FROM pierrezemb/gostatic

COPY --from=builder index.html /srv/http/index.html
COPY --from=builder static /srv/http/static
