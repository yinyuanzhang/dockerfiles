FROM parity/parity:beta

COPY . .

USER root
RUN chmod 777 entrypoint.sh
USER parity

RUN mkdir -p ~/.local/share/io.parity.ethereum/signer

ENTRYPOINT ["./entrypoint.sh"]
