FROM passcod/ccv-base
MAINTAINER Félix Saparelli <me@passcod.name>
CMD ["ccv"]
EXPOSE 3350

RUN git clone --depth=1 git://github.com/liuliu/ccv.git /source &&\
    cd /source/lib && ./configure && make -j$(nproc) &&\
    cd ../serve && make -j$(nproc) && cd .. &&\
    rm -rf .git bin doc js site test &&\
\
    echo '#!/bin/sh\ncd /source/serve; ./ccv $*' > /bin/ccv &&\
    chmod +x /bin/ccv

