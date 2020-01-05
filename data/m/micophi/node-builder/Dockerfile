FROM ubuntu:latest

# Replace the shell with bash for easier path sourcing
SHELL ["/bin/bash", "-c", "-l"]

RUN apt-get update
RUN apt-get install -y htop build-essential chromium-browser chromium-chromedriver maven curl git

ENV CHROME_BIN=/usr/bin/chromium-browser

RUN useradd --create-home --shell /bin/bash user
COPY --chown=user:user install-nvm.sh /home/user/install-nvm.sh

USER user
WORKDIR /home/user

RUN ./install-nvm.sh
RUN rm install-nvm.sh

RUN nvm install --lts; \
    nvm use --lts;

RUN npm install -g node-sass

CMD [ "node" ]
