%define upstream_name	 HTTP-Daemon-SSL
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A simple http server class with SSL support
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz
# default port could be in use by the sieve daemon (2000), so
# let's change it to something hopefully free so that make test
# works
Patch0:		HTTP-Daemon-SSL-1.01-sslport.patch

BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-libwww-perl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
HTTP::Daemon::SSL is a descendant of HTTP::Daemon that uses SSL
sockets (via IO::Socket::SSL) instead of cleartext sockets. It
also handles SSL-specific problems, such as dealing with HTTP
clients that attempt to connect to it without using SSL.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1

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
