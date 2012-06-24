Summary:	Utilities for SAS Management Protocol (SMP)
Summary(pl):	Narz�dzia do protoko�u SAS Management Protocol (SMP)
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
Ten pakiet zawiera narz�dzia, z kt�rych ka�de wysy�a ��danie Serial
Attached SCSI (SAS) Management Protocol (SMP) do urz�dzenia SMP. Je�li
��danie nie powiedzie si�, b��d jest dekodowany. Je�li ��danie
powiedzie si�, odpowied� jest dekodowana i wypisywana w postaci
szesnastkowej lub wyprowadzana binarnie. Ten pakiet obs�uguje wiele
interfejs�w, jako �e przekazywanie SMP nie jest jeszcze dojrza�e. Ten
pakiet obs�uguje Linuksa zar�wno z serii 2.4 jak i 2.6 i powinien by�
�atwy do sportowania na inne systemy operacyjne.

Uwaga: niekt�re z narz�dzi operuj� na wn�trzno�ciach systemu i ich
nieprawid�owe u�ycie mo�e spowodowa� niezdatno�� systemu do dalszej
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
