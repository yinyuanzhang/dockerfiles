FROM blackikeeagle/alpine:edge

ENV C_USER node

COPY ./container /container
RUN /container/install-node.sh

WORKDIR /nodeapp

ENTRYPOINT ["/entrypoint.sh"]
CMD ["node"]
