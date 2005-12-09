#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
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
%{_libdir}/%{name}/tests
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
/usr/lib/perl5/vendor_perl/5.8.0/i686-pld-linux-thread-multi/DBD/monetdb.pm
/usr/lib/perl5/vendor_perl/5.8.0/i686-pld-linux-thread-multi/DBD/monetdb/GetInfo.pm
/usr/lib/perl5/vendor_perl/5.8.0/i686-pld-linux-thread-multi/DBD/monetdb/TypeInfo.pm
/usr/lib/perl5/vendor_perl/5.8.0/i686-pld-linux-thread-multi/MapiLib.la
/usr/lib/perl5/vendor_perl/5.8.0/i686-pld-linux-thread-multi/MapiLib.pm
/usr/lib/perl5/vendor_perl/5.8.0/i686-pld-linux-thread-multi/MapiLib.so.0.0.0   /usr/lib/php/monetdb.la
/usr/lib/python2.4/site-packages/CMapi.py
/usr/lib/python2.4/site-packages/MapiLib.py
/usr/lib/python2.4/site-packages/_MapiLib.la
/usr/lib/python2.4/site-packages/_MapiLib.so.0.0.0
