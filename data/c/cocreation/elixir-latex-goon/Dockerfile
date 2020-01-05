FROM elixir:1.7.2-alpine

# Install TeX Live 2018 with some basic collections
RUN apk --no-cache add perl=5.26.2-r1 wget=1.19.5-r0 xz=5.2.4-r0 tar=1.30-r0 && \
    wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \
    mkdir /install-tl-unx && \
    tar -xvf install-tl-unx.tar.gz -C /install-tl-unx --strip-components=1 && \
    echo "selected_scheme scheme-basic" >> /install-tl-unx/texlive.profile && \
    /install-tl-unx/install-tl -profile /install-tl-unx/texlive.profile && \
    apk del perl wget xz tar && \
    rm -r /usr/local/texlive/2018/texmf-dist/doc && \
    rm -r /install-tl-unx && \
    rm install-tl-unx.tar.gz

ENV PATH="/usr/local/texlive/2018/bin/x86_64-linuxmusl/:${PATH}"

# Install additional packages
RUN apk --no-cache add perl=5.26.2-r1 wget=1.19.5-r0 && \
    tlmgr install pdfpages && \
    apk del perl wget && \
    mkdir /workdir

# Install Goon (for Porcelain)
RUN apk --no-cache add perl=5.26.2-r1 wget=1.19.5-r0 xz=5.2.4-r0 tar=1.30-r0 && \
    wget https://github.com/alco/goon/releases/download/v1.1.1/goon_linux_amd64.tar.gz && \
    mkdir /goon_linux_amd64 && \
    tar -xvf goon_linux_amd64.tar.gz -C /goon_linux_amd64 && \
    chmod +x /goon_linux_amd64/goon && \
    mv /goon_linux_amd64/goon /usr/local/bin && \
    apk del perl wget xz tar && \
    rm -r /goon_linux_amd64 && \
    rm goon_linux_amd64.tar.gz

CMD ["iex"]
