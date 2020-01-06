FROM mendersoftware/useradm:1.7.0

RUN ln -s /run/secrets/useradm_key /etc/useradm/rsa/private.pem

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh", "--config", "/etc/useradm/config.yaml"]
