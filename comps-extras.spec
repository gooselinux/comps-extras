Summary: Images for components included in Fedora
Name: comps-extras
Version: 17.8
Release: 1%{?dist}
URL: http://git.fedorahosted.org/git/?p=comps-extras.git;a=summary
Source0: http://fedorahosted.org/releases/c/o/comps-extras/%{name}-%{version}.tar.gz
# while GPL isn't normal for images, it is the case here
# No version specified.
# KDE logo is LGPL
License: GPL+ and LGPL+
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
This package contains images for the components included in Fedora.

%prep
%setup -q

%build
# nothing to do

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc comps.dtd comps-cleanup.xsl
%dir %{_datadir}/pixmaps/comps
%{_datadir}/pixmaps/comps/*

%changelog
* Thu Aug 12 2010 Bill Nottingham <notting@redhat.com> - 17.8-1
- further RHEL 6 updates (#623739)

* Thu Jun 17 2010 Bill Nottingham <notting@redhat.com> - 17.7-1
- further RHEL 6 updates (#603163, #605176)

* Thu Mar  4 2010 Bill Nottingham <notting@redhat.com> - 17.6-1
- further RHEL 6 updates (#568348)

* Wed Feb  3 2010 Bill Nottingham <notting@redhat.com> - 17.5-1
- update for RHEL 6
