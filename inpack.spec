[project]
name = redis3
version = 3.2.11
vendor = redis.io
homepage = https://redis.io
groups = dev/db
description = in-memory data structure store

%build

PREFIX="{{.project__prefix}}"

cd {{.inpack__pack_dir}}/deps

if [ ! -f "redis-{{.project__version}}.tar.gz" ]; then
    wget http://redis.org/download/redis-{{.project__version}}.tar.gz
fi
if [ -d "redis-{{.project__version}}" ]; then
    rm -rf redis-{{.project__version}}
fi
tar -zxf redis-{{.project__version}}.tar.gz

cd redis-{{.project__version}}

make -j2

rm -rf   {{.buildroot}}/*
mkdir -p {{.buildroot}}/{bin,conf,data,run,log}

install src/redis-server             {{.buildroot}}/bin/redis-server
install src/redis-cli                {{.buildroot}}/bin/redis-cli
strip -s {{.buildroot}}/bin/redis-server
strip -s {{.buildroot}}/bin/redis-cli

cd {{.inpack__pack_dir}}
install misc/redis.conf.default      {{.buildroot}}/conf/redis.conf.default

rm -rf {{.inpack__pack_dir}}/deps/redis-{{.project__version}}

%files

