# Start from proteintrees to reuse as much as possible
FROM muffato/ensembl-linuxbrew-compara-proteintrees

RUN /home/linuxbrew/repos/install_cask.sh compara

# Mark all the casks as installed
RUN /home/linuxbrew/repos/install_cask.sh compara-ncrnatrees  \
 && /home/linuxbrew/repos/install_cask.sh compara-speciestree \
 && /home/linuxbrew/repos/install_cask.sh compara-lastz       \
 && /home/linuxbrew/repos/install_cask.sh compara-epo

