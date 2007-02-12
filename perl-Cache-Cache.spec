#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Cache
%define		pnam	Cache
Summary:	Cache::Cache - a generic interface for creating persistent data stores
Summary(pl.UTF-8):   Cache::Cache - ogólny interfejs do trwałego przechowywania danych
Name:		perl-Cache-Cache
Version:	1.05
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	09e4d37979c8f8ce2518e1d1ccd10d99
URL:		http://perl-cache.sourceforge.net/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Digest-SHA1 >= 2.01
BuildRequires:	perl-Error >= 0.15
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl-IPC-ShareLite >= 0.08
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

%description -l pl.UTF-8
Moduły Cache mają na celu pomóc programiście w utrzymywaniu danych
przez określony czas. Te moduły są przeważnie używane w aplikacjach
WWW do zapisywania danych lokalnie w celu uniknięcia powtarzających
się i niepotrzebnych odwołań do zewnętrznych maszyn lub baz danych.
Cache::Cache bywa używany ze względu na swój prosty interfejs do
dzielenia danych pomiędzy uruchomieniami aplikacji lub wywołaniami
skryptu CGI, albo po prostu jako łatwa w użyciu abstrakcja systemu
plików lub pamięci dzielonej.

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
