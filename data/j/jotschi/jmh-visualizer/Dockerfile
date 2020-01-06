FROM node:alpine as builder

RUN apk update && apk upgrade && \
    apk add --no-cache git
RUN git clone https://github.com/jzillmann/jmh-visualizer.git

WORKDIR jmh-visualizer
RUN npm install && npm run release

FROM nginx:1.15-alpine
COPY --from=builder /jmh-visualizer/build /usr/share/nginx/html
