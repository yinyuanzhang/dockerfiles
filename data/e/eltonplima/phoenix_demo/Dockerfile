# Build context image
FROM elixir:1.7-alpine as builder

ENV MIX_ENV=prod

WORKDIR /home/builder
COPY . .
RUN apk update
RUN apk add bash git
RUN mix local.hex --force
RUN mix local.rebar --force
RUN mix deps.get
RUN cd apps/phoenix_demo_web && mix phx.digest && cd -
RUN mix release
# Final image

FROM elixir:1.7-alpine

LABEL "project"="phoenix_demo"
LABEL "version"="0.1.0"
ARG TESTE
RUN echo "This is the TESTE value: " && echo ${TESTE}
ENV TESTE=${TESTE}
ENV MIX_ENV=prod
ENV PORT=4000

RUN apk update && apk add bash
WORKDIR /home/app
COPY --from=builder /home/builder/_build _build

ENTRYPOINT ["_build/prod/rel/phoenix_demo_umbrella/bin/phoenix_demo_umbrella"]
CMD ["foreground"]
