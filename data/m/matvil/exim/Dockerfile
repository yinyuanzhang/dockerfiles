FROM alpine:3.8 as builder
RUN apk update && apk add alpine-sdk
RUN echo "%abuild ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN adduser builder -D -G abuild -s /bin/sh
USER builder
WORKDIR /home/builder
RUN abuild-keygen -a
RUN git clone --depth 1 -b 3.8-stable https://github.com/alpinelinux/aports.git
WORKDIR /home/builder/aports/community/exim
RUN sed -i 's/EXPERIMENTAL_PROXY/SUPPORT_PROXY/' exim.Makefile
RUN abuild checksum
RUN abuild -r

FROM alpine:3.8
RUN apk --update-cache --no-cache add ca-certificates s6
COPY --from=builder /home/builder/packages/community/x86_64/exim-4.91-r1.apk /tmp/
RUN apk add --allow-untrusted /tmp/exim-4.91-r1.apk && rm /tmp/exim-4.91-r1.apk
COPY etc/ /etc/
ENTRYPOINT [ "/bin/s6-svscan", "/etc/s6" ]
