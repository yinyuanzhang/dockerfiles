FROM rancher/confd-base:0.11.0-dev-rancher

ADD ./conf.d /etc/confd/conf.d
ADD ./templates /etc/confd/templates

VOLUME ["/app/gogs/custom/conf"]

ENV GOGS_SERVICE_ENABLE_REVERSE_PROXY_AUTHENTICATION=false \
    GOGS_SERVICE_ENABLE_REVERSE_PROXY_AUTO_REGISTRATION=false \
    GOGS_SERVICE_DISABLE_REGISTRATION=false \
    GOGS_SERVICE_SHOW_REGISTRATION_BUTTON=true

ENTRYPOINT ["/confd"]
CMD ["--backend", "env", "--onetime", "--log-level", "debug"]
