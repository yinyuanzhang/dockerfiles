FROM rustlang/rust:nightly
ENV ROCKET_ADDRESS=0.0.0.0
ENV ROCKET_PORT=8080
WORKDIR /web
COPY . .
RUN mkdir -p ./share
VOLUME /web/share
WORKDIR /web/app
RUN cargo install --path .
RUN mv target/release/fuzen_info /bin/fuzen_info
WORKDIR /web
RUN rm -rf /web/app
EXPOSE 8080
CMD /bin/fuzen_info
