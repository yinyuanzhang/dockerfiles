FROM r-base:3.5.2
MAINTAINER math2306@hotmail.com

RUN apt-get -qq update && \
    apt-get -qqy install libcurl4-openssl-dev libssl-dev && \
    apt-get -qq clean autoclean &&\
    apt-get -qq autoremove --yes &&\
    rm -rf /var/lib/{apt,dpkg,cache,log}/

RUN  R --slave -e "install.packages(c('https://cran.r-project.org/src/contrib/crayon_1.3.4.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/stringdist_0.9.5.1.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/assertthat_0.2.1.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/cli_1.1.0.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/R6_2.4.0.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/digest_0.6.18.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/rlang_0.3.3.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/withr_2.1.2.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/praise_1.0.0.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/magrittr_1.5.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/testthat_2.0.1.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/sys_3.1.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/askpass_1.1.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/pkgconfig_2.0.2.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/igraph_1.2.4.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/rstudioapi_0.10.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/mime_0.6.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/openssl_1.3.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/curl_3.3.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/jsonlite_1.6.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/httr_1.4.0.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/evaluate_0.13.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/highr_0.8.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/markdown_0.9.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/glue_1.3.1.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/stringi_1.4.3.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/stringr_1.4.0.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/yaml_2.2.0.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/xfun_0.5.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/knitr_1.22.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/lazyeval_0.2.2.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/rex_1.1.2.tar.gz',\
                                      'https://cran.r-project.org/src/contrib/lintr_1.0.3.tar.gz'\
                                    ), \
                                    repo=NULL, \
                                    type='source')"

ADD lint.sh /usr/local/bin/lint
CMD ["bash"]
