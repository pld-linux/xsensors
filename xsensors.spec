Summary:	Display all related information from motherboard sme}ensors
Summary(pl.UTF-8):	Program wyświetlający informacje z czujników płyty głównej
Name:		xsensors
Version:	0.70
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.linuxhardware.org/xsensors/%{name}-%{version}.tar.gz
# Source0-md5:	4f8fb83cfd03c0cc34967a73c6021531
Source1:	%{name}.desktop
URL:		http://www.linuxhardware.org/
Patch0:		%{name}-cleanup-allocs.patch
Patch1:		%{name}-remove-unused-variables.patch
Patch2:		%{name}-replace-deprecated-gtk.patch
Patch3:		%{name}-select-chip.patch
Patch4:		%{name}-support-multiple-chips-on-cmd.patch
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

%description -l pl.UTF-8
Jest to program napisany przy użyciu GTK+2 służący do wyświetlania
informacji z czujników płyty głównej.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

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

install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/xsensors
%dir %{_pixmapsdir}/xsensors
%{_pixmapsdir}/xsensors/default.xpm
%{_desktopdir}/xsensors.desktop
