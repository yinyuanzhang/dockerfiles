FROM alpine:latest 
RUN apk update
RUN apk add bash alpine-sdk cmake gmp-dev boost-dev mpfr-dev ncurses
RUN mkdir /opt
WORKDIR /opt
RUN git clone https://github.com/ledger/ledger
WORKDIR /opt/ledger
RUN ./acprep update
RUN make install
WORKDIR /root
ADD bashrc /root/.bashrc
ADD git-completion.bash /root/.git-completion.bash
ADD ledgerrc /root/.ledgerrc
ADD journal /root/journal
VOLUME /var/ledger
