%include	/usr/lib/rpm/macros.perl
%define	pdir	Cache
%define	pnam	Cache
Summary:	Cache::Cache perl extension
Summary(pl):	Rozszerzenie perla: Cache::Cache
Name:		perl-Cache-Cache
Version:	1.01
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-Error
BuildRequires:	perl-modules
BuildRequires:	perl-IPC-ShareLite
BuildRequires:	perl-Storable
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Cache modules are designed to assist a developer in persisting
data for a specified period of time. Often these modules are used
in web applications to store data locally to save repeated and
redundant expensive calls to remote machines or databases. People
have also been known to use Cache::Cache for its straightforward
interface in sharing data between runs of an application or
invocations of a CGI-style script or simply as an easy to use
abstraction of the filesystem or shared memory.

%description -l pl
Modu³y Cache maj± na celu pomóc programi¶cie w utrzymywaniu danych
przez okre¶lony czas. Te modu³y s± przewa¿nie u¿ywane w aplikacjach
WWW do zapisywania danych lokalnie w celu unikniêcia powtarzaj±cych
siê i niepotrzebnych odwo³añ do zewnêtrznych maszyn lub baz danych.
Cache::Cache bywa u¿ywany ze wzglêdu na swój prosty interfejs do
dzielenia danych pomiêdzy uruchomieniami aplikacji lub wywo³aniami
skryptu CGI, albo po prostu jako ³atwa w u¿yciu abstrakcja systemu
plików lub pamiêci dzielonej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES COPYING CREDITS DISCLAIMER README STYLE TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Cache
%{_mandir}/man3/*
