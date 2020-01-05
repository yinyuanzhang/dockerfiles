#Definimos a imagem basea qual nossa aplicação vai se basear
FROM nginx:1.17.0-alpine
#Definimos o nome do mantenedor, seja ele uma pessoa ou instituição
LABEL maintainer="Miudo <miudo@gmail.com>"
#Copiamos o conteudo estatico pro nosso servidor
COPY ./arquivos /usr/share/nginx/html
#Copiamos uma configuração pro nginx que servirá para expor nosso site ao msm tempo que faz o proxy
#COPY ./web-proxy/localhost.conf /etc/nginx/conf.d/default.conf
#Expomos a porta 80
EXPOSE 80
#Definimos o sinal de stop como o sinal de termino da aplicação
STOPSIGNAL SIGTERM
#Definimos o comando inicial que inicializa o nginx com o modo daemon desligado
CMD ["nginx", "-g", "daemon off;"]
