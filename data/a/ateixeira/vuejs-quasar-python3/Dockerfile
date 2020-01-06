#
# Vuejs + Quasar + Python3 With Backblaze B2 Storage
#

# Pick Our Base Image
FROM node:10.16.0-alpine

# ################################################################
# Install NPM Deps
# ################################################################

# Create Dir & Install Deps
RUN mkdir -p /app && \
set -xe && \
npm install -g vue@2.6.10 && \
npm install -g @vue/cli@3.8.4 && \ 
npm install -g @quasar/cli@1.0.0-rc.2 && \ 
npm install -g cordova@9.0.0 && \
npm install -g @cloudflare/wrangler@1.0.2 --unsafe-perm && \
apk add --no-cache python3 && \
pip3 install b2==1.4.0 cloudflare==2.3.0 && \
rm -rf /var/cache/apk/* /tmp/*

# Setup Workdir
WORKDIR /app
