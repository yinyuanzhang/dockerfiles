FROM golang
RUN git clone https://github.com/gohugoio/hugo.git /hugo
RUN cd /hugo && go install

COPY . /site
WORKDIR /site

RUN hugo -v

# Minify things
RUN go get github.com/tdewolff/minify/cmd/minify
RUN minify -vr --match=\.js --type=js -o public public
RUN minify -vr --match=\.css --type=css -o public public
RUN minify -vr --match=\.html --type=html -o public public

# Proper image
FROM nginx:alpine
LABEL maintainer "Mickael BERNARDINI <mikafouenski@gmail.com>"
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=0 /site/public /usr/share/nginx/html

