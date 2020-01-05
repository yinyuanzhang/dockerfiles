FROM alpine:latest
ENV HUGO_VERSION 0.40.3
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux-64bit

# Install pygments (for syntax highlighting) and bash
RUN apk update && apk add py-pygments && apk add bash && rm -rf /var/cache/apk/*


# Download and Install hugo
RUN mkdir /usr/local/hugo
ADD https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz /usr/local/hugo/
RUN tar xzf /usr/local/hugo/${HUGO_BINARY}.tar.gz -C /usr/local/hugo/ \
	&& ln -s /usr/local/hugo/hugo /usr/local/bin/hugo \
	&& rm /usr/local/hugo/${HUGO_BINARY}.tar.gz

VOLUME ["/src", "/dest"]
EXPOSE 1313
ENV HUGO_SRC /src
ENV HUGO_DEST /dest
ENV HUGO_THEME hyde
ENV HUGO_BUILD_DRAFT false
ENV HUGO_BASE_URL ""
ADD run-hugo /run-hugo
ENTRYPOINT ["/run-hugo"]
CMD ["server", "--source=${HUGO_SRC}", "--theme=${HUGO_THEME}", "--buildDrafts=${HUGO_BUILD_DRAFT}", "--baseUrl=${HUGO_BASE_URL}", "--watch", "--destination=${HUGO_DEST}", "--appendPort=false"]
