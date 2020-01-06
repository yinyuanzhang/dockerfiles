FROM elixir:1.8
ARG VCS_REF
ARG BUILD_DATE


LABEL org.label-schema.vcs-ref=$VCS_REF \
          org.label-schema.vcs-url="https://github.com/mloftis/docker-elixir" \
          org.label-schema.build-date=$BUILD_DATE \
          org.label-schema.schema-version="1.0"


RUN set -x && apt-get update && apt-get install -y libgmp-dev libboost-dev postgresql-client ocl-icd-opencl-dev ocl-icd-libopencl1 pocl-opencl-icd

CMD ["iex"]
