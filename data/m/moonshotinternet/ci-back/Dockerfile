FROM python:3.7-slim

LABEL vendor=Moonshot-Internet
LABEL com.moonshot.name=ci-back
LABEL com.moonshot.version=1.0.0

# add src
RUN mkdir -p /opt/bin/src
COPY ./src/ /opt/bin/src

# Set apt preferences
RUN mv /opt/bin/src/preferences /etc/apt/preferences
RUN echo "# testingi\n deb http://deb.debian.org/debian testing main" >> /etc/apt/sources.list

# install missing software
RUN apt-get update && apt-get install --no-install-recommends -y rsync \
    curl \
    gpg \
    vim \
    zip \
    unzip \
    git \
    jq \
    openssh-client \
    libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info \
    && apt-get install -y -t testing libcairo2 \
    && rm -rf /var/lib/apt/lists/*

# install some python packages
RUN pip install --no-cache-dir \
    awscli \
    boto3 \
    botocore \
    yq \
    virtualenv \
    flake8 \
    tox \
    pytest \
    WeasyPrint \
    ansible

# install terraform latest version
RUN curl --output /tmp/terraform.zip https://releases.hashicorp.com/terraform/0.12.16/terraform_0.12.16_linux_amd64.zip \
    && unzip -d /usr/local/bin/ /tmp/terraform.zip \
    && rm /tmp/terraform.zip

# do some tweaks
RUN  mkdir /etc/ansible/ /ansible \
    && echo "[local]" >> /etc/ansible/hosts \
    && echo "localhost ansible_connection=local" >> /etc/ansible/hosts \
    && echo "[defaults]" >> /etc/ansible/ansible.cfg \
    && echo "retry_files_save_path = \"/tmp\"" >> /etc/ansible/ansible.cfg \
    && echo "jinja2_native = true" >> /etc/ansible/ansible.cfg \
    && rm -rf /root/.cache

RUN ln -s /usr/local/bin/python /usr/bin/python

# flatten scripts, clean-up dirs, add execution flag to binaries, link'em to the bin PATH
RUN find /opt/bin/src -type f -exec sh -c 'mv "$@" /opt/bin' _ {} + \
    && find /opt/bin/* -type d -depth -exec rmdir {} + \
    && chmod +x /opt/bin/*.sh \
    && chmod +x /opt/bin/*.py \
    && ln -s /opt/bin/*.sh /usr/local/bin/. \
    && ln -s /opt/bin/*.py /usr/local/bin/.

# add ansible playbooks
COPY ansible /ansible

RUN addgroup --gid 1001 --system ciuser && \
    adduser --uid 1000 --system ciuser --group

USER ciuser

