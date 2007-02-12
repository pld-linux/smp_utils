Summary:	Utilities for SAS Management Protocol (SMP)
Summary(pl.UTF-8):   Narzędzia do protokołu SAS Management Protocol (SMP)
Name:		smp_utils
Version:	0.92
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://sg.torque.net/sg/p/%{name}-%{version}.tgz
# Source0-md5:	431bd3413347b04868fca018c4bbdf17
Patch0:		%{name}-make.patch
URL:		http://sg.torque.net/sg/smp_utils.html
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

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} \$(EXTRA_FLAGS)" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
 	PREFIX=%{_prefix} \
 	INSTDIR=$RPM_BUILD_ROOT%{_bindir} \
 	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG COPYING README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
