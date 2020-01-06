FROM node:10.15.1 as builder-history

# compile all to dev

WORKDIR /app
COPY ./history/ .

RUN npm install -g yarn
RUN yarn
RUN PUBLIC_URL=https://gf6-dev.clickbit.net/history \
    REACT_APP_ASSET_PATH=https://cdn-dev.clickbit.net/gf6assets \
    yarn build

FROM node:10.15.1 as builder-tables

WORKDIR /app
COPY ./tables/ .
COPY ./tables/emptySession.json /app/app/core/commonSession.json

RUN npm install -g yarn
RUN yarn
RUN yarn build

FROM node:10.15.1 as builder-slots

WORKDIR /app
COPY ./slots/ .

RUN npm install -g yarn
RUN yarn
RUN PUBLIC_URL=https://gf6-dev.clickbit.net/slot \
    REACT_APP_ASSET_PATH=https://cdn-dev.clickbit.net/gf6assets \
    yarn build


FROM nginx:stable

RUN mkdir -p /var/www
COPY --from=builder-tables /app/dist/ /var/www

RUN mkdir -p /var/www/history
COPY --from=builder-history /app/build/ /var/www/history

RUN mkdir -p /var/www/slot
COPY --from=builder-slots /app/build/ /var/www/slot

RUN ln -s /var/www/slot/ /var/www/43
RUN ln -s /var/www/slot/ /var/www/1043
RUN ln -s /var/www/slot/ /var/www/46
RUN ln -s /var/www/slot/ /var/www/1046
RUN ln -s /var/www/slot/ /var/www/49
RUN ln -s /var/www/slot/ /var/www/1049
RUN ln -s /var/www/slot/ /var/www/52
RUN ln -s /var/www/slot/ /var/www/1052
RUN ln -s /var/www/slot/ /var/www/55
RUN ln -s /var/www/slot/ /var/www/1055
RUN ln -s /var/www/slot/ /var/www/58
RUN ln -s /var/www/slot/ /var/www/1058
RUN ln -s /var/www/slot/ /var/www/61
RUN ln -s /var/www/slot/ /var/www/1061
RUN ln -s /var/www/slot/ /var/www/64
RUN ln -s /var/www/slot/ /var/www/1064
RUN ln -s /var/www/slot/ /var/www/68
RUN ln -s /var/www/slot/ /var/www/1068
RUN ln -s /var/www/slot/ /var/www/73
RUN ln -s /var/www/slot/ /var/www/1073
RUN ln -s /var/www/slot/ /var/www/76
RUN ln -s /var/www/slot/ /var/www/1076
RUN ln -s /var/www/slot/ /var/www/79
RUN ln -s /var/www/slot/ /var/www/1079
RUN ln -s /var/www/slot/ /var/www/80
RUN ln -s /var/www/slot/ /var/www/1080
RUN ln -s /var/www/slot/ /var/www/81
RUN ln -s /var/www/slot/ /var/www/1081
RUN ln -s /var/www/slot/ /var/www/328
RUN ln -s /var/www/slot/ /var/www/1328
RUN ln -s /var/www/slot/ /var/www/333
RUN ln -s /var/www/slot/ /var/www/1333
RUN ln -s /var/www/slot/ /var/www/339
RUN ln -s /var/www/slot/ /var/www/1339
RUN ln -s /var/www/slot/ /var/www/344
RUN ln -s /var/www/slot/ /var/www/1344
RUN ln -s /var/www/slot/ /var/www/349
RUN ln -s /var/www/slot/ /var/www/1349
RUN ln -s /var/www/slot/ /var/www/354
RUN ln -s /var/www/slot/ /var/www/1354
RUN ln -s /var/www/slot/ /var/www/359
RUN ln -s /var/www/slot/ /var/www/1359
RUN ln -s /var/www/slot/ /var/www/364
RUN ln -s /var/www/slot/ /var/www/1364
RUN ln -s /var/www/slot/ /var/www/369
RUN ln -s /var/www/slot/ /var/www/1369
RUN ln -s /var/www/slot/ /var/www/374
RUN ln -s /var/www/slot/ /var/www/1374
RUN ln -s /var/www/slot/ /var/www/379
RUN ln -s /var/www/slot/ /var/www/1379
RUN ln -s /var/www/slot/ /var/www/384
RUN ln -s /var/www/slot/ /var/www/1384
RUN ln -s /var/www/slot/ /var/www/389
RUN ln -s /var/www/slot/ /var/www/1389
RUN ln -s /var/www/slot/ /var/www/394
RUN ln -s /var/www/slot/ /var/www/1394
RUN ln -s /var/www/slot/ /var/www/399
RUN ln -s /var/www/slot/ /var/www/1399
RUN ln -s /var/www/slot/ /var/www/404
RUN ln -s /var/www/slot/ /var/www/1404
RUN ln -s /var/www/slot/ /var/www/409
RUN ln -s /var/www/slot/ /var/www/1409
RUN ln -s /var/www/slot/ /var/www/414
RUN ln -s /var/www/slot/ /var/www/1414
RUN ln -s /var/www/slot/ /var/www/420
RUN ln -s /var/www/slot/ /var/www/1420
RUN ln -s /var/www/slot/ /var/www/425
RUN ln -s /var/www/slot/ /var/www/1425
RUN ln -s /var/www/slot/ /var/www/432
RUN ln -s /var/www/slot/ /var/www/1432
RUN ln -s /var/www/slot/ /var/www/450
RUN ln -s /var/www/slot/ /var/www/1450
RUN ln -s /var/www/slot/ /var/www/455
RUN ln -s /var/www/slot/ /var/www/1455

RUN ln -s /var/www/slot/ /var/www/550
RUN ln -s /var/www/slot/ /var/www/555
RUN ln -s /var/www/slot/ /var/www/560
RUN ln -s /var/www/slot/ /var/www/565
RUN ln -s /var/www/slot/ /var/www/570
RUN ln -s /var/www/slot/ /var/www/575
RUN ln -s /var/www/slot/ /var/www/580
RUN ln -s /var/www/slot/ /var/www/585
RUN ln -s /var/www/slot/ /var/www/590
RUN ln -s /var/www/slot/ /var/www/595
RUN ln -s /var/www/slot/ /var/www/600
RUN ln -s /var/www/slot/ /var/www/605

RUN ln -s /var/www/slot/ /var/www/902
RUN ln -s /var/www/slot/ /var/www/905
RUN ln -s /var/www/slot/ /var/www/908
RUN ln -s /var/www/slot/ /var/www/911
RUN ln -s /var/www/slot/ /var/www/914
RUN ln -s /var/www/slot/ /var/www/919
RUN ln -s /var/www/slot/ /var/www/923
RUN ln -s /var/www/slot/ /var/www/928
RUN ln -s /var/www/slot/ /var/www/933
RUN ln -s /var/www/slot/ /var/www/938
RUN ln -s /var/www/slot/ /var/www/943
RUN ln -s /var/www/slot/ /var/www/948

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
