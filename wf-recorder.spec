Name     : wf-recorder
Version  : 0.5.0
Release  : 1
URL      : https://github.com/ammen99/wf-recorder
Source0  : https://github.com/ammen99/wf-recorder/archive/refs/tags/v%{version}.tar.gz
Summary  : Utility program for screen recording of wlroots-based compositors
Group    : Development/Tools
License  : MIT
Requires : sway
BuildRequires :  meson cmake
BuildRequires :  not-ffmpeg-dev
BuildRequires :  mesa-dev
BuildRequires :  pkgconfig(scdoc)  
BuildRequires :  pkgconfig(libpulse)
BuildRequires :  pkgconfig(wayland-client)
BuildRequires :  pkgconfig(wayland-cursor)
BuildRequires :  pkgconfig(wayland-protocols)

%description
Utility program for screen recording of wlroots-based compositors

%prep
%setup -q -n wf-recorder-%{version}

%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=release   builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
strip %{buildroot}/usr/bin/wf-recorder
rm -rf %{buildroot}/usr/share/man

%files
%defattr(-,root,root,-)
/usr/bin/wf-recorder
