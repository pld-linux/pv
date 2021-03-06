#
# Conditional build:
%bcond_without	tests		# build without tests

Summary:	Pipe Viewer - tool for monitoring the progress of data through a pipeline
Summary(pl.UTF-8):	Pipe Viewer - monitorowanie przepływu danych przez potok
Name:		pv
Version:	1.6.6
Release:	1
License:	Artistic v2.0
Group:		Applications
Source0:	http://www.ivarch.com/programs/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	ff3564fddcc2b9bd4a9c1d143aba4b4c
URL:		http://www.ivarch.com/programs/pv.shtml
BuildRequires:	gettext-tools
# the unit tests call usleep(1)
BuildRequires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pipe Viewer is a terminal-based tool for monitoring the progress of
data through a pipeline. It can be inserted into any normal pipeline
between two processes to give a visual indication of how quickly data
is passing through, how long it has taken, how near to completion it
is, and an estimate of how long it will be until completion.

%description -l pl.UTF-8
Pipe Viewer jest tekstowym narzędziem do monitorowania przepływu
danych przez potok. Może być wstawiony w dowolny potok pomiędzy dwa
procesy w celu wizualizacji prędkości z jaką dane przepływają pomiędzy
nimi, ile czasu im to zajmuje, ile jeszcze zostało do ukończenia i ile
mniej więcej czasu to będzie trwało.

%prep
%setup -q

%build
%configure
%{__make}
%{?with_test:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README doc/NEWS doc/TODO
%attr(755,root,root) %{_bindir}/pv
%{_mandir}/man1/pv.1*
