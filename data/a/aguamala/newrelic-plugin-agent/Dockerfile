FROM aguamala/centos-systemd:7
MAINTAINER "gabo" <aguamala@deobieta.com>

RUN yum -y install epel-release unzip &&\
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 &&\
    yum install -y python-pip &&\
    pip install --upgrade pip &&\
    pip install newrelic-plugin-agent &&\
    yum clean all && \
    groupadd newrelic && \
    useradd newrelic -g newrelic

ENV CONSUL_TEMPLATE_VERSION 0.15.0

RUN gpg --keyserver keys.gnupg.net --recv-keys 91A6E7F85D05C65630BEF18951852D87348FFC4C && \
    mkdir -p /tmp/build && \
    cd /tmp/build && \
    curl -O https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip  && \
    curl -O https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS && \
    curl -O https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS.sig && \
    gpg --batch --verify consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS.sig consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS && \
    grep ${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS | sha256sum -c && \
    unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    cp  consul-template /usr/local/bin/ && \
    cd /tmp && \
    rm -rf /tmp/build && \
    rm -rf /root/.gnupg && \
    yum remove -y unzip

RUN mkdir -p /etc/consul-template /etc/consul-template/conf.d /etc/consul-template/templates && \
    mkdir -p /opt/newrelic-plugin-agent/assemble && \
    mkdir -p /var/log/newrelic && \
    chown newrelic:newrelic -R /var/log/newrelic


COPY config.hcl /etc/consul-template/conf.d/
COPY consul-template.service /etc/systemd/system/
RUN systemctl enable consul-template.service

COPY newrelic-plugin-agent.service /etc/systemd/system/
RUN systemctl enable newrelic-plugin-agent.service

COPY newrelic-plugin-agent-restart /usr/bin/
RUN chmod +x /usr/bin/newrelic-plugin-agent-restart
