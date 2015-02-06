#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Date
Version  : 6.02
Release  : 8
URL      : http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/HTTP-Date-6.02.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/HTTP-Date-6.02.tar.gz
Summary  : date conversion routines
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-HTTP-Date-doc

%description
NAME
HTTP::Date - date conversion routines
SYNOPSIS
use HTTP::Date;
$string = time2str($time);    # Format as GMT ASCII time
$time = str2time($string);    # convert ASCII date to machine time

%package doc
Summary: doc components for the perl-HTTP-Date package.
Group: Documentation

%description doc
doc components for the perl-HTTP-Date package.


%prep
%setup -q -n HTTP-Date-6.02

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/HTTP/Date.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
