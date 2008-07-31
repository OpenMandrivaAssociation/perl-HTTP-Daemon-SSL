%define module	HTTP-Daemon-SSL
%define version		1.04
%define release		%mkrel 3

Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
Summary:	A simple http server class with SSL support
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.gz
# default port could be in use by the sieve daemon (2000), so
# let's change it to something hopefully free so that make test
# works
Patch:		HTTP-Daemon-SSL-1.01-sslport.patch
BuildRequires:	perl-devel
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-libwww-perl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
HTTP::Daemon::SSL is a descendant of HTTP::Daemon that uses SSL
sockets (via IO::Socket::SSL) instead of cleartext sockets. It
also handles SSL-specific problems, such as dealing with HTTP
clients that attempt to connect to it without using SSL.

%prep
%setup -q -n %{module}-%{version} 
%patch -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc certs Changes BUGS README
%{perl_vendorlib}/HTTP
%{_mandir}/*/*


