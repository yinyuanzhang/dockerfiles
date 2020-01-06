FROM h2non/imaginary:1.0.15

ENV IMAGINARY_VERSION="1.0.15" \
    PORT=9000

RUN addgroup --gid 1000 imaginary \
 && adduser imaginary --uid 1000 --gid 1000 --shell /bin/sh

USER imaginary
