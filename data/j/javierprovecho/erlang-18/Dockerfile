FROM alpine
MAINTAINER javiertitan@gmail.com

RUN export DEPS="\
	git \
	erlang \
	erlang-webtool \
	erlang-xmerl \
	erlang-tools \
	erlang-typer \
	erlang-snmp \
	erlang-test-server \
	erlang-syntax-tools \
	erlang-ssl \
	erlang-sasl \
	erlang-runtime-tools \
	erlang-ssh \
	erlang-stdlib \
	erlang-ose \
	erlang-otp-mibs \
	erlang-reltool \
	erlang-mnesia \
	erlang-percept \
	erlang-parsetools \
	erlang-orber \
	erlang-public-key \
	erlang-odbc \
	erlang-os-mon \
	erlang-observer \
	erlang-et \
	erlang-ic \
	erlang-megaco \
	erlang-kernel \
	erlang-hipe \
	erlang-inets \
	erlang-jinterface \
	erlang-erts \
	erlang-gs \
	erlang-eunit \
	erlang-debugger \
	erlang-costime \
	erlang-costransaction \
	erlang-erl-interface \
	erlang-edoc \
	erlang-dialyzer \
	erlang-eldap \
	erlang-diameter \
	erlang-erl-docgen \
	erlang-crypto \
	erlang-cosevent \
	erlang-cosnotification \
	erlang-asn1 \
	erlang-cosfiletransfer \
	erlang-coseventdomain \
	erlang-dev \
	erlang-common-test \
	erlang-compiler \
	erlang-cosproperty\
 " &&\
 apk --update add $DEPS &&\
 rm -rf /var/cache/apk/* &&\
 git clone https://github.com/erlang/rebar3.git /rebar3 &&\
 cd /rebar3 &&\
 escript bootstrap &&\
 mv /rebar3/rebar3 /bin &&\
 cd / &&\
 rm -rf /rebar3

