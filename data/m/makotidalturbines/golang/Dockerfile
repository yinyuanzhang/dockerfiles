FROM circleci/golang:1.11.5

# ensure golang dep is available
RUN dep version

# install gcloud
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-jessie main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl -sS https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - && \
    sudo apt-get update -y -qq && \
    sudo apt-get install google-cloud-sdk -y && \
    sudo rm -rf /var/lib/apt/lists/*

# install ghr (GitHub release file uploader)
ENV GHR_VERSION 0.12.0
RUN sudo wget -q -O tmp.tgz https://github.com/tcnksm/ghr/releases/download/v${GHR_VERSION}/ghr_v${GHR_VERSION}_linux_amd64.tar.gz && \
    sudo tar -xzf tmp.tgz --strip-components=1 -C /usr/local/bin ghr_v${GHR_VERSION}_linux_amd64/ghr && \
    sudo rm -rf tmp.tgz
