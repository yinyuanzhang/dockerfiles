#
# DESCRIPTION: A cloudcmd image for raspberry pi (based on arm32v7/node).  
# 
FROM arm32v7/node:latest
LABEL maintainer="joeychen"

COPY qemu-arm-static /usr/bin/

ENV NODE_ENV=production

# To handle 'not get uid/gid'
RUN npm config set unsafe-perm true

# npm WARN tarball tarball data for edward
RUN npm i edward -g

RUN npm i cloudcmd -g

EXPOSE 8000

ENTRYPOINT ["cloudcmd"]

