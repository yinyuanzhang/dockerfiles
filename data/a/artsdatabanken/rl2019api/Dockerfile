FROM steinhoem/rl2019api
RUN groupadd --gid 1007 dockerrunner && \
	useradd -r --uid 1007 -g dockerrunner dockerrunner
RUN mkdir /app/logs
RUN chmod g+w /app/logs
RUN chown -R :dockerrunner /app
EXPOSE 8000
ENTRYPOINT ["dotnet", "Prod.Api.dll", "--urls=http://rl2019api.artsdatabanken.no:8000"]