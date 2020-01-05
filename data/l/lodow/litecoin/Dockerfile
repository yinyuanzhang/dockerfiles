FROM ubuntu:18.04 as build

RUN apt-get update && apt-get install -y wget gpg && \
    wget https://download.litecoin.org/litecoin-0.17.1/linux/litecoin-0.17.1-x86_64-linux-gnu.tar.gz && \
    wget https://download.litecoin.org/litecoin-0.17.1/linux/litecoin-0.17.1-linux-signatures.asc

#  https://blog.litecoin.org/litecoin-core-v0-17-1-release-7cf1207ee833 
# "For this release, the binaries have been signed with key identifier FE3348877809386C (thrasher’s key)"
RUN gpg --keyserver pgp.mit.edu --recv-key FE3348877809386C || \ 
    gpg --keyserver keyserver.ubuntu.com --recv-key FE3348877809386C && \
    gpg --verify litecoin-0.17.1-linux-signatures.asc && \
    cat litecoin-0.17.1-linux-signatures.asc | grep  litecoin-0.17.1-x86_64-linux-gnu.tar.gz | sha256sum --check --status && \
    tar xzf litecoin-0.17.1-x86_64-linux-gnu.tar.gz
   
FROM ubuntu:18.04

RUN mkdir /home/app && groupadd app && useradd -g app -d /home/app app && chown app:app -R /home/app
COPY --from=build /litecoin-0.17.1 /home/app/litecoin
RUN chown app:app -R /home/app/litecoin

USER app

EXPOSE 9332

CMD ["/home/app/litecoin/bin/litecoind"]

