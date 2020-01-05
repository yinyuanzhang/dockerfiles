FROM microsoft/dotnet:2.1-sdk

MAINTAINER <vk@alphacloud.net>

RUN dotnet tool install --global dotnet-outdated \
    && dotnet tool install --global nukeeper

COPY DependencyCache.csproj /work/cache/

RUN cd /work/cache \
    && dotnet add package AWSSDK.Core \
    && dotnet add package AWSSDK.Extensions.NETCore.Setup \
    && dotnet add package AWSSDK.IdentityManagement \
    && dotnet add package AWSSDK.KeyManagementService \
    && dotnet add package AWSSDK.S3 \
    && dotnet add package AWSSDK.SQS \
    && dotnet add package AWSSDK.SimpleNotificationService \
    && dotnet add package AngleSharp \
    && dotnet add package AutoFixture \
    && dotnet add package AutoMapper \
    && dotnet add package Autofac \
    && dotnet add package Autofac.Extensions.DependencyInjection \
    && dotnet add package Autofac.Extras.DynamicProxy \
    && dotnet add package Autofac.Extras.Moq \
    && dotnet add package Autofac.Extras.Quartz \
    && dotnet add package Automapper \
    && dotnet add package Castle.Core \
    && dotnet add package Confluent.Kafka \
    && dotnet add package Dapper \
    && dotnet add package FluentAssertions \
    && dotnet add package FluentValidation \
    && dotnet add package FluentValidation.AspNetCore \
    && dotnet add package Humanizer.Core \
    && dotnet add package JetBrains.Annotations \
    && dotnet add package LibLog \
    && dotnet add package MOQ \
    && dotnet add package MassTransit \
    && dotnet add package MassTransit.Autofac \
    && dotnet add package MassTransit.Automatonymous \
    && dotnet add package MassTransit.Extensions.DependencyInjection \
    && dotnet add package MassTransit.MongoDb \
    && dotnet add package MassTransit.RabbitMQ \
    && dotnet add package MassTransit.Redis \
    && dotnet add package MassTransit.SerilogIntegration -v 5.* \
    && dotnet add package MassTransit.TestFramework \
    && dotnet add package MediatR \
    && dotnet add package MediatR.Extensions.Microsoft.DependencyInjection \
    && dotnet add package MessagePack \
    && dotnet add package MessagePackAnalyzer \
    && dotnet add package Microsoft.AspNetCore.Mvc.Testing \
    && dotnet add package Microsoft.AspNetCore.SignalR \
    && dotnet add package Microsoft.AspNetCore.SignalR.Common \
    && dotnet add package Microsoft.AspNetCore.SignalR.Protocols.Json \
    && dotnet add package Microsoft.AspNetCore.SignalR.Protocols.MessagePack \
    && dotnet add package Microsoft.CSharp \
    && dotnet add package Microsoft.CodeAnalysis.CSharp \
    && dotnet add package Microsoft.Extensions.Caching.Memory \
    && dotnet add package Microsoft.Extensions.Http.Polly \
    && dotnet add package Microsoft.IO.RecyclableMemoryStream \
    && dotnet add package MongoDB.Driver \
    && dotnet add package NHibernate \
    && dotnet add package Newtonsoft.Json \
    && dotnet add package Polly \
    && dotnet add package Polly.Caching.IDistributedCache \
    && dotnet add package Polly.Caching.MemoryCache \
    && dotnet add package Polly.Extensions.Http \
    && dotnet add package Quartz \
    && dotnet add package RabbitMQ \
    && dotnet add package RedLock.net \
    && dotnet add package RedLock.net.StrongName \
    && dotnet add package Serilog \
    && dotnet add package Serilog.AspNetCore \
    && dotnet add package Serilog.Exceptions \
    && dotnet add package Serilog.Extensions.Logging \
    && dotnet add package Serilog.Sinks.ColoredConsole \
    && dotnet add package Serilog.Sinks.File \
    && dotnet add package StackExchange.Redis \
    && dotnet add package SwashBuckle.AspNetCore.Examples \
    && dotnet add package Swashbuckle.AspNetCore \
    && dotnet add package System.Buffers \
    && dotnet add package System.ComponentModel.Annotations \
    && dotnet add package System.ComponentModel.Primitives \
    && dotnet add package System.Data.SqlClient \
    && dotnet add package System.Dynamic.Runtime \
    && dotnet add package System.Linq.Queryable \
    && dotnet add package System.Reflection.Emit \
    && dotnet add package System.Reflection.TypeExtensions \
    && dotnet add package System.Reflection.TypeExtensions \
    && dotnet add package System.Reflection.TypeExtensions \
    && dotnet add package System.Runtime.Loader \
    && dotnet add package System.Security.SecureString \
    && dotnet add package System.Threading.Tasks.Extensions \
    && dotnet add package System.ValueTuple \
    && dotnet add package System.Xml.XmlSerializer \
    && dotnet add package librdkafka.redist \
    && dotnet add package xunit \
    && dotnet add package xunit.runner.visualstudio \
    && dotnet restore \
    && cat /work/cache/DependencyCache.csproj \
    && cd / \
    && rm -rf /work/cache/* \
    && echo "# Add .Net Core tools" >> ~/.bash_profile \
    && echo "export PATH=\"\$PATH:/root/.dotnet/tools\"" >> ~/.bash_profile \

#    && dotnet add package MassTransit.RedisSagas \
#    && dotnet add package MassTransit.RedisSagas.RedLock \

