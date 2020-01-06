FROM rabbitmq

ARG BUILD_DATE
ARG VCS_REF

# Good docker practice, plus we get microbadger badges
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/grin-pool.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"
      
RUN set -ex && \
    apt-get update && \
    apt-get --no-install-recommends --yes install \
        python

#ENV RABBITMQ_USER mwgrinpool
#ENV RABBITMQ_PASSWORD rpassword

COPY rabbitmqadmin /
COPY definitions.json /etc/rabbitmq/

RUN rabbitmq-plugins enable rabbitmq_management
