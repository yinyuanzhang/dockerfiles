# Build
FROM node:alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Production
FROM nginx:alpine as production
COPY --from=build /app/dist /usr/share/nginx/html
COPY --from=build /app/build/niller.xyz.conf /etc/nginx/conf.d/default.conf
LABEL traefik.enable="true"
LABEL traefik.frontend.redirect.entryPoint="https"
LABEL traefik.frontend.redirect.regex="^https?://niller.xyz/(.*)"
LABEL traefik.frontend.redirect.replacement="https://www.niller.xyz/$$1"
LABEL traefik.frontend.rule="Host:www.niller.xyz,niller.xyz"
LABEL traefik.port="80"
EXPOSE 80
