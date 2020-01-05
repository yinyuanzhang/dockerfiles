FROM coresystem/acestream

# RemoteFork
# https://docs.microsoft.com/en-us/dotnet/core/linux-prerequisites?tabs=netcore2x
RUN apt-get update -y && apt-get install -y curl liblttng-ust0 libcurl4 libssl1.0.0 libkrb5-3 zlib1g libicu60 libunwind8 libuuid1 \
	&& rm -f /start.sh
COPY app /app
   
# add services
ADD start.sh /start.sh
RUN chmod +x /start.sh
