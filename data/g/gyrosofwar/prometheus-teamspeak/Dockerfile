FROM rust:latest
WORKDIR /app
COPY . .
RUN cargo build --release
RUN cargo install --path .
CMD ["/usr/local/cargo/bin/prometheus-teamspeak"]