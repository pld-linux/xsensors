Summary:	Display all related information from motherboard sensors
Summary(pl):	Program wy¶wietlaj±cy informacje z czujników p³yty g³ównej
Name:		xsensors
Version:	0.50
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.linuxhardware.org/xsensors/%{name}-%{version}.tar.gz
# Source0-md5:	3c80057bf8cc2d2f9803a496e7bc6e78
URL:		http://www.linuxhardware.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libtool
BuildRequires:	lm_sensors-devel >= 2.9.1
BuildRequires:	pkgconfig
Requires:	lm_sensors >= 2.9.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xsensors is a GTK+2 program designed to display all the related
information from motherboard sensors.

%description -l pl
Jest to program napisany przy u¿yciu GTK+2 s³u¿±cy do wy¶wietlania
informacji z czujników p³yty g³ównej.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/xsensors
%dir %{_pixmapsdir}/xsensors
%{_pixmapsdir}/xsensors/*.xpm
