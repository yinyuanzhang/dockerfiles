FROM moander/java8

ENV BIGTOP_VERSION=1.2.1

RUN curl https://apache.uib.no/bigtop/bigtop-${BIGTOP_VERSION}/repos/GPG-KEY-bigtop | apt-key add - \
 && curl https://apache.uib.no/bigtop/bigtop-${BIGTOP_VERSION}/repos/debian8/bigtop.list -o /etc/apt/sources.list.d/bigtop.list \
 && apt-get update && apt-get install -y --no-install-recommends bigtop-utils \
 && rm -rf /var/lib/apt/lists/*

