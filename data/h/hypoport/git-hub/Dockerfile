FROM debian:stable-slim

RUN apt update \
    && apt install -y git curl \
    && git version \
    && apt-get clean autoclean \
    && apt-get autoremove --yes \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/

#RUN apt update \
#    && apt install -y hub \
#    && hub version
# TODO cleanup apt-cache

RUN mkdir -p /hub && \
    cd /hub \
    && curl -L -o hub.tgz $(curl -s https://api.github.com/repos/github/hub/releases/latest | grep -o "http.*hub-linux-amd64*.*tgz") \
    && tar xfz hub.tgz \
    && HUB_VERSION=$(tar tfz hub.tgz | head -n1 | cut -f1 -d"/") \
    && echo "installing latest $HUB_VERSION" \
    && $(tar tfz hub.tgz | head -n1 | cut -f1 -d"/")/install \
    && echo "installed hub" \
    && cd / \
    && rm -rf /hub \
    && hub version

# Sources:
# https://github.com/github/hub
#
# Docs:
# https://hub.github.com/
# https://hub.github.com/hub.1.html

#RUN mkdir -p ~/.ssh && ssh-keyscan -H github.com >> ~/.ssh/known_hosts

ENTRYPOINT [ "hub" ]
CMD [ "help" ]
