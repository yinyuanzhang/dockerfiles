FROM amazonlinux:2

ENV ELIXIR_VERSION 1.9.4

RUN yum install -y unzip
RUN mkdir -p /opt/elixir/${ELIXIR_VERSION}/
RUN curl -Lo /tmp/elixir.zip https://github.com/elixir-lang/elixir/releases/download/v${ELIXIR_VERSION}/Precompiled.zip
RUN unzip /tmp/elixir.zip -d /opt/elixir/${ELIXIR_VERSION}/

FROM groguelon/erlang:22.1-amazonlinux2

LABEL maintainer="Geoffrey Roguelon"

ENV PATH /opt/elixir/1.9.4/bin:$PATH

COPY --from=0 /opt/elixir /opt/elixir

RUN mix local.rebar --force && \
    mix local.hex --force

CMD ["iex"]
