FROM banzaicloud/mkdocs:latest
WORKDIR /documents
COPY ./ /documents
ARG GIT_COMMIT=HEAD
RUN sed -i mkdocs.yml -e "s/#BANZAI_COMMIT#/${GIT_COMMIT}/" -e "s/#DATE#/$(date)/"
RUN mkdocs build

FROM nginx:1.15-alpine

COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=0 /documents/site/ /usr/share/nginx/html/docs/

CMD ["nginx", "-g", "daemon off;"]
