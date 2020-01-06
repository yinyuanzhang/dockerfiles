FROM node:11.4.0-stretch-slim

ENV YARNHOME /home/node/yarn
ENV APPHOME /home/node/app
ENV PATH $PATH:$YARNHOME/bin

RUN set -eux; \
  mkdir -p $YARNHOME/bin $APPHOME \
  && chown -R node:node ~node \
  && apt-get update \
  && apt-get install git -y \
  && rm -rf /var/lib/apt/lists/* \
  && curl -o purty.tar.gz -L https://bintray.com/joneshf/generic/download_file\?file_path\=purty-3.0.7-linux.tar.gz \
  && tar -xzvf purty.tar.gz \
  && mv purty /usr/local/bin \
  && chmod +x /usr/local/bin/purty \
  && rm -rf purty.tar.gz

USER node
WORKDIR $APPHOME
RUN set -eux; \
  yarn global add --prefix $YARNHOME \
    purescript \
    pulp \
    psc-package \
  && pulp --version \
  && psc-package --version

VOLUME [$APPHOME]

CMD ["pulp", "run"]
