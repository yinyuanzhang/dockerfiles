FROM debian:buster

WORKDIR /home/terraform

ENV \
	HOME /home/terraform

ENV \
	GOPASS_VERSION=1.8.5 \
	SUMMON_VERSION=0.6.11 \
	SUMMON_PROVIDER=$HOME/bin/summon-gopass \
	PATH=$HOME/.tfenv/bin:$HOME/bin:$PATH

COPY moduleroot/Makefile.erb Makefile
COPY summon-gopass $SUMMON_PROVIDER

RUN apt-get update && apt-get install -y \
	git \
	gpg \
	make \
	unzip \
	wget \
	libnss-wrapper \
	ansible \
	curl \
	&& rm -rf /var/lib/apt/lists/*

# Install gopass
RUN wget https://github.com/gopasspw/gopass/releases/download/v${GOPASS_VERSION}/gopass-${GOPASS_VERSION}-linux-amd64.tar.gz -qO - | tar xz gopass-${GOPASS_VERSION}-linux-amd64/gopass -O > $HOME/bin/gopass
RUN chmod +x $HOME/bin/gopass

# Install summon
RUN wget https://github.com/cyberark/summon/releases/download/v${SUMMON_VERSION}/summon-linux-amd64.tar.gz -qO - | tar xz summon -O > $HOME/bin/summon
RUN chmod +x $HOME/bin/summon

RUN chown 1001:0 -R $HOME && chmod g=u -R $HOME

USER 1001

RUN make install
