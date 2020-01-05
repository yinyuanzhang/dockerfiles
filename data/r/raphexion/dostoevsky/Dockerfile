FROM erlang:20.3.7

RUN git clone https://github.com/Raphexion/dostoevsky.git /dostoevsky
WORKDIR /dostoevsky

RUN rebar3 release

EXPOSE 7070

ENTRYPOINT ["/dostoevsky/_build/default/rel/dostoevsky/bin/dostoevsky", "foreground"]
