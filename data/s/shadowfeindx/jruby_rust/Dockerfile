FROM codenvy/ubuntu_jdk8

RUN sudo apt-get update && \
    sudo apt-get install g++ gcc make gdb gdbserver -y && \
    sudo apt-get clean && \
    sudo apt-get -y autoremove && \
    sudo rm -rf /var/lib/apt/lists/*
    
RUN sed -i '$ d' /home/user/.bashrc && \
    echo "export PATH=/home/user/che/jruby/bin:/home/user/che/rust/rustc/bin:/home/user/che/rust/cargo/bin:$PATH" >> /home/user/.bashrc

CMD tail -f /dev/null
