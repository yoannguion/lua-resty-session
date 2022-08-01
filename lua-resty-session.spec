%define lua_dir	%{_datarootdir}/lua
%define lua_dir_resty	%{lua_dir}/5.3/resty

Name: lua-resty-session
Summary: Session library for for ngx_lua and LuaJIT
Version: 3.10
Release: 3
URL: https://github.com/yoannguion/lua-resty-session
License: BSD
Provides: Session library for ngx_lua and LuaJIT
Requires: lua-resty-string
BuildArch: noarch

%description
Session library for ngx_lua and LuaJIT


%install
mkdir -p $RPM_BUILD_ROOT%{lua_dir_resty}
cp -rf %{_sourcedir}/lib/resty/* $RPM_BUILD_ROOT%{lua_dir_resty}

%files
%{lua_dir_resty}/session.lua
%{lua_dir_resty}/session/ciphers/aes.lua
%{lua_dir_resty}/session/ciphers/none.lua
%{lua_dir_resty}/session/compressors/zlib.lua
%{lua_dir_resty}/session/compressors/none.lua
%{lua_dir_resty}/session/encoders/hex.lua
%{lua_dir_resty}/session/encoders/base16.lua
%{lua_dir_resty}/session/encoders/base64.lua
%{lua_dir_resty}/session/hmac/sha1.lua
%{lua_dir_resty}/session/identifiers/random.lua
%{lua_dir_resty}/session/serializers/json.lua
%{lua_dir_resty}/session/storage/cookie.lua
%{lua_dir_resty}/session/storage/dshm.lua
%{lua_dir_resty}/session/storage/memcache.lua
%{lua_dir_resty}/session/storage/memcached.lua
%{lua_dir_resty}/session/storage/redis.lua
%{lua_dir_resty}/session/storage/shm.lua
%{lua_dir_resty}/session/strategies/default.lua
%{lua_dir_resty}/session/strategies/regenerate.lua



%changelog
* Mon Aug 01 2022 Yoann GUION <yoann.guion@gmail.com> - 3.10-3
- Initial release 3.10
