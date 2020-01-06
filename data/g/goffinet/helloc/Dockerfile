FROM debian AS compiler
RUN apt-get update && apt-get install -y build-essential
COPY hello.c /
RUN make hello
FROM debian
COPY --from=compiler /hello /hello
CMD /hello
