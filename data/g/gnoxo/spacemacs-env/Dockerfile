FROM gnoxo/spacemacs-env:latex

COPY scripts/install-packages.r $UHOME/install-packages.r

COPY latex-r/.spacemacs $UHOME/.spacemacs

RUN apt-get update \
   && apt-get install -y r-base \
   && apt-get autoremove -y \
   && curl https://codeload.github.com/emacs-ess/ESS/tar.gz/v17.11 --output ess.tar.gz \
   && mkdir $UHOME/.emacs.d/private/local/ESS \
   && tar xvf ess.tar.gz -C $UHOME/.emacs.d/private/local/ESS --strip-components=1 \
   && echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile \
   && Rscript $UHOME/install-packages.r \
   && rm ess.tar.gz $UHOME/install-packages.r \
   && rm -rf /tmp/* /var/lib/apt/lists/* /root/.cache/*

RUN install-deps

