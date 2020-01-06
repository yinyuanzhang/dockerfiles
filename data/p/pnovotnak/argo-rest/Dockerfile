FROM golang:1.10 AS compiler
WORKDIR /go/src/github.com/CyrusBiotechnology/argo-rest
COPY vendor/ /go/src/
COPY pkg ./pkg
COPY server ./server
# Compile a static binary
RUN CGO_ENABLED=0 GOOS=linux \
    go build -a -ldflags '-extldflags "-static"' \
    -o /go/bin/argo-rest-server ./server

FROM node:8 AS ui
ENV NODE_ENV development
WORKDIR /
COPY ui ./ui
WORKDIR ./ui
RUN npm install git://github.com/substack/node-mkdirp.git \
    &&  npm install --only=dev \
    && npm install -g sass react-scripts-ts typescript react
RUN sass src/App.scss src/App.css \
    && sass src/Header.scss src/Header.css \
    && sass src/Status.scss src/Status.css \ 
    && sass src/WorkflowViewer/WorkflowViewer.scss src/WorkflowViewer/WorkflowViewer.css
RUN npm run build

FROM centos
ENV NODE_ENV production
COPY --from=compiler /go/bin/argo-rest-server /argo-rest-server
COPY --from=ui /ui/build /react-ui
EXPOSE 80
ENTRYPOINT ["./argo-rest-server"]
