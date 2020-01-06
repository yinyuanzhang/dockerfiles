FROM runatlantis/atlantis:v0.6.0

ENV TERRAGRUNT_VERSION=0.18.2
ENV KOPS_VERSION=1.11.1

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# Install terragrunt
RUN curl -Ls https://github.com/gruntwork-io/terragrunt/releases/download/v${TERRAGRUNT_VERSION}/terragrunt_linux_386 \
  -o /usr/local/bin/terragrunt && chmod +x /usr/local/bin/terragrunt

# Install kops
RUN curl -Lso kops https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-linux-amd64 \
  && chmod +x ./kops \
  && mv ./kops /usr/local/bin/

# Python packages for Terragrunt hooks
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Git token config
COPY gitconfig /home/atlantis/.gitconfig
RUN chown atlantis /home/atlantis/.gitconfig && chmod 644 /home/atlantis/.gitconfig

# AWS config
COPY aws.config /home/atlantis/.aws/config
RUN chown atlantis /home/atlantis/.aws/config && chmod 644 /home/atlantis/.aws/config

# copy docker entrypoint
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["server"]