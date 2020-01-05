FROM hashicorp/packer:light

RUN apk update
RUN apk --no-cache add git python unzip tar openssh-client rsync jq py2-pip py-boto py2-six py2-cryptography py2-bcrypt py2-asn1crypto py2-jsonschema py2-pynacl py2-asn1 py2-markupsafe py2-paramiko py2-dateutil py2-docutils py2-futures py2-rsa py2-libxml2 libxml2 libxslt && \
    apk --no-cache add gcc python2-dev musl-dev linux-headers libxml2-dev libxslt-dev && \
    pip install ansible jsonmerge awscli boto3 hvac ansible-modules-hashivault molecule python-gilt python-jenkins lxml openshift docker docker-compose mitogen yamale ansible-lint && \
    apk del gcc python2-dev musl-dev linux-headers libxml2-dev libxslt-dev

USER root

ENTRYPOINT [] 
