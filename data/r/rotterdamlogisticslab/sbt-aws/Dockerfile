FROM  codestar/circleci-scala-sbt-git:scala-2.12.6-sbt-1.1.6


# kubernetes and helm. see https://github.com/dtzar/helm-kubectl
# Note: Latest version of kubectl may be found at:
# https://aur.archlinux.org/packages/kubectl-bin/
ENV KUBE_VERSION="1.10.3"
# Note: Latest version of helm may be found at:
# https://github.com/kubernetes/helm/releases
ENV HELM_VERSION="v2.9.1"
ENV DOCKER_VERSION="17.03.0-ce"


RUN \
  apk add --update --no-cache yarn && \
  apk add --no-cache python3 && \
  python3 -m ensurepip --default-pip && \
  rm -r /usr/lib/python*/ensurepip && \
  pip3 install --upgrade --no-cache-dir pip setuptools && \
  if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
  if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
  pip --no-cache-dir install awscli --ignore-installed six && \
  apk add --no-cache postgresql-client && \
  apk add --no-cache ncurses && \
  apk add --no-cache libc6-compat && \
  apk add --no-cache ca-certificates && \
  wget -q https://storage.googleapis.com/kubernetes-release/release/v${KUBE_VERSION}/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl && \
  chmod +x /usr/local/bin/kubectl && \
  curl -o /usr/bin/heptio-authenticator-aws https://amazon-eks.s3-us-west-2.amazonaws.com/${KUBE_VERSION}/2018-06-05/bin/linux/amd64/heptio-authenticator-aws && \
  chmod +x /usr/bin/heptio-authenticator-aws && \
  wget -q http://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm && \
  chmod +x /usr/local/bin/helm && \
  set -x && \
  curl -L -o /tmp/docker-${DOCKER_VERSION}.tgz https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz && \
  tar -xz -C /tmp -f /tmp/docker-${DOCKER_VERSION}.tgz && \
  mv /tmp/docker/* /usr/bin



