FROM debian:stable-slim
ONBUILD COPY --from=snapshot /usr/bin/dart /usr/bin/dart
ONBUILD COPY --from=snapshot /app/main.snap /app/
ONBUILD ENTRYPOINT ["dart", "/app/main.snap"]
