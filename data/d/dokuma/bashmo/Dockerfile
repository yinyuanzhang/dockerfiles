FROM appropriate/curl:3.1 AS get-mo
RUN curl -sSL https://raw.githubusercontent.com/tests-always-included/mo/2.0.4/mo -o mo &&\
    chmod +x mo &&\
    mv mo /usr/bin/

FROM bash:5.0.7
COPY --from=get-mo /usr/bin/mo /usr/bin/mo
ENTRYPOINT ["/usr/bin/mo"]
