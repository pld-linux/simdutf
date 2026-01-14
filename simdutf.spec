Summary:	Text processing at billions of characters per second
Name:		simdutf
Version:	8.0.0
Release:	1
License:	Apache v2.0 or MIT
Group:		Libraries
#Source0Download: https://github.com/simdutf/simdutf/releases
Source0:	https://github.com/simdutf/simdutf/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	da16902283c2f7af81687ebadf44c4da
URL:		https://simdutf.github.io/simdutf/
BuildRequires:	cmake >= 3.15
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode routines (UTF8, UTF16, UTF32) and Base64: billions of
characters per second using SSE2, AVX2, NEON, AVX-512, RISC-V Vector
Extension, LoongArch64, POWER.

%package devel
Summary:	Header files for simdutf library
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libstdc++-devel%{?_isa}

%description devel
Header files for simdutf library.

%package tools
Summary:	simdutf based tools for text encoding conversion
Group:		Applications/Text
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description tools
simdutf based tools for text encoding conversion.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS LICENSE-MIT README.md
%{_libdir}/libsimdutf.so.*.*.*
%ghost %{_libdir}/libsimdutf.so.31

%files devel
%defattr(644,root,root,755)
%{_libdir}/libsimdutf.so
%{_includedir}/simdutf
%{_includedir}/simdutf.h
%{_includedir}/simdutf_c.h
%{_libdir}/cmake/simdutf
%{_pkgconfigdir}/simdutf.pc

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fastbase64
%attr(755,root,root) %{_bindir}/sutf
