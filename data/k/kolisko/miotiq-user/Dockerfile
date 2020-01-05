FROM microsoft/dotnet:2.2-sdk AS build-env
WORKDIR /app

COPY Stratox.Miotiq.Billing.User ./Stratox.Miotiq.Billing.User
COPY Stratox.Miotiq.Billing.Common ./Stratox.Miotiq.Billing.Common
RUN dotnet restore Stratox.Miotiq.Billing.User/*.csproj
RUN dotnet publish Stratox.Miotiq.Billing.User/*.csproj -c Release -o out

FROM microsoft/dotnet:2.2-aspnetcore-runtime
WORKDIR /app
COPY --from=build-env /app/Stratox.Miotiq.Billing.User/out .
ENTRYPOINT ["dotnet", "Stratox.Miotiq.Billing.User.dll"]
