FROM haskell
RUN useradd -u 1000 -m jenkins
USER jenkins
RUN cd /home/jenkins && \
  cabal new-update && \
  cabal new-install --overwrite-policy=always happy && \
  cabal new-install --overwrite-policy=always hlint && \
  rm -rf /home/jenkins/.stack/*
ENV PATH /home/jenkins/.cabal/bin:/home/jenkins/.local/bin:$PATH
CMD ["/bin/bash"]