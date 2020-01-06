FROM golang:1.12.9
LABEL maintainer suzakinishi <ccyansnow@gmail.com>

# install dependence

RUN apt-get update  \
 && curl --silent --location https://deb.nodesource.com/setup_10.x | bash - \
 && apt-get install -y -f vim apt-utils git build-essential flex bison libgmp-dev libssl-dev cmake nodejs net-tools expect\
 && rm -rf /var/lib/apt/lists/*    \
# download golang deps 
 && echo "download golang deps"  \ 
 && mkdir -p $GOPATH/src/golang.org/x  \ 
 && cd $GOPATH/src/golang.org/x  \
 && git clone https://go.googlesource.com/crypto  --depth 1  \
 && git clone https://go.googlesource.com/tools  --depth 1  \
 && git clone https://go.googlesource.com/sys --depth 1  \
 && git clone https://go.googlesource.com/text --depth 1  \
 && git clone https://go.googlesource.com/net --depth 1  \
 && mkdir -p $GOPATH/src/google.golang.org  \ 
 && cd $GOPATH/src/google.golang.org  \
 && git clone https://github.com/grpc/grpc-go.git grpc  --depth 1  \
 && git clone https://github.com/google/go-genproto.git genproto  --depth 1  \
 # download ipfs deps
 && echo "download ipfs deps"  \ 
 && echo "download github.com/cheekybits/genny ..."  \ 
 && go get -u github.com/cheekybits/genny  \ 
 && echo "download github.com/hashicorp/golang-lru ..."  \ 
 && go get -u github.com/hashicorp/golang-lru  \
 && echo "download github.com/lucas-clemente/aes12  ..."  \ 
 && go get -u github.com/lucas-clemente/aes12  \
 && echo "download github.com/lucas-clemente/quic-go-certificates ..."  \ 
 && go get -u github.com/lucas-clemente/quic-go-certificates  \
 && echo "download github.com/golang/protobuf ..."  \ 
 && git clone https://github.com/golang/protobuf.git /go/src/github.com/golang/protobuf --depth 1   \
 && echo "download github.com/gogo/protobuf ..."  \ 
 && git clone https://github.com/gogo/protobuf.git /go/src/github.com/gogo/protobuf --depth 1   \
 && echo "download github.com/ncw/gmp ..."  \ 
 && git clone https://github.com/ncw/gmp.git /go/src/github.com/ncw/gmp --depth 1   \
 # download tendeermint deps 
 && echo "download tendeermint deps"  \ 
 && echo "github.com/go-kit/kit ..."  \ 
 && git clone https://github.com/go-kit/kit.git /go/src/github.com/go-kit/kit --depth 1\
 && echo "download github.com/go-logfmt/logfmt ..."  \  
 && go get -u github.com/go-logfmt/logfmt  \
 && echo "download github.com/gorilla/websocket ..."  \ 
 && go get -u github.com/gorilla/websocket  \
 && echo "download github.com/rcrowley/go-metrics ..."  \ 
 && go get -u github.com/rcrowley/go-metrics  \
 && echo "download github.com/syndtr/goleveldb ..."  \ 
 && git clone https://github.com/syndtr/goleveldb.git /go/src/github.com/syndtr/goleveldb  --depth 1\
 && echo "download github.com/golang/snappy ..."  \ 
 && go get -u github.com/golang/snappy  \
 && echo "download github.com/rs/cors ..."  \ 
 && go get -u github.com/rs/cors  \
 && echo "download github.com/spf13/cobra ..."  \ 
 && go get -u github.com/spf13/cobra  \ 
 && echo "download github.com/spf13/viper ..."  \ 
 && go get -u github.com/spf13/viper  \
 && echo "download github.com/tendermint/go-amino ..."  \ 
 && go get -u github.com/tendermint/go-amino  \
 && echo "download github.com/btcsuite/btcd ..."  \ 
 && go get -u github.com/btcsuite/btcd  \
 && echo "download github.com/prometheus/client_golang ..."  \ 
 && git clone https://github.com/prometheus/client_golang.git /go/src/github.com/prometheus/client_golang --depth 1\
 && echo "download github.com/prometheus/client_model  ..."  \ 
 && git clone https://github.com/prometheus/client_model.git /go/src/github.com/prometheus/client_model --depth 1\
 && echo "download github.com/prometheus/common ..."  \ 
 && git clone https://github.com/prometheus/common.git /go/src/github.com/prometheus/common --depth 1\
 && echo "download github.com/prometheus/procfs ..."  \ 
 && go get -u github.com/prometheus/procfs  \
 && echo "download github.com/pkg/errors  ..."  \ 
 && go get -u github.com/pkg/errors  \
 && echo "download github.com/beorn7/perks  ..."  \ 
 && git clone https://github.com/beorn7/perks.git /go/src/github.com/beorn7/perks --depth 1 \
 && echo "download github.com/matttproud/golang_protobuf_extensions ..."  \ 
 && git clone https://github.com/matttproud/golang_protobuf_extensions.git /go/src/github.com/matttproud/golang_protobuf_extensions --depth 1   \
 && echo "download github.com/bifurcation/mint  ..."  \ 
 && go get -u github.com/bifurcation/mint   \ 
 && echo "reset mint for compile"   \ 
 && cd $GOPATH/src/github.com/bifurcation/mint   \ 
 && git reset --hard 824af65410658916142a7600349144e1289f2110   \ 
 && echo "download github.com/xcshuan/go-mefs-api ..."  \ 
 && git clone https://github.com/xcshuan/go-mefs-api.git /go/src/github.com/xcshuan/go-mefs-api --depth 1   \  
 # download tendermint source
 && echo "download tendermint source"  \ 
 && mkdir -p $GOPATH/src/github.com/tendermint  \
 && cd $GOPATH/src/github.com/tendermint  \ 
 && git clone https://github.com/tendermint/tendermint.git  \
 && echo "reset tendermint for compile"   \ 
 && cd $GOPATH/src/github.com/tendermint/tendermint   \ 
 && git reset --hard 4253e67c07c69be6d7f7263ab03944ce30a9fc90   \ 
 # download ethereum source
 && echo "download ethereum source"  \ 
 && mkdir -p $GOPATH/src/github.com/ethereum  \
 && cd $GOPATH/src/github.com/ethereum  \ 
 && git clone https://github.com/ethereum/go-ethereum.git   \
 # install mcl 
 && echo "install mcl"\
 && mkdir -p $GOPATH/src/mcl  \
 && cd $GOPATH/src/mcl  \
 && git clone https://github.com/herumi/mcl.git  \ 
 && cd mcl  \
 && mkdir build  \
 && cd build  \
 && cmake ..  \
 && make -j 24  \
 && make install  \
 && ldconfig  \
# install mefs-test 
 && echo "install mefs-test"\
 && echo "mefs-http-api-test version 0.0.62"  \
 && mkdir -p $GOPATH/mefs-http-api-test \
 && cd $GOPATH/mefs-http-api-test  \
 && npm install mefs-http-client  \ 
 # install golangci-lint
 && echo "install golangci-lint"\
 && curl -sfL https://install.goreleaser.com/github.com/golangci/golangci-lint.sh | sh -s -- -b $(go env GOPATH)/bin v1.17.1 \
 && echo "download github.com/golang/mock/gomock ..."  \ 
 && go get -u github.com/golang/mock/gomock \
 && echo "download github.com/onsi/gomega ..."  \ 
 && go get -u github.com/onsi/gomega    \
 && echo "download gopkg.in/check.v1 ..."  \ 
 && go get -u gopkg.in/check.v1 \
 && echo "download github.com/onsi/ginkgo ..."  \ 
 && go get -u github.com/onsi/ginkgo    \
 && echo "download github.com/jbenet/go-cienv ..."  \ 
 && go get -u github.com/jbenet/go-cienv    \
 && echo "download gopkg.in/cheggaaa/pb.v1 ..."  \ 
 && go get -u gopkg.in/cheggaaa/pb.v1   \
 && echo "download github.com/lucas-clemente/quic-clients ..."  \ 
 && go get -u github.com/lucas-clemente/quic-clients    \
 && echo "download github.com/smartystreets/goconvey/convey ..."  \ 
 && go get -u github.com/smartystreets/goconvey/convey  \
 && echo "download github.com/warpfork/go-wish ..."  \ 
 && go get -u github.com/warpfork/go-wish  \
 && echo "download github.com/stretchr/testify/assert ..."  \ 
 && go get -u github.com/stretchr/testify/assert  \
 && echo "download github.com/dustin/go-humanize ..."  \ 
 && go get -u github.com/dustin/go-humanize  \