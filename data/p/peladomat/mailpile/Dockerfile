FROM alpine:latest
MAINTAINER Matias Vidal <matias@m01.cl>

ENV VERSION master

# Install requirements
RUN apk add --update-cache \
        shadow \
        git \
        zlib \
        gnupg1 \
        py2-pip \
        openssl \
        py-jinja2 \
        py-libxml2 \
        py-libxslt \
        py-lxml \
        py-pbr \
        py-pillow \
        py-cffi \
        py-cryptography \
        ca-certificates

## CREATE APP USER ##

# Create the home directory for the new app user.
RUN mkdir -p /home/mailpile

# Create an app user so our program doesn't run as root.
RUN groupadd -r mailpile &&\
    useradd -r -g mailpile -d /home/mailpile -s /sbin/nologin -c "MailPile user" mailpile

# Set the home directory to our app user's home.
ENV HOME=/home/mailpile

WORKDIR $HOME

# Chown all the files to the app user.
RUN chown -R mailpile:mailpile $HOME

# Change to the app user.
USER mailpile

# Get Mailpile from github
RUN git clone https://github.com/mailpile/Mailpile.git \
        --branch $VERSION --single-branch --recursive

WORKDIR $HOME/Mailpile

# Install missing requirements
RUN pip install --user -r requirements.txt

# Initial Mailpile setup
RUN ./mp setup

# set the http_path
RUN ./mp set sys.http_path /mailpile

CMD ./mp --www=0.0.0.0:33411 --wait
EXPOSE 33411

VOLUME /home/mailpile/.local/share/Mailpile
VOLUME /home/mailpile/.gnupg
