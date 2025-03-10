Name: xdriinfo
Version: 1.0.7
Release: 1
Summary: X application to query configuration information of DRI drivers
License: MIT
URL: https://gitlab.freedesktop.org/xorg/app/xdriinfo
Source0: https://www.x.org/releases/individual/app/%{name}-%{version}.tar.xz

# This package was split from the mesa-demos package, which used to
# also build and install xdriinfo until mesa-demos-9.0.0
Conflicts: mesa-demos < 9.0.0

BuildRequires: make gcc
BuildRequires: pkgconfig(glproto)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xorg-macros) >= 1.8
BuildRequires: libGL-devel

%description
xdriinfo can be used to query configuration information of direct
rendering drivers.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/xdriinfo
%{_mandir}/man1/xdriinfo.1*

%changelog
* Mon Jan 27 2025 Funda Wang <fundawang@yeah.net> - 1.0.7-1
- init package
