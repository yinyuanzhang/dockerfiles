FROM %%BASE_IMAGE%%

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.name="ruby%%RUBY_VERSION%%" \
      org.label-schema.description="A Ruby %%RUBY_VERSION%% image based on Debian %%DEBIAN_RELEASE%%." \
      org.label-schema.url="https://github.com/LuisAlejandro/dockershelf" \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.vcs-url="https://github.com/LuisAlejandro/dockershelf" \
      org.label-schema.vendor="Luis Alejandro Martínez Faneyth" \
      org.label-schema.version=${VERSION} \
      org.label-schema.schema-version="1.0.0-rc.1" \
      maintainer="Luis Alejandro Martínez Faneyth <luis@luisalejandro.org>"

ENV RUBY_VER_NUM="%%RUBY_VERSION%%" RUBY_DEBIAN_SUITE="%%RUBY_DEBIAN_SUITE%%"

COPY build-image.sh library.sh /usr/share/dockershelf/ruby/
RUN bash /usr/share/dockershelf/ruby/build-image.sh

CMD ["ruby"]