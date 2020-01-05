FROM ubuntu:19.04

# install pdftk
RUN apt-get update \
    && apt-get install -y --no-install-recommends pdftk \
    && rm -Rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
