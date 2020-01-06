FROM node:6.9

RUN npm install pm2 -g
RUN pm2 install pm2-server-monit

# Create app directory
RUN mkdir -p /var/apps
WORKDIR /var/apps/

CMD ["pm2-docker", "apps.json"]