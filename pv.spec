Summary:	Pipe Viewer
Summary(pl):	Pipe Viewer - monitorowanie przep�ywu danych przez potok
Name:		pv
Version:	0.4.4
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.ivarch.com/programs/sources/%{name}-%{version}.tar.gz
URL:		http://www.ivarch.com/programs/pv.shtml
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pipe Viewer is a terminal-based tool for monitoring the progress of data
through a pipeline. It can be inserted into any normal pipeline between
two processes to give a visual indication of how quickly data is passing
through, how long it has taken, how near to completion it is, and an
estimate of how long it will be until completion.

%description -l pl
Pipe Viewer jest tekstowym narz�dziem do monitorowania przep�ywu danych
przez potok. Mo�e by� wstawiony w dowolny potok pomi�dzy dwa procesy w celu
wizualizacji pr�dko�ci z jak� dane przep�ywaj� pomi�dzy nimi, ile czasu im
to zajmuje, ile jeszcze zosta�o do uko�czenia i ile mniej wi�cej czasu to
b�dzie trwa�o.

%prep
%setup -q

%build
cd autoconf
%{__autoconf}
cd ..
install autoconf/configure .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_infodir}}

%{__make} install RPM_BUILD_ROOT=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README doc/manual.html doc/NEWS doc/TODO
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*.info*
%{_mandir}/man1/*
