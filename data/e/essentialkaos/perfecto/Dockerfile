## BUILDER #####################################################################

FROM centos:6 as builder

RUN mkdir -p "/go/src" && chmod -R 777 "/go"

ENV GOPATH=/go

WORKDIR /go/src/github.com/essentialkaos/perfecto

COPY . .

RUN yum -y -q install https://yum.kaos.st/kaos-repo-latest.el6.noarch.rpm && \
    yum -y -q install make golang git upx && \
    make deps && \
    make all && \
    upx perfecto

## FINAL IMAGE #################################################################

FROM centos:6

LABEL name="Perfecto Image on CentOS 6" \
      vendor="ESSENTIAL KAOS" \
      maintainer="Anton Novojilov" \
      license="EKOL" \
      version="2019.07.10"

COPY --from=builder /go/src/github.com/essentialkaos/perfecto/perfecto /usr/bin/

COPY common/rpmlint.conf /root/.config/rpmlint

RUN yum -y -q install https://yum.kaos.st/kaos-repo-latest.el6.noarch.rpm && \
    yum -y -q install rpmlint

VOLUME /perfecto
WORKDIR /perfecto

ENTRYPOINT ["perfecto"]

################################################################################
