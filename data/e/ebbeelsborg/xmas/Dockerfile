FROM rust:1.37-slim as build
COPY . .
RUN cargo build --release

FROM ubuntu:latest
LABEL maintainer="Ebbe Elsborg"
COPY --from=build /target/release/xmas .
CMD ["./xmas"]
