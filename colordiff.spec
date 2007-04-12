%define name	colordiff
%define version	1.0.6

Summary:	Wrapper for diff that produces output with syntax highlighting
Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
License:	GPL
Url:		http://colordiff.sourceforge.net/
Source0:	http://download.sourceforge.net/sourceforge/colordiff/%{name}-%{version}.tar.bz2  
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc BUGS CHANGES colordiffrc-lightbg COPYING INSTALL README TODO
%{_bindir}/cdiff
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/colordiffrc
%{_mandir}/man1/colordiff*


