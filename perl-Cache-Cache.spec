#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Cache
%define		pnam	Cache
Summary:	Cache::Cache - a generic interface for creating persistent data stores
Summary(pl):	Cache::Cache - ogólny interfejs do trwa³ego przechowywania danych
Name:		perl-Cache-Cache
Version:	1.02
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9dfff47f2317a59a15546a972b2a67ba
URL:		http://perl-cache.sourceforge.net/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Digest-SHA1 >= 2.01
BuildRequires:	perl-Error >= 0.15
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl-IPC-ShareLite >= 0.08
BuildRequires:	perl-Storable >= 1.014
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
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
%{__perl} -MExtUtils::MakeMaker -wle 'WriteMakefile(NAME=>"Cache::Cache")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING CREDITS DISCLAIMER README STYLE
%{perl_vendorlib}/Cache/*.pm
%{_mandir}/man3/*
