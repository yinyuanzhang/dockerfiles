FROM mongo:3.0.14

LABEL maintainer "itiQiti SAS <opensource@itiqiti.com>"
LABEL creator "Mikael Robert <mikaelrob@gmail.com>"

ENV MODE=default

RUN apt-get update && \
    apt-get install -y curl && \
    curl -s -f -L https://github.com/itiqiti/dkconf/releases/download/0.2/dkconf-linux -o /usr/local/bin/dkconf && \
    chmod +x /usr/local/bin/dkconf && \
    apt-get remove -y curl && \
    apt-get autoremove -y

COPY ["templates", "/usr/local/etc/mongo/templates"]
COPY ["docker-pre-entrypoint.sh", "/usr/local/bin/"]

# docker-entrypoint.sh already exist in base image
ENTRYPOINT ["/usr/local/bin/docker-pre-entrypoint.sh"]

CMD ["mongod"]
