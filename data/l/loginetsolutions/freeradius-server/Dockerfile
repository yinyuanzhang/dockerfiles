
FROM freeradius/freeradius-server:latest-alpine
COPY radius/server/raddb/ /etc/raddb

# Build Args
ARG APP_NAME=freeradius-server
ARG DB_DIR=/${APP_NAME}/db

RUN mkdir -p ${DB_DIR}

# Declare volumes to mount
VOLUME ["/freeradius-server/db"]

