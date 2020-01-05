FROM alpine:3.3
MAINTAINER Erwin Boskma <erwin@datarift.nl

RUN apk --update add erlang-xmerl erlang-dialyzer erlang-cosproperty erlang-parsetools erlang-costime \
    erlang-test-server erlang-percept erlang-sasl erlang-stdlib erlang-runtime-tools erlang-ssh erlang-erl-docgen \
    erlang-eunit erlang erlang-inets erlang-orber erlang-tools erlang-cosfiletransfer erlang-snmp erlang-et erlang-ic \
    erlang-dev erlang-debugger erlang-jinterface erlang-typer erlang-asn1 erlang-erl-interface erlang-hipe \
    erlang-cosnotification erlang-odbc erlang-ose erlang-otp-mibs erlang-reltool erlang-crypto erlang-common-test \
    erlang-ssl erlang-mnesia erlang-cosevent erlang-compiler erlang-os-mon erlang-erts erlang-costransaction \
    erlang-public-key erlang-syntax-tools erlang-gs erlang-observer erlang-edoc erlang-kernel erlang-webtool \
    erlang-eldap erlang-coseventdomain erlang-megaco erlang-diameter && rm -rf /var/cache/apk/*

ENV ELIXIR_VERSION 1.2.2

RUN apk --update add --virtual build-dependencies wget ca-certificates && \
    wget https://github.com/elixir-lang/elixir/releases/download/v${ELIXIR_VERSION}/Precompiled.zip && \
    mkdir -p /opt/elixir-${ELIXIR_VERSION}/ && \
    unzip Precompiled.zip -d /opt/elixir-${ELIXIR_VERSION}/ && \
    rm Precompiled.zip && \
    apk del build-dependencies && \
    rm -rf /etc/ssl && \    
    rm -rf /var/cache/apk/*

ENV PATH $PATH:/opt/elixir-${ELIXIR_VERSION}/bin

RUN mix local.hex --force && \
    mix local.rebar --force

CMD ["/bin/sh"]

