FROM rustlang/rust:nightly as build

RUN USER=root cargo new --bin bonamy
WORKDIR /bonamy

COPY ./Cargo.lock ./Cargo.lock
COPY ./Cargo.toml ./Cargo.toml

RUN cargo build --release
RUN rm src/*.rs

COPY ./ ./

RUN rm ./target/release/deps/bonamy*
RUN cargo build --release

FROM debian:stable-slim

COPY --from=build /bonamy .

CMD ["./target/release/bonamy"]