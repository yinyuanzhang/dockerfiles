FROM node:8-slim

LABEL vendor="Dr.Entrega" \
      maintainer="Dr.Entrega <technology+docker@drentrega.com>" \
      image="node" \
      tag="8-slim"

RUN apt-get update -yq \
  && apt-get upgrade -yq \
  && apt-get install -yq git-core openssl python make g++ \
  && apt-get clean -yq \
  && apt-get autoremove -yq \
  && mkdir /root/.ssh \
  && touch /root/.ssh/known_hosts \
  && ssh-keyscan bitbucket.org \
  && ssh-keyscan github.com

ENTRYPOINT [""]

CMD ["sh", "-c", "npm i --production --non-interactive"]

# This dockerfile was auto-generated at 2019-01-10T11:38:35-02:00.

# In case of security branches, please contact technology+security@drentrega.com.