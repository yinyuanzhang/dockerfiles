FROM ubuntu

# gettext-base contains envsubst program
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y gettext-base python python-pip python-dev libpq-dev && \
    pip install --no-cache-dir newrelic-plugin-agent[postgresql] && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m user

ADD newrelic-plugin-agent.cfg.tpl /etc/
ADD entrypoint.sh /usr/bin/entrypoint.sh

USER user
CMD entrypoint.sh
