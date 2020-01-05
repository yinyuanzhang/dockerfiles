FROM busybox

COPY ./gotop /gotop

COPY ./ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2

ENTRYPOINT ["/gotop"]
