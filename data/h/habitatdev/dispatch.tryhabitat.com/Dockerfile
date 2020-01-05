FROM node:8.6.0 as staticassets

RUN mkdir /app
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
ENV API_ROOT https://api_root.habitat.com
RUN npm run heroku-postbuild

# ================================================================================
# Add files to nginx alpine

FROM nginx:1.15.0-alpine

COPY --from=staticassets /app/server/index.html /usr/share/nginx/html/index.html
COPY --from=staticassets /app/public/ /usr/share/nginx/html
COPY --from=staticassets /app/dockup /dockup
COPY --from=staticassets /app/dockup/default.conf /etc/nginx/conf.d/default.conf

CMD /dockup/run-nginx
