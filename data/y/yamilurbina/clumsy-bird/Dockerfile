FROM node:lts-slim AS builder
WORKDIR /app
COPY . .
RUN npm install -g grunt-cli && npm install && grunt

FROM nginx:1.16.0-alpine
COPY --from=builder /app/ /usr/share/nginx/html/
