FROM google/dart

VOLUME [ "/work", "/output" ]

RUN mkdir -p /app
COPY pubspec.yaml /app
COPY compile-sass.dart /app

WORKDIR /app
RUN pub get

WORKDIR /work

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
