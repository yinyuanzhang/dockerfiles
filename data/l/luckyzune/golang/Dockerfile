FROM luckyzune/golang:alpinegcc
LABEL MAINTAINER QiMa "mq@luckyzune.com"
LABEL builder_version="9.1.19"

# 更新常用的go lib
RUN go get -u github.com/btcsuite/btcutil/... && go get -u github.com/fsnotify/fsnotify/... && go get -u github.com/hashicorp/hcl/... && go get -u github.com/ryanuber/columnize && go get -u github.com/Joker/jade && go get -u github.com/aymerick/raymond/... && go get -u github.com/eknkc/amber && go get -u github.com/flosch/pongo2 && go get -u github.com/axgle/mahonia && go get -u github.com/chanxuehong/rand && go get -u github.com/golang/protobuf/... && go get -u github.com/gorilla/websocket && go get -u github.com/labstack/gommon/log && go get -u github.com/op/go-logging && go get -u github.com/tealeg/xlsx && go get -u github.com/spf13/cobra && go get -u github.com/spf13/viper && go get -u github.com/kataras/iris/... && go get -u github.com/kataras/golog && go get -u github.com/kataras/go-errors && go get -u github.com/eclipse/paho.mqtt.golang && go get -u github.com/go-pg/pg && go get -u github.com/streadway/amqp && go get -u github.com/garyburd/redigo/redis && go get -u golang.org/x/net/http2 && go get -u gopkg.in/chanxuehong/wechat.v2/... && go get -u gopkg.in/yaml.v2  && go get -u gopkg.in/mgo.v2  && go get -u github.com/opentracing/opentracing-go  && go get -u sourcegraph.com/sourcegraph/appdash  && go get -u github.com/dinever/golf  && go get -u github.com/satori/go.uuid  && go get -u github.com/juju/errors  && go get -u github.com/lib/pq && go get -u github.com/rs/cors  && go get -u github.com/bitly/go-simplejson  && go get -u github.com/mholt/archiver  && go get -u github.com/gomodule/redigo/...  && go get -u gonum.org/v1/gonum/...  && go get -u github.com/kniren/gota/... && go get -u  github.com/emirpasic/gods/...  && go get -u github.com/ulikunitz/xz && go get -u github.com/pierrec/xxHash/... && go get -u github.com/pierrec/lz4 && go get -u github.com/nwaples/rardecode && go get -u github.com/golang/snappy && go get -u github.com/dsnet/compress

#8.5.18
RUN go get -u github.com/Sirupsen/logrus && go get -u golang.org/x/net/webdav

#8.5.22
RUN go get -u github.com/asdine/storm  && go get -u github.com/coreos/bbolt && go get -u github.com/hacdias/fileutils && go get -u gopkg.in/natefinch/lumberjack.v2 && go get -u github.com/GeertJohan/go.rice && go get -u github.com/daaku/go.zipexe  && go get -u github.com/kardianos/osext && go get -u github.com/BurntSushi/toml && go get -u github.com/chaseadamsio/goorgeous && go get -u github.com/russross/blackfriday && go get -u github.com/shurcooL/sanitized_anchor_name && go get -u github.com/PuerkitoBio/purell && go get -u github.com/PuerkitoBio/urlesc && go get -u github.com/alecthomas/chroma && go get -u github.com/mholt/caddy && go get -u github.com/robfig/cron  && go get -u github.com/dgrijalva/jwt-go && go get -u github.com/hacdias/varutils && go get -u github.com/flynn/go-shlex && go get -u github.com/google/uuid && go get -u github.com/robfig/cron && go get -u golang.org/x/crypto/blowfish && go get -u github.com/dgrijalva/jwt-go/request && go get -u golang.org/x/crypto/bcrypt

#8.5.23
# && go get -u github.com/abiosoft/caddyplug
RUN go get -u github.com/abiosoft/errs && go get -u github.com/fatih/color/... && go get -u github.com/abiosoft/errs && go get -u github.com/hashicorp/go-syslog && go get -u github.com/bifurcation/mint/syntax && go get -u golang.org/x/crypto/curve25519 && go get -u golang.org/x/crypto/hkdf && go get -u github.com/hashicorp/golang-lru/simplelru && go get -u github.com/lucas-clemente/aes12 && go get -u github.com/hashicorp/golang-lru && go get -u golang.org/x/text/transform && go get -u github.com/russross/blackfriday && go get -u gopkg.in/natefinch/lumberjack.v2


#8.9.28
RUN go get -u github.com/mohae/deepcopy && go get -u github.com/360EntSecGroup-Skylar/excelize && go get -u github.com/go-redis/redis/... && go get -u github.com/rdegges/go-ipify && go get -u github.com/jpillora/backoff && go get -u github.com/go-sql-driver/mysql

#9.1.5
RUN go get -u github.com/go-openapi/errors && go get -u github.com/go-openapi/runtime/... && go get -u github.com/go-openapi/loads && go get -u github.com/go-openapi/strfmt && go get -u github.com/go-openapi/analysis/... && go get -u github.com/go-openapi/swag && go get -u github.com/go-openapi/validate && go get -u github.com/go-openapi/jsonpointer && go get -u github.com/go-openapi/spec && go get -u github.com/go-openapi/jsonreference 
 
RUN go get -u github.com/asaskevich/govalidator && go get -u github.com/globalsign/mgo  && go get -u github.com/mailru/easyjson && go get -u github.com/skip2/go-qrcode && go get -u github.com/aliyun/aliyun-oss-go-sdk

#9.1.11
RUN go get -u github.com/xlstudio/wxbizdatacrypt

#9.1.28
RUN go get -u github.com/pkg/errors
 
#9.2.2
RUN go get -u github.com/yireyun/go-queue && go get -u github.com/gorilla/mux && go get -u sourcegraph.com/sourcegraph/appdash-data
RUN go get -u github.com/aeternity/aepp-sdk-go

#9.5.13
RUN go get -u github.com/ethereum/go-ethereum

#9.6.30
RUN go get -u github.com/nats-io/go-nats && go get -u github.com/nats-io/nkeys && go get -u github.com/nats-io/nuid && go get -u github.com/hashicorp/consul
RUN go get -u github.com/go-xorm/core && go get -u github.com/go-xorm/xorm
RUN go get -u github.com/mitchellh/hashstructure && go get -u github.com/pborman/uuid

#9.8.21 
RUN go get -u golang.org/x/sync/syncmap

WORKDIR /go/src/github.com/luckyzune/golang/
ADD builder .

RUN mkdir -p /root/.ssh/
COPY builder/id_rsa /root/.ssh/id_rsa 
RUN chmod 600 /root/.ssh/id_rsa
COPY builder/id_rsa.pub /root/.ssh/id_rsa.pub
COPY builder/.gitconfig /root/.gitconfig

RUN mkdir -p /etc/ssh/ && echo 'IdentityFile ~/.ssh/id_rsa'  >> /etc/ssh/ssh_config && sed -i 's/#   StrictHostKeyChecking ask/StrictHostKeyChecking no/' /etc/ssh/ssh_config
