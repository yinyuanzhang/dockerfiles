FROM n4nn31355/ubuntu:customuser

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends git npm nodejs-legacy build-essential libxext-dev libxtst-dev libxkbfile-dev libgtk2.0-0 libxss1 libgconf-2-4 libnss3 libasound2 && \
    rm -rf /var/lib/apt/lists/*

USER $CUSTOMUSER

ENV HOME $HOME
ENV DISPLAY :0
WORKDIR $HOME

RUN git clone https://github.com/zulip/zulip-electron
WORKDIR $HOME/zulip-electron
RUN npm install

ENTRYPOINT ["npm", "start"]
