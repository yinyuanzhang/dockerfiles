FROM bitnami/postgresql:10.6.0
USER root
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
  build-essential libssl-dev libkrb5-dev git
RUN git clone https://github.com/pgaudit/pgaudit.git /tmp/pgaudit
WORKDIR /tmp/pgaudit
RUN git checkout REL_10_STABLE
RUN make install USE_PGXS=1
WORKDIR /
USER 1001
