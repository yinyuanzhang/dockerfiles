FROM okuisatoshi/docker_coq_ssr
RUN sudo apt-get update && sudo apt-get install -yq wget unzip
RUN opam install -y depext && opam depext -y frama-c
RUN opam install -y frama-c
RUN opam install -y why3

RUN wget http://www.cs.nyu.edu/acsys/cvc3/releases/2.4.1/linux64/cvc3-2.4.1-optimized-static.tar.gz \
    && tar -xzf cvc3-2.4.1-optimized-static.tar.gz && sudo cp -R cvc3-2.4.1-optimized-static/* /usr/local/
    
RUN wget http://cvc4.cs.stanford.edu/downloads/builds/x86_64-linux-opt/unstable/cvc4-latest-x86_64-linux-opt \
    && sudo cp cvc4-latest-x86_64-linux-opt /usr/local/bin/cvc4 && sudo chmod +x /usr/local/bin/cvc4

RUN wget https://github.com/Z3Prover/z3/releases/download/z3-4.4.1/z3-4.4.1-x64-ubuntu-14.04.zip \
    && unzip z3-4.4.1-x64-ubuntu-14.04.zip && sudo cp z3-4.4.1-x64-ubuntu-14.04/bin/z3 /usr/local/bin \
    && sudo chmod +x /usr/local/bin/z3

RUN eval `opam config env` && /home/opam/.opam/4.04.0/bin/why3 config --detect




    

    
    















