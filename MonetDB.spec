Summary:	Fast database engine
Summary(pl.UTF-8):	Szybki silnik baz danych
Name:		MonetDB
Version:	4.8.2
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/monetdb/%{name}-%{version}.tar.gz
# Source0-md5:	3fafd56f98a02859b04762ab3d601e37
URL:		http://monetdb.cwi.nl/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MonetDB is an open source high-performance database system developed
at CWI, the Institute for Mathematics and Computer Science Research of
The Netherlands. It was designed to provide high performance on
complex queries against large databases, e.g. combining tables with
hundreds of columns and multi-million rows. As such, MonetDB can be
used in application areas that because of performance issues are no-go
areas for using traditional database technology in a real-time manner.
MonetDB has been successfully applied in high-performance applications
for data mining, OLAP, GIS, XML Query, text and multimedia retrieval.

%description -l pl.UTF-8
MonetDB to wysokowydajny system baz danych o otwartych źródłach
tworzony w CWI - Institute for Mathematics and Computer Science
Research of The Netherlands (Instytucie Matematyki i Nauk
Informatycznych Holandii). Został zaprojektowany aby zapewnić wysoką
wydajność przy złożonych zapytaniach dla dużych baz danych, np.
łączących tabele z setkami kolumn i wieloma milionami wierszy. Jako
taki MonetDB może być używany w takich zastosowaniach aplikacyjnych, w
których tradycyjne technologie bazodanowe nie sprawdzały się w czasie
rzeczywistym. MonetDB został z sukcesem zastosowanych w
wysokowydajnych aplikacjach z zakresu górnistwa, OLAP, GIS, zapytań
XML, przetwarzania tekstu i multimediów.

%package devel
Summary:	Header files for MonetDB
Summary(pl.UTF-8):	Pliki nagłówkowe MonetDB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for MonetDB.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe MonetDB.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/{%{name},php}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc HowToStart README
%{_sysconfdir}/MonetDB.conf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.mil
%attr(755,root,root) %{_libdir}/%{name}/*.so.*
%attr(755,root,root) %{_libdir}/%{name}/*.so
# XXX: php-* module?
%attr(755,root,root) %{_libdir}/php/*.so.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.mil
%{_datadir}/%{name}/*.gif
%{_datadir}/%{name}/tools
%{_datadir}/%{name}/Mprofile-commands.lst
%{_datadir}/%{name}/perl
%{_datadir}/%{name}/php
%{_datadir}/%{name}/python

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/MonetDB.pc
%{_datadir}/%{name}/conf
# XXX: missing dir?
%{_libdir}/autogen/*.py
