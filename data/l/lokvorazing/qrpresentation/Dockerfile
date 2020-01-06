FROM mcr.microsoft.com/dotnet/core/aspnet:2.2-stretch-slim AS base

RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN ln -s /usr/lib/libgdiplus.so /usr/lib/gdiplus.dll

WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build
WORKDIR /src
COPY ["Services/QRCodeAttendance/QRCodeAttendance.Presentation/QRCodeAttendance.Presentation.csproj", "Services/QRCodeAttendance/QRCodeAttendance.Presentation/"]
COPY ["Common/Zing.Common/Zing.Common.csproj", "Common/Zing.Common/"]
RUN dotnet restore "Services/QRCodeAttendance/QRCodeAttendance.Presentation/QRCodeAttendance.Presentation.csproj"
COPY . .
WORKDIR "/src/Services/QRCodeAttendance/QRCodeAttendance.Presentation"
RUN dotnet build "QRCodeAttendance.Presentation.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "QRCodeAttendance.Presentation.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "QRCodeAttendance.Presentation.dll"]