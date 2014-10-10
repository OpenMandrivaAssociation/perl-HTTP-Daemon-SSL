%define upstream_name	 HTTP-Daemon-SSL
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A simple http server class with SSL support
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz
# default port could be in use by the sieve daemon (2000), so
# let's change it to something hopefully free so that make test
# works
Patch0:		HTTP-Daemon-SSL-1.01-sslport.patch

BuildRequires:	perl-devel
BuildRequires:	perl(HTTP::Daemon)
BuildRequires:	perl(IO::Socket::SSL)
BuildRequires:	perl-libwww-perl
BuildArch:	noarch

%description
HTTP::Daemon::SSL is a descendant of HTTP::Daemon that uses SSL
sockets (via IO::Socket::SSL) instead of cleartext sockets. It
also handles SSL-specific problems, such as dealing with HTTP
clients that attempt to connect to it without using SSL.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc certs Changes BUGS README
%{perl_vendorlib}/HTTP
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 403267
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.04-3mdv2009.0
+ Revision: 257248
- rebuild

* Wed Feb 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2008.1
+ Revision: 166953
- new version
  re-enable tests

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.02-2mdv2008.1
+ Revision: 122706
- kill re-definition of %%buildroot on Pixel's request


* Fri Nov 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-2mdv2007.0
+ Revision: 86969
- rebuild
- Import perl-HTTP-Daemon-SSL

* Fri Sep 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdk
- new version (TODO: fix tests)
- fix sources url for rpmbuildupdate
- fix directory ownership
- better summary

* Fri Jul 15 2005 Andreas Hasenack <andreas@mandriva.com> 1.01-2mdk
- made make test work, thanks rgs

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.01-1mdk
- initial Mandriva package

