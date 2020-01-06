FROM helphi/wkhtmltopdf:0.12.4-win7fonts

RUN wget --no-check-certificate https://github.com/jgm/pandoc/releases/download/2.4/pandoc-2.4-1-amd64.deb -O pandoc-2.4-1-amd64.deb &&\
    dpkg -i pandoc-2.4-1-amd64.deb &&\
    rm -rf pandoc-2.4-1-amd64.deb

CMD [ "pandoc", "--help" ]