################################
# Build stage for the frontend #
################################
FROM node:12-alpine as BUILDER

RUN apk add openssh \
     && echo "root:UghDocker!" | chpasswd
     
COPY sshd_config /etc/ssh/
EXPOSE 80 2222

WORKDIR /usr/src/client
# Copy first package.json so changes in code dont require to reinstall all npm modules
COPY client/package.json client/package-lock.json ./
RUN npm i

COPY . /usr/src
RUN npm run build

# Added here to avoid an extra layer in the final stage
COPY Dockerfiles/server_config_docker.cfg /usr/src/server/server_config.cfg

###############
# Final stage #
###############
FROM python:3.6-slim

MAINTAINER Kruptein <info@darragh.dev>

EXPOSE 8000

WORKDIR /planarally

VOLUME /planarally/data
VOLUME /planarally/static/assets

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
# Copy first requirements.txt so changes in code dont require to reinstall python requirements
COPY --from=BUILDER /usr/src/server/requirements.txt .
RUN apt-get update && apt-get install dumb-init curl -y && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt
# Copy the final server files
COPY --from=BUILDER /usr/src/server/ .

CMD [ "python", "-u", "planarserver.py"]
