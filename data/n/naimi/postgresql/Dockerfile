FROM bitnami/postgresql:11

USER root

RUN echo 'ru_RU.UTF-8 UTF-8' >> /etc/locale.gen && \
    echo 'kk_KZ.UTF-8 UTF-8' >> /etc/locale.gen && \
    locale-gen
    
USER 1001