FROM drentrega/aws-cli:stable-slim

LABEL vendor="Dr.Entrega" \
      maintainer="Dr.Entrega <technology+docker@drentrega.com>" \
      image="drentrega/aws-cli" \
      tag="stable-slim"

RUN apt-get update --yes \
  && apt-get upgrade --yes \
  && apt-get install  --yes --quiet curl \
  && apt-get clean --yes --quiet \
  && apt-get autoremove --yes --quiet \
  && curl https://get.docker.com/ | bash \
  && service docker start

ENTRYPOINT [""]

# This dockerfile was auto-generated at 2019-01-10T11:38:35-02:00.

# In case of security branches, please contact technology+security@drentrega.com.