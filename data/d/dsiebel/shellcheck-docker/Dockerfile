# ------------------------------------------------------------- shellcheck-build

ARG SHELLCHECK_BUILDER_BASE_IMAGE="fleshgrinder/debian:stretch-build"
ARG SHELLCHECK_BASE_IMAGE="fleshgrinder/debian:stretch"

FROM ${SHELLCHECK_BUILDER_BASE_IMAGE} AS shellcheck-build

ARG SHELLCHECK_VERSION_REF="master"

RUN apt-install git ghc cabal-install \
 && mkdir -p /usr/src/shellcheck \
 && cd /usr/src/shellcheck \
 && git clone https://github.com/koalaman/shellcheck.git . \
 && git checkout ${SHELLCHECK_VERSION_REF} \
 && cabal update && cabal install

ENV PATH="$PATH:/root/.cabal/bin"

RUN mkdir -p  /package/bin /package/lib \
 && cp $(which shellcheck) /package/bin/ \
 && ldd $(which shellcheck) | grep "=> /" | awk '{print $3}' | xargs -I '{}' cp -v '{}' /package/lib/

# ------------------------------------------------------------------- shellcheck

FROM ${SHELLCHECK_BASE_IMAGE} AS shellcheck

COPY --from=shellcheck-build /package/bin/ /usr/local/bin/
COPY --from=shellcheck-build /package/lib/ /usr/local/lib/
COPY resources/docker/bin/shellcheckw /usr/local/bin/shellcheckw

RUN apt-install bash file \
 && ldconfig /usr/local/lib

ENTRYPOINT ["shellcheckw"]
