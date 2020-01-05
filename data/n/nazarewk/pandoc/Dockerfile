FROM nazarewk/archlinux
MAINTAINER Krzysztof Nazarewski <nazarewk+docker@gmail.com>

RUN yay -S --noconfirm pandoc-bin pandoc-citeproc pandoc-crossref texlive-most \
 && sudo docker-build-cleanup arch

WORKDIR /source
ENTRYPOINT ["/usr/bin/pandoc"]
CMD ["--help"]