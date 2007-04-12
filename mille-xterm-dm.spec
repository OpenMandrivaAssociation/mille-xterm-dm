Summary:	Mille-xterm display manager 
Name:		mille-xterm-dm
Version:	1.0
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
URL:		http://www.revolutionlinux.com/mille-xterm
Source0:	%{name}-%{version}.tar.bz2
Requires:	python >= 2.4
Requires:	python-gnome
Requires:	pygtk2.0-libglade
Requires:	openssh-clients
Requires:	xorg-x11-server
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


