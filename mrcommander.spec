%define 	sub_ver preview6

Summary:	Clone of Total Commander for Linux
Summary(pl):	Klon Total Commandera dla Linuksa
Name:		mrcommander
Version:	0.1a
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/mrcommander/%{name}-%{version}-%{sub_ver}.tar.gz
# Source0-md5:	9c335de683dc9b9dda96011a75ae7e09
URL:		http://mrcommander.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mrcommander is a clone of Total Commander used to manage files under
Linux.

%description -l pl
mrcommander jest klonem Total Commandera u�ywanym do zarz�dzania
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