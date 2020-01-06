# LaTeX with Japanese
# docker run --rm -it -v $(pwd):/work pottava/latex:2019jp uplatex sample.tex
# docker run --rm -it -v $(pwd):/work pottava/latex:2019jp dvipdfmx sample.dvi

FROM pottava/latex:2019

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
