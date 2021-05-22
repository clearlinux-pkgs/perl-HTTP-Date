#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Date
Version  : 6.05
Release  : 39
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Date-6.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Date-6.05.tar.gz
Summary  : 'HTTP::Date - date conversion routines'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-Date-license = %{version}-%{release}
Requires: perl-HTTP-Date-perl = %{version}-%{release}
Requires: perl(Time::Local)
Requires: perl(Time::Zone)
BuildRequires : buildreq-cpan
BuildRequires : perl(Time::Local)
BuildRequires : perl(Time::Zone)

%description
# NAME
HTTP::Date - HTTP::Date - date conversion routines
# VERSION
version 6.05

%package dev
Summary: dev components for the perl-HTTP-Date package.
Group: Development
Provides: perl-HTTP-Date-devel = %{version}-%{release}
Requires: perl-HTTP-Date = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Date package.


%package license
Summary: license components for the perl-HTTP-Date package.
Group: Default

%description license
license components for the perl-HTTP-Date package.


%package perl
Summary: perl components for the perl-HTTP-Date package.
Group: Default
Requires: perl-HTTP-Date = %{version}-%{release}

%description perl
perl components for the perl-HTTP-Date package.


%prep
%setup -q -n HTTP-Date-6.05
cd %{_builddir}/HTTP-Date-6.05

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-Date
cp %{_builddir}/HTTP-Date-6.05/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTTP-Date/330396915e37b0e350d3729eaae62cd3a37aea22
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Date.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-Date/330396915e37b0e350d3729eaae62cd3a37aea22

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Date.pm
