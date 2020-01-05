FROM funkypenguin/grinpool-mwnginx-dockerbase

ARG BUILD_DATE
ARG VCS_REF

# Good docker practice, plus we get microbadger badges
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/grin-pool.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"

WORKDIR /keybase
RUN chown 1000:1000 /keybase
ENV HOME /keybase

EXPOSE 16423
EXPOSE 16723

RUN echo "keybase:x:1000:1000:,,,:/keybase:/bin/bash" >> /etc/passwd && \
    echo "keybase:x:1000:" >> /etc/group && \
    echo "keybase:x:17888:0:99999:7:::" >> /etc/shadow

COPY keybase_amd64.deb /keybase/
RUN set -ex && \
    apt-get update && \
    dpkg -i keybase_amd64.deb || /bin/true
RUN apt-get install -f --yes
RUN set -ex && \
    apt-get --no-install-recommends --yes install \
      vim \
      net-tools \
      procps

COPY entrypoint.sh /

CMD ["/entrypoint.sh"]
