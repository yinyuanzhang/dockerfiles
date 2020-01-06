FROM alpine:3.9 as build

ARG TIKZ_UML_VERSION=v1.0-2016-03-29

WORKDIR /work

RUN apk --no-cache add libarchive-tools && \
        wget -qO- https://perso.ensta-paristech.fr/~kielbasi/tikzuml/var/files/src/tikzuml-${TIKZ_UML_VERSION}.tbz | bsdtar -xvf - && \
        mkdir tikz-uml && \
        mv tikzuml-${TIKZ_UML_VERSION}/tikz-uml.sty tikz-uml/ && \
        wget https://raw.githubusercontent.com/aclements/latexrun/master/latexrun -O latexrun && \
        chmod +x latexrun

FROM ubuntu:18.04

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Latexrun" \
      org.label-schema.description="LaTeX build based on latexrun" \
      org.label-schema.url="https://github.com/baez90/docker-latex" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/baez90/docker-latex" \
      org.label-schema.vendor="baez90" \
      org.label-schema.version="latest" \
      org.label-schema.schema-version="1.0" \
      maintainer="peter.kurfer@gmail.com"

COPY --from=build /work/tikz-uml /usr/share/texmf/tex/
COPY --from=build /work/latexrun /usr/local/bin/latexrun

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
	apt-get install \
		-y \
		--no-install-recommends \
        make \
        python-pygments \
        hunspell hunspell-tools hunspell-de-de hunspell-en-us hunspell-en-gb \
		    texlive-full && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/