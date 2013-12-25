#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	GCrypt
Summary:	Crypt::GCrypt - Perl interface to the GNU Cryptographic library
Name:		perl-Crypt-GCrypt
Version:	1.26
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d23084ed878e5d12d4956c39e6f2b813
URL:		http://search.cpan.org/dist/Crypt-GCrypt/
BuildRequires:	libgcrypt-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::GCrypt provides an object interface to the C libgcrypt library.
It currently supports symmetric encryption/decryption and message
digests, while asymmetric cryptography is being worked on.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%{perl_vendorarch}/Crypt/GCrypt.pm
%{perl_vendorarch}/Crypt/GCrypt
%dir %{perl_vendorarch}/auto/Crypt/GCrypt
%{perl_vendorarch}/auto/Crypt/GCrypt/GCrypt.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/GCrypt/GCrypt.so
%{_mandir}/man3/Crypt::GCrypt*.3*
