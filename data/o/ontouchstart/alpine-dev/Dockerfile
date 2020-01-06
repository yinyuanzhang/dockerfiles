FROM alpine
RUN apk add --update alpine-sdk \
      erlang \
      elixir \
      go \
      ruby \
      python \
      python3 \
      perl \
      nodejs \
      lua 
RUN cat /etc/os-release
RUN cat /usr/lib/erlang/releases/RELEASES
RUN iex -v
RUN go version
RUN ruby --version
RUN python --version
RUN python3 --version
RUN perl --version
RUN node -v
RUN lua -v

ENTRYPOINT ["sh"]
