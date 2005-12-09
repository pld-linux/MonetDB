#
Summary:	Fast database engine
Name:		MonetDB
Version:	4.8.2
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/monetdb/%{name}-%{version}.tar.gz
# Source0-md5:	3fafd56f98a02859b04762ab3d601e37
URL:		-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast database engine

%package devel
Summary:	Header files for MonetDB
Summary(pl):	Pliki nagłówkowe MonetDB
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for MonetDB.

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

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%{_sysconfdir}/MonetDB.conf
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.mil
%attr(755,root,root) %{_libdir}/%{name}/*.so.*
%attr(755,root,root) %{_libdir}/*.so.*
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
%{_includedir}/%{name}
%{_libdir}/%{name}/*.la
%{_libdir}/*.la
%{_libdir}/pkgconfig/MonetDB.pc
%{_datadir}/%{name}/conf
%attr(755,root,root) %{_libdir}/php/*.la
%{_libdir}/autogen/*.py
