FROM openjdk:11.0-slim

ENV AUTO_REGISTER_RESOURCES="scala,maven,sbt,java11" \
    AUTO_REGISTER_ENVIRONMENTS="dev,stg"


RUN apt-get update \
    && apt-get install --no-install-recommends -y curl openssh-client gnupg2 apt-transport-https git jq procps maven gettext \
    && echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list \
    && echo "deb https://download.gocd.org /" | tee -a /etc/apt/sources.list.d/gocd.list \
    && curl -sSL https://download.gocd.org/GOCD-GPG-KEY.asc | apt-key add - \
    && apt-get update \
    && apt-get install --no-install-recommends -y --allow-unauthenticated sbt go-agent \
    && apt-get remove --purge -y gnupg2 \
    && apt-get autoremove --purge -y \
    && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

CMD ["/entrypoint.sh"]
