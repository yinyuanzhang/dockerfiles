# FROM geircode/vscode-plugin-workspace-filecontainer:latest as filecontainer

# FROM node:13.4.0-buster
FROM geircode/vscode-plugin-workspace-nodejs

WORKDIR /app
COPY . /app

# RUN pip install -r requirements.txt 

# RUN apt-get update
# RUN apt-get install -y jq

# RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.03.1-ce.tgz && tar --strip-components=1 -xvzf docker-17.03.1-ce.tgz -C /usr/local/bin

# WORKDIR /files
# COPY --from=filecontainer /files .
# RUN tar --strip-components=1 -xvzf docker-ce.tgz -C /usr/local/bin
# RUN rm *

# RUN npm install -g yo bower grunt-cli gulp; \
#   npm install -g generator-webapp generator-angular

# RUN npm install --global yo

RUN adduser --disabled-password --gecos "" yeoman; \
  echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

ENTRYPOINT tail -f /dev/null
