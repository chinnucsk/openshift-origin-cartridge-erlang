%global cartridgedir %{_libexecdir}/openshift/cartridges/erlang

Summary:    ERLANG cartridge
Name:       openshift-origin-cartridge-erlang
Version:    0.8.0
Release:    1%{?dist}
Group:      Development/Languages
License:    ASL 2.0
URL:        https://www.openshift.com
Source0:    http://lsm5.fedorapeople.org/%{name}/%{name}-%{version}.tar.gz
Requires:   rubygem(openshift-origin-node)
Requires:   openshift-origin-node-util

Obsoletes:  openshift-origin-cartridge-erlang-0.1

BuildArch:  noarch

%description
ERLANG cartridge for openshift. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Thu Aug 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.1-1
- Initial package
