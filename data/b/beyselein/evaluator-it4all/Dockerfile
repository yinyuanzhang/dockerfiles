FROM hseeberger/scala-sbt:11.0.4_1.3.0_2.13.1

ARG DIST_DIR=/opt/dist
ARG SOURCE_DIR=/root/source

COPY . ${SOURCE_DIR}

RUN mkdir ${DIST_DIR} && \
    cd ${SOURCE_DIR} && \
    sbt packageZipTarball && \
    ls -al && \
    tar -xzf ./target/universal/evaluator-it4all.tgz -C ${DIST_DIR}/ && \
    rm -r ${SOURCE_DIR}

WORKDIR ${DIST_DIR}/evaluator-it4all

ENTRYPOINT ./bin/evaluator-it4all -Dplay.http.secret.key="3if9ßsd8vzaßs9d8vzaßs9c8vz" -Dplay.evolutions.db.default.autoApply=true
