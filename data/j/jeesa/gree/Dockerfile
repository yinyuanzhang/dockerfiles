FROM homeassistant/amd64-base:latest

ENV LANG C.UTF-8

RUN apk add --no-cache jq nodejs nodejs-npm && \
npm set unsafe-perm true 

# Copy options.json to /opt

COPY ./options.json /opt/options.json

# Copy data for add-on
WORKDIR /usr/src/app
COPY . .
RUN chmod +x run.sh

VOLUME /data/

CMD [ "./run.sh" ]
