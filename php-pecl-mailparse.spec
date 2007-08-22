%global php_extdir  %(php-config --extension-dir 2>/dev/null || echo "failed")

Summary: PHP PECL package for parsing and working with email messages
Name: php-pecl-mailparse
Version: 2.1.1
Release: 8
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/mailparse
Source0: http://pecl.php.net/get/mailparse-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php-mbstring
Requires: php(zend-abi) = %{php_zend_api}
Requires: php(api) = %{php_core_api}
Provides: php-pecl(mailparse) = %{version}-%{release}
BuildRequires: php, php-devel
# Required by phpize
BuildRequires: autoconf, automake, libtool

%description
Mailparse is an extension for parsing and working with email messages.
It can deal with rfc822 and rfc2045 (MIME) compliant messages.


%prep
# We need to create our working directory since the package*.xml files from
# the sources extract straight to it
%setup -q -c
# Move back all other sources to the top level working directory
%{__mv} mailparse-%{version}/* .


%build
phpize
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/z-mailparse.ini << 'EOF'
; Enable mailparse extension module
extension = mailparse.so

; Set the default charset
;mailparse.def_charset = us-ascii
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README try.php
# We prefix the config file with "z-" so that it loads after mbstring.ini
%config(noreplace) %{_sysconfdir}/php.d/z-mailparse.ini
%{php_extdir}/mailparse.so


%changelog
* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 2.1.1-8
- Rebuild for new BuildID feature.

* Mon Aug  6 2007 Matthias Saou <http://freshrpms.net/> 2.1.1-7
- Update License field.
- Remove dist tag, since the package will seldom change.

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 2.1.1-6
- Fix package requirements by adding build-time zend-abi version.
- Clean up spec to conform to current PHP packaging rules.
- No longer bundle part of mbstring (mbfl), at last! (makes spec F7+ specific)

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 2.1.1-5
- FC6 rebuild.
- Add php-api requirement and php-pecl(mailparse) provides.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 2.1.1-4
- Add missing php-mbstring requirement (#197410).

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 2.1.1-3
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 2.1.1-2
- Rebuild for new gcc/glibc and FC5's PHP 5.1.

* Wed Jul 20 2005 Matthias Saou <http://freshrpms.net/> 2.1.1-1
- Update to 2.1.1.
- Update mbfl tarball to 4.4.0 PHP sources.
- Rename .ini file to "z-<name>" to have it load after mbstring.so.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Feb 16 2005 Matthias Saou <http://freshrpms.net/> 2.1-1
- Update to 2.1.

* Thu Jan 13 2005 Matthias Saou <http://freshrpms.net/> 2.0b-5
- Bump release.

* Tue Jul 27 2004 Matthias Saou <http://freshrpms.net/> 2.0b-4
- Update included mbfl source to 4.3.8 as the current 4.3.4 doesn't work
  anymore.

* Fri May 21 2004 Matthias Saou <http://freshrpms.net/> 2.0b-3
- Rebuild for Fedora Core 2.
- No need for a strict dependency on this package, it works fine with
  php 4.3.6 when compiled against 4.3.4.

* Fri May  7 2004 Matthias Saou <http://freshrpms.net/> 2.0b-2
- Added php.d entry to auto-load the module with recent php packages.
- Added more macros to the spec file.

* Mon Apr 26 2004 Matthias Saou <http://freshrpms.net/> 2.0b-1
- Initial RPM release.
- Included part of php-4.3.4's mbfl includes, ugly.

