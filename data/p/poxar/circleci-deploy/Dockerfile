FROM circleci/python:3

RUN sudo apt-get update -y \
 && sudo apt-get upgrade -y \
 && sudo apt-get install -y lsb-release gettext

RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" \
 && echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
 && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - \
 && sudo apt-get update -y \
 && sudo apt-get install -y google-cloud-sdk kubectl

ENV OC_VERSION=v3.11.0 \
    OC_TAG_SHA=0cbc58b

RUN curl -sLo /tmp/oc.tar.gz https://github.com/openshift/origin/releases/download/${OC_VERSION}/openshift-origin-client-tools-${OC_VERSION}-${OC_TAG_SHA}-linux-64bit.tar.gz \
 && tar xzvf /tmp/oc.tar.gz -C /tmp/ \
 && sudo mv /tmp/openshift-origin-client-tools-${OC_VERSION}-${OC_TAG_SHA}-linux-64bit/oc /usr/local/bin/ \
 && sudo chown root:root /usr/local/bin/oc \
 && sudo chmod 0555 /usr/local/bin/oc \
 && rm -rf /tmp/oc.tar.gz /tmp/openshift-origin-client-tools-${OC_VERSION}-${OC_TAG_SHA}-linux-64bit
