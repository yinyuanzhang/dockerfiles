#FROM debian:stretch-slim
FROM debian:stretch

ARG USER_ID
ARG GROUP_ID

ENV STELLAR_CORE_VERSION 12.1.0-28
ENV STELLAR_HORIZON_VERSION 0.22.2-65
ENV HOME /home/stellar

# add user with specified (or default) user/group ids
ENV USER_ID ${USER_ID:-1000}
ENV GROUP_ID ${GROUP_ID:-1000}

RUN groupadd -g ${GROUP_ID} stellar \
        && useradd -u ${USER_ID} -g stellar -s /bin/bash -m -d ${HOME} stellar
# slim workaround
#RUN bash -c "for i in {1..8}; do mkdir -p "/usr/share/man/man${i}"; done"
#RUN ls -la /usr/share/man
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y --no-install-recommends apt-transport-https gnupg ca-certificates wget gosu && \
  wget -qO - https://apt.stellar.org/SDF.asc | apt-key add - && \
  echo "deb https://apt.stellar.org/public stable/" | tee /etc/apt/sources.list.d/SDF.list && \
  apt-get update && \
  apt-get install -y --no-install-recommends stellar-core=$STELLAR_CORE_VERSION stellar-horizon=$STELLAR_HORIZON_VERSION && \
  apt-get purge -y apt-transport-https wget gnupg && \
  apt-get autoclean

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["stellard"]
