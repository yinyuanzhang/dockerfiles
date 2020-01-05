FROM julia:latest
MAINTAINER Michael Gant (gntmic002@myuct.ac.za)

RUN julia -e 'import Pkg; Pkg.update()' && \
    julia -e 'import Pkg.add, Pkg.PackageSpec; add(PackageSpec(url="https://github.com/GantZA/LunoAPI.jl", rev="master"))' && \
    julia -e 'import Pkg.add, Pkg.PackageSpec; add(PackageSpec(url="https://github.com/GantZA/TelegramAPI.jl", rev="master"))' && \
    # Precompile Julia packages \
    julia -e 'using LunoAPI, TelegramAPI'

WORKDIR /app

COPY luno-autotrader/ /app/
