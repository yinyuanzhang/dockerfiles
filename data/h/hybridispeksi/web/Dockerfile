FROM keymetrics/pm2:latest-alpine

WORKDIR /var/www/

# Install deps
COPY ./package* ./
COPY . .
COPY webpack webpack/
# COPY dist dist/
COPY assets src/assets
COPY ecosystem.config.js .
RUN npm install --production
RUN npm install -g pm2


RUN npm run build
CMD ["pm2-runtime", "start", "ecosystem.config.js"]
