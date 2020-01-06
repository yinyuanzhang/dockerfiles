from scorpil/rust:1.17

RUN mkdir -p /opt/transmission_bot \
  && apt-get update \
  && apt-get install --no-install-recommends -y libssl-dev \
  && rm -rf rm -rf /var/lib/apt/lists/*

COPY . /opt/transmission_bot

RUN cd /opt/transmission_bot \
  && cargo build --release \
  && cp /opt/transmission_bot/target/release/transmission_bot /opt/bot \
  && rm -rf /opt/transmission_bot

EXPOSE 8080

ENV RUST_LOG=transmission_bot=info

ENTRYPOINT ["/opt/bot"]

CMD [""]
