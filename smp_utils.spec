Summary:	Utilities for SAS Management Protocol (SMP)
Summary(pl):	Narzêdzia do protoko³u SAS Management Protocol (SMP)
Name:		smp_utils
Version:	0.91
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://www.torque.net/sg/p/%{name}-%{version}.tgz
# Source0-md5:	b5edc77a4bc06d4d0c4a08fb374b2231
Patch0:		%{name}-make.patch
URL:		http://www.torque.net/sg/smp_utils.html
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

%description -l pl
Ten pakiet zawiera narzêdzia, z których ka¿de wysy³a ¿±danie Serial
Attached SCSI (SAS) Management Protocol (SMP) do urz±dzenia SMP. Je¶li
¿±danie nie powiedzie siê, b³±d jest dekodowany. Je¶li ¿±danie
powiedzie siê, odpowied¼ jest dekodowana i wypisywana w postaci
szesnastkowej lub wyprowadzana binarnie. Ten pakiet obs³uguje wiele
interfejsów, jako ¿e przekazywanie SMP nie jest jeszcze dojrza³e. Ten
pakiet obs³uguje Linuksa zarówno z serii 2.4 jak i 2.6 i powinien byæ
³atwy do sportowania na inne systemy operacyjne.

Uwaga: niektóre z narzêdzi operuj± na wnêtrzno¶ciach systemu i ich
nieprawid³owe u¿ycie mo¿e spowodowaæ niezdatno¶æ systemu do dalszej
pracy.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

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
