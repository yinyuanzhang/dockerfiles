FROM maven:3-jdk-8-slim as builder

# criar pasta para guardar os recursos
#RUN mkdir -p /build

WORKDIR /app

# situacoes em que precisamos mudar as configuracoes do maven
#COPY settings.xml /root/.m2/

# copiar o arquivo de definicoes de dependencias e plugins
COPY pom.xml .

# baixa todas as dependencias em uma camada
RUN mvn -B dependency:resolve dependency:resolve-plugins

# copiar codigo fonte do projeto
COPY src src

# agora que temos o diretorio /build com o pom e o codigo, podemos 'buildar' o projeto e gerar o .jar
RUN mvn package -DskipTests


FROM openjdk:8-jdk-slim as runtime

EXPOSE 8080

# define diretorio da aplicacao em variavel ambiente
ENV APP_HOME /app

# quando precisar mudar as configuracoes do JVM para otimização
ENV JAVA_OPTS=""

# cria diretorio base da aplicação
RUN mkdir $APP_HOME

# cria pasta para salvar os arquivos de configuracao
RUN mkdir $APP_HOME/config

# cria pasta para salvar os logs da aplicacao
RUN mkdir $APP_HOME/logs

# cria volumes para persistir config e logs da aplicacao
VOLUME $APP_HOME/log
VOLUME $APP_HOME/config

WORKDIR $APP_HOME

# finalmente, copia o .jar gerado na imagem builder e renomeia como app.jar
COPY --from=builder /app/target/*.jar app.jar


# existe uma propriedade apontando para '/dev/./urandom' para diminuir o tempo de inicio do TOMCAT
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar app.jar" ]
