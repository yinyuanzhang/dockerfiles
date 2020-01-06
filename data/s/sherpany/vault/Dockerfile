FROM vault:1.1.3

USER root

RUN apk add --no-cache iputils curl \
    && touch /.vault-token \
    && chown -R 1001:0 /vault/config /.vault-token \
    && export VAULT_PATH=$(readlink -f $(which vault)) \
    && cp ${VAULT_PATH} ${VAULT_PATH}-ipc \
    && setcap cap_ipc_lock=+ep ${VAULT_PATH}-ipc

USER 1001
