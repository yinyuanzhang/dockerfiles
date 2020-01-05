FROM docker:stable

LABEL maintainer="Yoann VANITOU <yvanitou@gmail.com>"

ARG DCRON_VERSION=4.5

RUN set -x \
    && apk add --virtual mybuild --no-cache \
        build-base \
    && apk add tzdata --no-cache \
    && cd /tmp \
    && wget -O dcron.tar.gz "https://github.com/dubiousjim/dcron/archive/v${DCRON_VERSION}.tar.gz" \
    && tar xvzf dcron.tar.gz \
    && cd dcron-${DCRON_VERSION} \
    && make -j$(nproc) \
    && make install \
    && cd \
    && rm -rf /tmp/* \
    && apk del mybuild

COPY --chown=0:0 ./entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/usr/local/sbin/crond", "-f", "-l", "6", "-s", "/etc/cron.d", "/etc/cron.d/*"]
