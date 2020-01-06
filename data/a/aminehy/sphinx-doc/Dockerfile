FROM alpine:latest

LABEL maintainer "Amine Hadj-Youcef  <hadjyoucef.amine@gmail.com>"
# Connect with me: LinkedIn - https://www.linkedin.com/in/aminehy/

ENV VERSION="2.1.2"

RUN apk --no-cache add make py3-pip python3-dev && \
    pip3 install --upgrade pip &&\
    pip3 install sphinx==${VERSION} && \
    pip3 install sphinx_rtd_theme && \
    pip3 install sphinx-autobuild && \
    pip3 install pygments-markdown-lexer && \
    pip3 install recommonmark && \
    pip3 install sphinxcontrib-mermaid

WORKDIR /workspace
