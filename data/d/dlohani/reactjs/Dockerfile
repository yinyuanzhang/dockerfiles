FROM node:10
LABEL maintainer="dlohani48@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive \
    CREATE_REACT_APP_VERSION=2.1.1 \
    # Fix for the issue with Selenium, as described here:
    # https://github.com/SeleniumHQ/docker-selenium/issues/87
    DBUS_SESSION_BUS_ADDRESS=/dev/null

# Install basics
RUN apt-get update &&  \
    apt-get install -y git wget curl unzip build-essential && \
    curl -sS http://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update &&  \
    apt-get install yarn -y --no-install-recommends && \
    mkdir app && \
    mkdir -p /root/.cache/yarn/

RUN yarn global add create-react-app@"$REACT_NATIVE_CLI_VERSION"

COPY ./entrypoint.sh /

WORKDIR /app
EXPOSE 3000
ENTRYPOINT ["/entrypoint.sh"]
CMD ["yarn", "start"]