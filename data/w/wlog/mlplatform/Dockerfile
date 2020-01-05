#
# Collecting system packages
#

FROM ubuntu:16.04 as syspkgs_builder

RUN apt-get update \
    && mkdir -p /tmp/syspacks \
    && apt-get install -y --download-only -o "dir::cache=/tmp/syspacks" \
        python-pip \
        dos2unix \
        curl

#
# Building image itsel
#

FROM ubuntu:16.04

ARG whisky_tag_raw
ENV WHISKY_TAG ${whisky_tag_raw:-dev}

COPY --from=syspkgs_builder /tmp/syspacks /tmp/syspacks

COPY ./packages_Py /tmp/packages_Py
RUN echo "======== Building wlog/whisky:base_pybuilder($WHISKY_TAG) ..." \
    && apt-get install -y --allow-downgrades /tmp/syspacks/archives/*.deb \
    && find . -name /tmp/packages_Py/\*.py | xargs dos2unix \
        && /usr/bin/pip install /tmp/packages_Py/whisky_core \
    && rm -rf /tmp/*
