# Sphinx v2.0 with Japanese
#
# docker run --rm -v `pwd`:/doc -w /doc pottava/sphinx:2.0jp /bin/sh -c "make clean && make latex && cd _build/latex && uplatex -interaction=nonstopmode sample.tex && dvipdfmx sample.dvi"

FROM pottava/sphinx:2.0

RUN apk --no-cache add --virtual build-deps wget perl \
    && tlmgr install collection-latexrecommended \
    && fc-cache -fv && apk del --purge -r build-deps \
    && find / -depth -type f -name *.eps -exec rm -rf {} \; \
    && find / -depth -type f -name *.pdf -exec rm -rf {} \;

RUN apk --no-cache add --virtual build-deps wget perl \
    && tlmgr install collection-fontsrecommended \
    && fc-cache -fv && apk del --purge -r build-deps \
    && find / -depth -type f -name *.eps -exec rm -rf {} \; \
    && find / -depth -type f -name *.pdf -exec rm -rf {} \;

RUN apk --no-cache add --virtual build-deps wget perl \
    && tlmgr install collection-latexextra \
    && fc-cache -fv && apk del --purge -r build-deps \
    && find / -depth -type f -name *.eps -exec rm -rf {} \; \
    && find / -depth -type f -name *.pdf -exec rm -rf {} \;

RUN apk --no-cache add --virtual build-deps wget perl \
    && tlmgr install collection-langjapanese \
    && fc-cache -fv && apk del --purge -r build-deps \
    && find / -depth -type f -name *.eps -exec rm -rf {} \; \
    && find / -depth -type f -name *.pdf -exec rm -rf {} \;
