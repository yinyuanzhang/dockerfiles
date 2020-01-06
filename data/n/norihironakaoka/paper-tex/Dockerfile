FROM debian:stable-slim

LABEL  maintainer "NorihiroNakaoka <dev.pylori1229@gmail.com>"

RUN apt update && \
apt upgrade -y && \
apt install fonts-ipafont fonts-ipaexfont texlive texlive-formats-extra texlive-science texlive-lang-japanese latexmk pandoc -y && \
apt purge *-doc* *chinese* *korean* *thai* -y && \
apt clean -y && \
apt autoremove -y && \
apt autoclean -y
