FROM codenvy/ubuntu_jdk8

RUN sudo apt-get update && \
    sudo apt-get install g++ gcc make gdb gdbserver -y && \
    sudo apt-get clean && \
    sudo apt-get -y autoremove && \
    sudo rm -rf /var/lib/apt/lists/*

WORKDIR /home/user

RUN wget https://s3.amazonaws.com/jruby.org/downloads/9.1.2.0/jruby-bin-9.1.2.0.tar.gz && \
    tar zxf jruby-bin-9.1.2.0.tar.gz && \
    rm -rf jruby-bin-9.1.2.0.tar.gz && \
    mv jruby-9.1.2.0 jruby
    
RUN wget https://static.rust-lang.org/dist/rust-1.9.0-x86_64-unknown-linux-gnu.tar.gz && \
    tar zxf rust-1.9.0-x86_64-unknown-linux-gnu.tar.gz && \
    rm -rf rust-1.9.0-x86_64-unknown-linux-gnu.tar.gz && \
    mv rust-1.9.0-x86_64-unknown-linux-gnu rust && \
    mv rust/rust-std-x86_64-unknown-linux-gnu/lib/rustlib/x86_64-unknown-linux-gnu/ rust/rustc/lib/rustlib/
    
RUN sed -i '$ d' /home/user/.bashrc && \
    echo "export PATH=/home/user/jruby/bin:/home/user/rust/rustc/bin:/home/user/rust/cargo/bin:$PATH" >> /home/user/.bashrc

WORKDIR /projects

CMD tail -f /dev/null
