%define real_name	HTTP-Daemon-SSL
%define version		1.02
%define release		%mkrel 2

Name:		perl-%{real_name}
Version:	%{version}
Release:	%{release}
Summary:	A simple http server class with SSL support
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BE/BEHROOZI/%{real_name}-%{version}.tar.bz2
# default port could be in use by the sieve daemon (2000), so
# let's change it to something hopefully free so that make test
# works
Patch:		HTTP-Daemon-SSL-1.01-sslport.patch
BuildRequires:	perl-devel
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-libwww-perl
BuildArch:	noarch

%description
HTTP::Daemon::SSL is a descendant of HTTP::Daemon that uses SSL
sockets (via IO::Socket::SSL) instead of cleartext sockets. It
also handles SSL-specific problems, such as dealing with HTTP
clients that attempt to connect to it without using SSL.

%prep
%setup -q -n %{real_name}-%{version} 
#%patch -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

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


