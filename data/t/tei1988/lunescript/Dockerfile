FROM tei1988/lua:5.2.4-alpine3.9 AS lunescript

USER root
RUN apk --no-cache add \
      git \
      make
RUN git clone --depth 1 https://github.com/ifritJP/LuneScript.git &&\
    cd LuneScript
WORKDIR LuneScript/src
RUN lua setup.lua -d
RUN make install

FROM tei1988/lua:5.2.4-alpine3.9

COPY --from=lunescript /usr/bin/lnsc /usr/bin/lnsc
COPY --from=lunescript /usr/local/share/lua/5.2 /usr/share/lua/5.2
