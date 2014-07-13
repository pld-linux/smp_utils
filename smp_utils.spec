Summary:	Utilities for SAS Management Protocol (SMP)
Summary(pl.UTF-8):	Narzędzia do protokołu SAS Management Protocol (SMP)
Name:		smp_utils
Version:	0.98
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://sg.danny.cz/sg/p/%{name}-%{version}.tar.xz
# Source0-md5:	545544db04203b9f71f0ecb401e8a30c
URL:		http://sg.danny.cz/sg/smp_utils.html
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a package of utilities. Each utility sends a Serial Attached
SCSI (SAS) Management Protocol (SMP) request to a SMP target. If the
request fails then the error is decoded. If the request succeeds then
the response is either decoded, printed out in hexadecimal or output
in binary. This package supports multiple interfaces since SMP
passthroughs are not mature. This package supports the Linux 2.4 and
2.6 series and should be easy to port to other operating systems.

Warning: Some of these tools access the internals of your system and
the incorrect usage of them may render your system inoperable.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia, z których każde wysyła żądanie Serial
Attached SCSI (SAS) Management Protocol (SMP) do urządzenia SMP. Jeśli
żądanie nie powiedzie się, błąd jest dekodowany. Jeśli żądanie
powiedzie się, odpowiedź jest dekodowana i wypisywana w postaci
szesnastkowej lub wyprowadzana binarnie. Ten pakiet obsługuje wiele
interfejsów, jako że przekazywanie SMP nie jest jeszcze dojrzałe. Ten
pakiet obsługuje Linuksa zarówno z serii 2.4 jak i 2.6 i powinien być
łatwy do sportowania na inne systemy operacyjne.

Uwaga: niektóre z narzędzi operują na wnętrznościach systemu i ich
nieprawidłowe użycie może spowodować niezdatność systemu do dalszej
pracy.

%package devel
Summary:	Header file for SMP Utils library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki SMP Utils
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for SMP Utils library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki SMP Utils.

%package static
Summary:	Static SMP Utils library
Summary(pl.UTF-8):	Statyczna biblioteka SMP Utils
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static SMP Utils library.

%description static -l pl.UTF-8
Statyczna biblioteka SMP Utils.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COVERAGE CREDITS ChangeLog README
%attr(755,root,root) %{_bindir}/smp_*
%attr(755,root,root) %{_libdir}/libsmputils1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmputils1.so.1
%{_mandir}/man8/smp_*.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libsmputils1.so
%{_libdir}/libsmputils1.la
%{_includedir}/scsi/smp_lib.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libsmputils1.a
