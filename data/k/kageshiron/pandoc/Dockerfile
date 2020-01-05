FROM aruneko/texlive

RUN apt-get update && apt-get install -y python3-pip jq wget
# pandoc
RUN wget -qO- https://api.github.com/repos/jgm/pandoc/releases/latest | \
    jq '.assets[] | select(.content_type == "application/x-gzip").browser_download_url' | \
    xargs wget -qO- | \
    tar xvz --strip-components 1 -C /usr/local/

# pandoc-crossref
RUN wget -qO- https://api.github.com/repos/lierdakil/pandoc-crossref/releases/latest | \
    jq '.assets[] | select(.name | startswith("linux")).browser_download_url' | \
    xargs wget -qO- | \
    tar xvz --strip-components 1 -C /usr/local/bin/

RUN pip3 install --upgrade pandocfilters Pygments pandoc-minted 
RUN tlmgr install luatexbase ctablestack fontspec luaotfload lualatex-math
RUN apt purge -y wget jq \
    && apt autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists

VOLUME ["/workspace", "/root/.pandoc/templates"]
WORKDIR /workspace 
