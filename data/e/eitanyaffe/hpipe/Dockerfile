FROM eitanyaffe/hpipe_base:v1.2

ENV MAKESHIFT_ROOT /ms_root

RUN mkdir ${MAKESHIFT_ROOT}
WORKDIR ${MAKESHIFT_ROOT}

# clone code from git
RUN \
git clone --branch v1.2 https://github.com/eitanyaffe/makeshift-core.git && \
git clone --branch v1.2.3 https://github.com/eitanyaffe/makeshift-modules.git && \
git clone --branch v1.2.3 https://github.com/eitanyaffe/hpipe

# compile binaries
WORKDIR ${MAKESHIFT_ROOT}/hpipe/pipeline
RUN make init

