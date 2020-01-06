FROM jupyter/minimal-notebook
USER root
RUN apt update \
    && apt upgrade -y \
    && apt install -y python3-cffi \
    && wget http://ftp.es.debian.org/debian/pool/main/c/clips/libclips_6.30-4+b1_amd64.deb \
    && wget http://ftp.es.debian.org/debian/pool/main/c/clips/libclips-dev_6.30-4+b1_amd64.deb \
    && sudo dpkg -i libclips_6.30-4+b1_amd64.deb libclips-dev_6.30-4+b1_amd64.deb \
    && rm libclips_6.30-4+b1_amd64.deb libclips-dev_6.30-4+b1_amd64.deb \
    && pip install iclips
USER $NB_UID
ARG BUILD_DATE
ARG VCS_REF
ARG VCS_URL
ARG VERSION
LABEL   org.label-schema.build-date=$BUILD_DATE \
        org.label-schema.name="jupyterclips" \
        org.label-schema.description="image with iclips kernel for jupyter-notebook" \
        org.label-schema.url="https://hub.docker.com/r/krosf/jupyterclips/" \
        org.label-schema.vcs-ref=$VCS_REF \
        org.label-schema.vcs-url=$VCS_URL \
        org.label-schema.version=$VERSION \
        org.label-schema.schema-version="1.0" \
        MANTAINER="Rodrigo Sanabria <rodrigosanabria22@gmail.com>" 