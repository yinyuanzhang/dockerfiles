FROM node as builder
# builds commonui-bs3-2019 - maybe unnecessary?
RUN cd /opt && \
    git clone --recurse-submodules https://github.com/AtlasOfLivingAustralia/commonui-bs3-2019.git && \
    cd commonui-bs3-2019 && \
    git submodule foreach --recursive 'git checkout commonui-bs3-2019' && \
    yarn install && \
    ./node_modules/.bin/gulp build

FROM nginx:alpine

# commonui-bs3 ("native" ALA commonui-bs3)
RUN wget https://github.com/AtlasOfLivingAustralia/commonui-bs3/archive/master.zip && \
    unzip master.zip && \
    mv commonui-bs3-master /usr/share/nginx/html/commonui-bs3 && \
    rm master.zip

# commonui-bs2 ("native" ALA commonui-bs2)
RUN wget https://github.com/AtlasOfLivingAustralia/commonui-bs2/archive/master.zip && \
    unzip master.zip && \
    mv commonui-bs2-master /usr/share/nginx/html/commonui-bs2 && \
    rm master.zip

# commonui-bs3-2019
RUN mkdir -p /usr/share/nginx/html/commonui-bs3-2019/
COPY --from=builder /opt/commonui-bs3-2019/build /usr/share/nginx/html/commonui-bs3-2019/

ADD ./html /usr/share/nginx/html

#COPY cors.conf /etc/nginx/conf.d/default.conf

# replace-string para corrigir domains (kubernetes)
#COPY ./scripts/* /opt/

# muda entrypoint, mantém cmd
#ENTRYPOINT ["/opt/ala-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]

