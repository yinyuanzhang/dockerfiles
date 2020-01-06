# 0:

FROM alpine
RUN apk update; apk add --purge build-base gcc abuild binutils boost boost-dev boost-program_options cmake openssl openssl-dev git; cd; git clone https://github.com/trojan-gfw/trojan.git ; cd trojan/ ; mkdir build ; cd build/ ; cmake -DENABLE_MYSQL=OFF .. ; make ; ctest ; make install
WORKDIR /root
RUN mkdir trojan-gfw
WORKDIR /root/trojan-gfw
RUN mkdir -p usr/local/bin; cp -r /usr/local/bin/trojan usr/local/bin/ ; \
        mkdir -p usr/local/etc; cp -r /usr/local/etc/trojan usr/local/etc/ ; \
        mkdir -p usr/local/share/man/man1; cp -r /usr/local/share/man/man1/trojan.1 usr/local/share/man/man1/ ; \
        mkdir -p usr/local/share/doc; cp -r /usr/local/share/doc/trojan usr/local/share/doc/ ; \
# Folders below are not necessary ---->
# /usr/local/bin/trojan \
# /usr/local/etc/trojan/config.json \
# /usr/local/share/man/man1/trojan.1 \
# /usr/local/share/doc/trojan \
# /usr/local/share/doc/trojan/authenticator.md \
# /usr/local/share/doc/trojan/build.md \
# /usr/local/share/doc/trojan/config.md \
# /usr/local/share/doc/trojan/README.md \
# /usr/local/share/doc/trojan/usage.md \
# /usr/local/share/doc/trojan/protocol.md \
# /usr/local/share/doc/trojan/overview.md \
# /usr/local/share/doc/trojan/examples \
# /usr/local/share/doc/trojan/examples/client.json-example  \
# /usr/local/share/doc/trojan/examples/forward.json-example \
# /usr/local/share/doc/trojan/examples/server.json-example .
        mkdir -p usr/bin; cp -r /usr/bin/openssl usr/bin/ ; \
### No need as tested --- > RUN mkdir -p usr/include; cp -r /usr/include/openssl /usr/include/boost usr/include/ ; \
        mkdir -p usr/lib; cp -r /usr/lib/libboost_system-mt.so.1.67.0 /usr/lib/libboost_program_options-mt.so.1.67.0 /usr/lib/libgcc_s.so.1 usr/lib/ ; \
        cp -r /usr/lib/libstdc\+\+.so.6.0.25 usr/lib/libstdc\+\+.so.6

# 1:

FROM alpine
COPY --from=0 /root/trojan-gfw/usr /usr
# Below is your path to config.json and certificate.crt and private.key
VOLUME [ "/usr/local/etc/trojan" ]
ENTRYPOINT [ "trojan", "--config", "/usr/local/etc/trojan/config.json" ]
EXPOSE 443
