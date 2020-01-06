FROM python:2

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
      vim nano \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/ \
  && \
  pip install --no-cache-dir jira-cli

ENTRYPOINT [ "jira-cli" ]
CMD [ "-h" ]
