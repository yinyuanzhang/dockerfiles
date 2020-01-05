FROM mammo0/armv7hf-debian-qemu AS armBin


FROM arm32v6/node:8-alpine as builder
COPY --from=armBin /usr/bin/cross-build-start /usr/bin/
COPY --from=armBin /usr/bin/cross-build-end /usr/bin/
COPY --from=armBin /usr/bin/qemu-arm-static /usr/bin/
COPY --from=armBin /usr/bin/resin-xbuild /usr/bin/
RUN [ "cross-build-start" ]
RUN apk add -U build-base python jq
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN yarn add --force package.json && \
    yarn build && \
    yarn remove $(cat package.json | jq -r '.devDependencies | keys | join(" ")')
RUN [ "cross-build-end" ]


FROM arm32v6/node:8-alpine
LABEL maintainer="butlerx@notthe.cloud"
LABEL maintainer="marc.ammon@fau.de"

ENV PORT=3000
ENV SSHHOST=localhost
ENV SSHPORT=22

WORKDIR /usr/src/app
ENV NODE_ENV=production
COPY --from=armBin /usr/bin/cross-build-start /usr/bin/
COPY --from=armBin /usr/bin/cross-build-end /usr/bin/
COPY --from=armBin /usr/bin/qemu-arm-static /usr/bin/
COPY --from=armBin /usr/bin/resin-xbuild /usr/bin/
RUN [ "cross-build-start" ]
RUN apk add -U openssh-client sshpass
COPY --from=builder /usr/src/app/dist /usr/src/app/dist
COPY --from=builder /usr/src/app/node_modules /usr/src/app/node_modules
COPY package.json /usr/src/app
COPY index.js /usr/src/app
RUN mkdir ~/.ssh
RUN ssh-keyscan -H wetty-ssh >> ~/.ssh/known_hosts
RUN [ "cross-build-end" ]
EXPOSE $PORT

ENTRYPOINT [ "node", "." ]
