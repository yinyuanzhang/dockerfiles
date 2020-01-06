###############################################################################
# FRONTEND
###############################################################################
FROM node:10.1.0 as frontend

RUN mkdir app
WORKDIR app

COPY frontend/package.json frontend/yarn.lock ./
RUN yarn install

ADD frontend .

RUN node_modules/.bin/brunch build --production

###############################################################################
# BACKEND
###############################################################################
FROM liuchong/rustup:nightly-musl as backend

RUN mkdir -p app/src
WORKDIR app

COPY Cargo.toml Cargo.lock ./
RUN touch src/lib.rs \
    && cargo build --release \
    && rm -r src

ADD . .
RUN rm -rf frontend && mkdir frontend

COPY --from=frontend /app/public frontend/public

RUN cargo build --release

###############################################################################
# FINAL IMAGE
###############################################################################
FROM scratch

COPY --from=backend /root/app/target/x86_64-unknown-linux-musl/release/geuze /

ENV ROCKET_ENV=production
ENV ROCKET_PORT=8000

EXPOSE 8000

ENTRYPOINT ["/geuze"]
