Summary:	Mille-xterm display manager 
Name:		mille-xterm-dm
Version:	1.0
Release:	%mkrel 6
License:	GPL
Group:		System/Servers
URL:		http://www.revolutionlinux.com/mille-xterm
Source0:	%{name}-%{version}.tar.bz2
Requires:	python >= 2.4
Requires:	python-gnome
Requires:	pygtk2.0-libglade
Requires:	openssh-clients
Requires:	x11-server-xorg
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The mille-xterm display manager is the login interface on terminal. It runs on
the terminal and encrypts the X11 trafix through SSH. 

It is based on LDM, the LTSP Display Manager.  

%prep

%setup -q

%build
#nothing to do

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/screen.d
install -d %{buildroot}%{_sbindir} 
install -d %{buildroot}%{_prefix}/lib/ltsp/greeters
install -d %{buildroot}%{_datadir}/ldm
 
install -m0755 src/ldm %{buildroot}%{_sbindir}
install -m0755 src/ldm-askpass %{buildroot}%{_prefix}/lib/ltsp
install -m0755 src/greeters/* %{buildroot}%{_prefix}/lib/ltsp/greeters/
install -m0755 src/screen.d/ldm %{buildroot}%{_sysconfdir}/screen.d/ldm
cp -r src/themes %{buildroot}%{_datadir}/ldm/

%post
update-alternatives --install %{_datadir}/ldm/themes/default ldm-theme %{_datadir}/ldm/themes/Mille-xterm 35
update-alternatives --install %{_datadir}/ldm/themes/default ldm-theme %{_datadir}/ldm/themes/Ubuntu 40
update-alternatives --install %{_datadir}/ldm/themes/default ldm-theme %{_datadir}/ldm/themes/Edubuntu 45

%preun
update-alternatives --remove ldm-theme %{_datadir}/ldm/themes/Mille-xterm
update-alternatives --remove ldm-theme %{_datadir}/ldm/themes/Ubuntu
update-alternatives --remove ldm-theme %{_datadir}/ldm/themes/Edubuntu

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc copyright 
%{_sysconfdir}/screen.d/ldm
%{_sbindir}/ldm
%dir %{_prefix}/lib/ltsp
%{_prefix}/lib/ltsp/*
%dir %{_datadir}/ldm
%{_datadir}/ldm/*




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2011.0
+ Revision: 620331
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2010.0
+ Revision: 439807
- rebuild

* Tue Feb 10 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.0-4mdv2009.1
+ Revision: 339217
- Do not depend on old xorg-x11-server package. Use x11-server-xorg instead.

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 252452
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0-1mdv2008.1
+ Revision: 136579
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Feb 08 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2007.0
+ Revision: 117774
- Import mille-xterm-dm

* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdk
- initial Mandriva package (mille-xterm import)

