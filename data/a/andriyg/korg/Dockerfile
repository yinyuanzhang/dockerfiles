FROM andriyg/python2.7:bionic-nonginx

ADD certs/* /usr/local/share/ca-certificates/

RUN \
  update-ca-certificates && \
  apt update && apt upgrade -y && apt install rsync -y && \
  rm -rf /var/lib/apt/lists/ && \
  groupadd  korg -g 1000 && adduser --ingroup korg --uid=1001 korg && \
  true

ADD requirements.txt requirements2.txt /tmp/

RUN \
  pip install -U -r /tmp/requirements.txt && \
  pip install -U -r /tmp/requirements2.txt && \
  true

COPY src/ /korg/src/
COPY templates/ /korg/templates/
COPY media/ /korg/media_orig/
COPY docker-entrypoint.sh /korg/

RUN \
    find /korg/src -type f -name '*.pyc' | xargs rm -vf && \
    mkdir -p /korg/static /korg/media && \
    chown -Rf root:korg /korg/src/ /korg/templates/ /korg/media_orig/ /korg/docker-entrypoint.sh && \
    chown -v korg:korg /korg/static /korg/media && \
    true

VOLUME /korg/static
VOLUME /korg/media

# final definitions
WORKDIR /korg/src/

USER korg

ENTRYPOINT /korg/docker-entrypoint.sh
