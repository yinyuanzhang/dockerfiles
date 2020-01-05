FROM islasgeci/jupyter:ac5d

RUN pip install \
    fastkml \
    git+https://github.com/IslasGECI/descarga_datos.git@v0.1.0-beta \
    git+https://github.com/IslasGECI/distdens.git@v0.1.0 \
    git+https://github.com/IslasGECI/geoambiental.git@v0.1.0 \
    pandasql \
    pymc3

RUN conda install mkl-service
RUN R -e "install.packages(c('jsonlite', 'optparse'), repos = 'http://cran.us.r-project.org')"
RUN apt install texlive-lang-spanish

RUN curl -L http://mirrors.ctan.org/macros/latex/contrib/pythontex.zip --output /tmp/pythontex.zip && \
unzip /tmp/pythontex.zip -d /tmp && \
cd /tmp/pythontex && \
latex pythontex.ins && \
mkdir ~/texmf/tex --parents && \
mv * ~/texmf/tex && \
chmod +x ~/texmf/tex/pythontex.py && \
ln --symbolic ~/texmf/tex/pythontex.py /usr/local/bin/pythontex
