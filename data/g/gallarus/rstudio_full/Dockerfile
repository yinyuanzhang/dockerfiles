FROM rocker/geospatial:latest

# install htop
RUN apt-get install -y --no-install-recommends htop

# install R packages 
# verify that they are not already presents before adding them
RUN install2.r --error corrplot ggpubr psy MatchIt tableone pROC cobalt icd \
    DBI MonetDBLite ggmap fmsb survminer optmatch plotly profvis formula.tools \
    ggfortify pryr segmented lobstr bench codetools testthat withr tailr ggridges \ 
    EpiModel shiny rlang caret xgboost randomForest pdp moments  ggrepel desctable \
    ClustOfVar callr cowplot simmer arkdb fs tinytex ggcorrplot \
    drake txtq visNetwork skimr rticles here pkgnet reprex \
    foreach future future.callr doFuture future.batchtools RefManageR citr \
    # tidymodels \
# and those from github
    && Rscript -e 'devtools::install_github("IM-APHP/pmeasyr")' \
    && Rscript -e 'devtools::install_github("rstudio/gt")' \
    && Rscript -e 'devtools::install_github("ropenscilabs/gramr")' \
    && Rscript -e 'devtools::install_github("AdrienLeGuillou/descriptor")' 
    

# copy rstudio server user settings
COPY user-settings /home/rstudio/

RUN mkdir -p /home/rstudio/.rstudio/monitored/user-settings /home/rstudio/work \
    && mv /home/rstudio/user-settings /home/rstudio/.rstudio/monitored/user-settings/ \
    && chown -R rstudio:rstudio /home/rstudio
