FROM islasgeci/jupyter:3691

RUN pip install --upgrade pip && \
    pip install \
    git+https://github.com/IslasGECI/descarga_datos.git@v0.1.0-beta \
    pandasql

RUN curl -L http://mirrors.ctan.org/macros/latex/contrib/pythontex.zip --output /tmp/pythontex.zip && \
    unzip /tmp/pythontex.zip -d /tmp && \
    cd /tmp/pythontex && \
    latex pythontex.ins && \
    mkdir ~/texmf/tex --parents && \
    mv * ~/texmf/tex && \
    chmod +x ~/texmf/tex/pythontex.py && \
    ln --symbolic ~/texmf/tex/pythontex.py /usr/local/bin/pythontex
