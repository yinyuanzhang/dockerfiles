# TODO Compile errors are not handled well.
# [Let `--report=json` also have effect on `elm-test make`](https://github.com/rtfeldman/node-test-runner/issues/293)
# might help getting error messages from compiler. It's not released yet.
FROM node:8.12.0-slim

RUN set -ex; \
    useradd --create-home -u 9999 codewarrior; \
    mkdir /workspace; \
    chown codewarrior:codewarrior /workspace;

RUN yarn global add elm@0.19.0-no-deps elm-test@0.19.0-rev6 --prefix /usr/local

COPY --chown=codewarrior:codewarrior rootfs/workspace/elm/elm.json /workspace/elm/
COPY --chown=codewarrior:codewarrior rootfs/workspace/elm/tests/Example.elm /workspace/elm/tests/

# Need to run as `codewarrior` to avoid "CORRUPT BINARY" error for user submitted code
USER codewarrior
# Run Example.elm to compile dependencies during image build
# avoid compiling with each user submited code
RUN set -ex; \
    cd /workspace/elm; \
    # `src/` needs to exist
    mkdir src/; \
    elm-test --report=json tests/Example.elm; \
    rm -rf elm-stuff tests/Example.elm;

WORKDIR /workspace
ENV USER=codewarrior \
    HOME=/home/codewarrior
