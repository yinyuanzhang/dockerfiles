FROM debian

RUN apt update
RUN apt install -y curl libexpat1

RUN curl --output ejabberd_17.01-0_amd64.deb --location https://www.process-one.net/downloads/downloads-action.php?file=/ejabberd/17.01/ejabberd_17.01-0_amd64.deb
RUN dpkg -i ejabberd_17.01-0_amd64.deb
RUN rm ejabberd_17.01-0_amd64.deb

ENV PATH=/opt/ejabberd-17.01/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LC_ALL=C.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

CMD ["ejabberdctl","foreground"]
