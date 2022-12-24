Summary:	Wrapper for diff that produces output with syntax highlighting
Name:     colordiff
Version:	1.0.21
Release:	1
License:	GPLv2+
Url:		https://www.colordiff.org/
Source0:	https://www.colordiff.org/%{name}-%{version}.tar.gz
Group:		Development/Other
Requires:	diffutils
Requires:	less
Requires:	perl
Requires:	webfetch
BuildArch:	noarch

%description
The Perl script colordiff is a wrapper for diff. It produces the same
output but with syntax highlighting. Color schemes can be customized.

%prep
%setup -q

%build

%install
%{__install} -m 755 -D cdiff.sh %{buildroot}%{_bindir}/cdiff
%{__install} -m 755 -D colordiff.pl %{buildroot}%{_bindir}/colordiff
%{__install} -m 644 -D colordiff.1 %{buildroot}%{_mandir}/man1/colordiff.1
%{__sed} -i -e 's/banner=yes/banner=no/' colordiffrc*
%{__install} -m 644 -D colordiffrc %{buildroot}%{_sysconfdir}/colordiffrc

%files
%doc BUGS CHANGES colordiffrc-lightbg COPYING INSTALL README
%{_bindir}/cdiff
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/colordiffrc
%{_mandir}/man1/colordiff*




%changelog
* Wed Jun 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.10-2mdv2012.0
+ Revision: 805393
- version update 1.0.10

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.9-2mdv2011.0
+ Revision: 617405
- the mass rebuild of 2010.0 packages

* Thu Aug 13 2009 Emmanuel Andry <eandry@mandriva.org> 1.0.9-1mdv2010.0
+ Revision: 416111
- New version 1.0.9

* Wed Feb 18 2009 Jérôme Soyer <saispo@mandriva.org> 1.0.8a-1mdv2009.1
+ Revision: 342395
- New upstream release

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0.7-3mdv2009.0
+ Revision: 243596
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Dec 18 2007 Jérôme Soyer <saispo@mandriva.org> 1.0.7-1mdv2008.1
+ Revision: 132040
- New release

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

