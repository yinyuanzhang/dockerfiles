FROM hermantolim/nodejs-chrome:latest

WORKDIR /home/app

ENV TZ=Asia/Jakarta \
    NODE_NO_WARNINGS=1 \
    NODE_PENDING_DEPRECATION=1 \
    NODE_ENV=production \
    NODE_DEBUG=false

COPY ./app ./build
RUN mv ./build/bin ./build/lib ./build/package.json ./ \
    && rm -rf build \
    && chown -R app:app /home/app

ENTRYPOINT ["/sbin/my_init", "--"]

RUN /sbin/setuser app npm run build

CMD ["/sbin/setuser", "app", "npm", "run", "worker"]
