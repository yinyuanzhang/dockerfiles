FROM microsoft/dotnet:2.2-sdk AS build-env
WORKDIR /app

COPY Stratox.Miotiq.Billing.Sim ./Stratox.Miotiq.Billing.Sim
COPY Stratox.Miotiq.Billing.Common ./Stratox.Miotiq.Billing.Common
RUN dotnet restore Stratox.Miotiq.Billing.Sim/*.csproj
RUN dotnet publish Stratox.Miotiq.Billing.Sim/*.csproj -c Release -o out

FROM microsoft/dotnet:2.2-aspnetcore-runtime
WORKDIR /app
COPY --from=build-env /app/Stratox.Miotiq.Billing.Sim/out .
ENTRYPOINT ["dotnet", "Stratox.Miotiq.Billing.Sim.dll"]
