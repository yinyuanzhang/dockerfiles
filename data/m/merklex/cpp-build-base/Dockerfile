FROM merklex/celero:latest
FROM merklex/efvi:latest

FROM merklex/build-essentials

COPY --from=0 /usr/local/lib/* /usr/local/lib/
COPY --from=0 /usr/local/include/celero/ /usr/local/include/celero

COPY --from=1 /usr/local/lib/* /usr/local/lib/
COPY --from=1 /usr/local/include/ci /usr/local/include/ci
COPY --from=1 /usr/local/include/etherfabric /usr/local/include/etherfabric
