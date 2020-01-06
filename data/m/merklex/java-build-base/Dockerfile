FROM merklex/efvi:latest

FROM merklex/java8-jdk

COPY --from=0 /usr/local/lib/* /usr/local/lib/
COPY --from=0 /usr/local/include/ci /usr/local/include/ci
COPY --from=0 /usr/local/include/etherfabric /usr/local/include/etherfabric

