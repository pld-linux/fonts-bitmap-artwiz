%define		_tarname	artwiz-aleczapka-en
Summary:	Artwiz aleczapka bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe artwiz aleczapka
Name:		fonts-bitmap-artwiz
Version:	1.3
Release:	1
License:	GPL v2
Group:		Fonts
Source0:	http://dl.sourceforge.net/artwizaleczapka/%{_tarname}-%{version}.tar.bz2
# Source0-md5:	6c6c704f2f08f9d6308d366423dfa90e
URL:		http://artwizaleczapka.sourceforge.net/
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_miscfontsdir	%{_fontsdir}/misc

%description
This package contains artwiz aleczapka bitmap fonts (PCF).

%description -l pl.UTF-8
Pakiet ten zawiera bitmapowe (PCF) fonty artwiz aleczapka.

%prep
%setup -q -n %{_tarname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_miscfontsdir}
install *.pcf $RPM_BUILD_ROOT%{_miscfontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%{_miscfontsdir}/*
