FROM microsoft/dotnet:2.1.3-aspnetcore-runtime-stretch-slim
RUN mkdir -p /home/appuser
RUN groupadd -g 1000 appuser && \
    useradd -r -g appuser -d /home/appuser -s /sbin/nologin -c "Docker image user" appuser
ENV HOME=/home/appuser
ENV APP_HOME=/home/appuser/app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
RUN chown -R appuser:appuser $HOME
RUN chown -R appuser:appuser $APP_HOME
ADD newrelic-netcore20-agent_8.6.45.0_amd64.tar.gz /home/appuser/app/newrelic
ADD VERSION .
ENV CORECLR_ENABLE_PROFILING="1" \
COMPlus_TieredCompilation=1 \
CORECLR_PROFILER="{36032161-FFC0-4B61-B559-F6C5D41BAE5A}" \
CORECLR_NEWRELIC_HOME="/home/appuser/app/newrelic/newrelic-netcore20-agent" \
CORECLR_PROFILER_PATH="/home/appuser/app/newrelic/newrelic-netcore20-agent/libNewRelicProfiler.so"
RUN chown -R appuser:appuser /$HOME
USER appuser