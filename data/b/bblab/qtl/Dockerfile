FROM r-base:3.5.2

# Add R libraries under /tmp
COPY libs/* /tmp/
COPY src/map_qtl.R /tmp/map_qtl.R
# Install R packages
RUN Rscript -e "install.packages(c('snow','optparse', 'tictoc'))" && \
R CMD INSTALL '/tmp/RandomForestExtended.tar.gz'  && \
R CMD INSTALL '/tmp/RFQTL_diploid_v2_JW.tar.gz' && \
chmod a+x /tmp/map_qtl.R
# Define entrypoint
USER docker
ENTRYPOINT ["Rscript", "--vanilla", "/tmp/map_qtl.R"]
