# $Id: php-pecl-mailparse.spec,v 1.1 2004/11/09 02:49:07 cvsextras Exp $

%define php_extdir %(php-config --extension-dir)

Summary: RECL package for parsing and working with email messages
Name: php-pecl-mailparse
Version: 2.0b
Release: 2.1.fc1.fr
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/mailparse
Source0: http://pecl.php.net/get/mailparse-%{version}.tgz
Source1: mbfl-4.3.4.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php
BuildRequires: php, php-devel
# Required by phpize
BuildRequires: autoconf, automake, libtool, gcc-c++

%description
Mailparse is an extension for parsing and working with email messages.
It can deal with rfc822 and rfc2045 (MIME) compliant messages.


%prep 
%setup -a 1 -n mailparse-%{version}


%build
%{__mkdir_p} ext/mbstring/libmbfl/
%{__mv} mbfl-* ext/mbstring/libmbfl/mbfl
phpize
%configure
%{__make}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/mailparse.ini << 'EOF'
; Enable mailparse extension module
extension=mailparse.so
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc README try.php
%config(noreplace) %{_sysconfdir}/php.d/mailparse.ini
%{php_extdir}/mailparse.so


%changelog
* Fri May  7 2004 Matthias Saou <http://freshrpms.net/> 2.0b-2
- Added php.d entry to auto-load the module with recent php packages.
- Added more macros to the spec file.

* Mon Apr 26 2004 Matthias Saou <http://freshrpms.net/> 2.0b-1
- Initial RPM release.
- Included part of php-4.3.4's mbfl includes, ugly.
