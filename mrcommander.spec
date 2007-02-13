%define 	sub_ver preview6

Summary:	Clone of Total Commander for Linux
Summary(pl.UTF-8):	Klon Total Commandera dla Linuksa
Name:		mrcommander
Version:	0.1a
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/mrcommander/%{name}-%{version}-%{sub_ver}.tar.gz
# Source0-md5:	9c335de683dc9b9dda96011a75ae7e09
URL:		http://sourceforge.net/projects/mrcommander/
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mrcommander is a clone of Total Commander used to manage files under
Linux.

%description -l pl.UTF-8
mrcommander jest klonem Total Commandera używanym do zarządzania
plikami pod Linuksem.

%prep
%setup -q -n %{name}-%{version}-%{sub_ver}

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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
