FROM node:8-alpine AS builder

COPY . .

RUN npm install
RUN npm run build

FROM nginxinc/nginx-unprivileged:stable-alpine
COPY --from=builder ./build /usr/share/nginx/html
