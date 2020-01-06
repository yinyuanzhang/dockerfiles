FROM cblomart/gobasebuild as builder
MAINTAINER cblomart@gmail.com

RUN CC=musl-gcc CCGLAGS="-static" go get -ldflags '-linkmode external -s -w -extldflags "-static"' -a  github.com/vmware/govmomi/vcsim;\
    upx -qq --best --lzma ./bin/vcsim;\
    mv ./bin/vcsim /tmp/;\
    mkdir /tmp/tmp;\
    chmod 1777 /tmp/tmp

FROM scratch

COPY --from=builder /tmp/vcsim /vcsim
COPY --from=builder /tmp/tmp /tmp

EXPOSE 8989

CMD [ "/vcsim", "-l", ":8989" ]
