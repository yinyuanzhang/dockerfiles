FROM debian:stable
WORKDIR /tmp
RUN apt-get update && apt-get install -y \
  wget \
  xz-utils\
  xxd \
  openssl \
&& wget -qO- "https://developer.salesforce.com/media/salesforce-cli/sfdx-linux-amd64.tar.xz" \
  | tar xJf - \
&& bash ./$(ls | grep sfdx)/install \
&& apt-get remove -y wget xz-utils && apt-get autoremove -y \
&& rm -rf /var/lib/apt/lists/*
