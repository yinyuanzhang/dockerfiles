FROM gcr.io/distroless/java:debug
STOPSIGNAL 9
COPY ./glowroot-central /glowroot-central
COPY ./docker-entrypoint.sh /usr/bin/docker-entrypoint.sh
WORKDIR /glowroot-central
EXPOSE 4000 8181
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]
CMD ["/usr/bin/java","-jar","glowroot-central.jar"]