FROM debian:8

MAINTAINER Paul Williams <kwakwa@cpan.org>

ENV BUILD_PACKAGES build-essential wget
ENV MAIN_PACKAGES  fontconfig libjpeg62-turbo libssl-dev libxext6 libxrender-dev xfonts-base xfonts-75dpi

RUN apt-get update -qq \
  && apt-get install --no-install-recommends -yq $BUILD_PACKAGES $MAIN_PACKAGES \
  && wget --quiet http://download.gna.org/wkhtmltopdf/0.12/0.12.2/wkhtmltox-0.12.2_linux-jessie-amd64.deb \
  && dpkg -i wkhtmltox-0.12.2_linux-jessie-amd64.deb \
  && apt-get remove -y $BUILD_PACKAGES \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && truncate -s 0 /var/log/*log

ENTRYPOINT ["wkhtmltopdf"]

# Show the extended help
CMD ["-h"]
