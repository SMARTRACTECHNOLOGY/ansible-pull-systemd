%{?systemd_requires}
Name:           ansible-pull-systemd
Version:        1.0.2
Release:        1
Summary:        Unit file for starting ansible on first boot.

Group:          System Environment/Base
License:        MIT
Vendor:         SMARTRAC Technology Fletcher, Inc.

Requires:       ansible

BuildRequires:  systemd

URL:            https://github.com/smartractechnology
Source0:        %{name}.service
Source10:       %{name}
Source20:       %{name}.conf
BuildArch:      noarch

%description
Unit file for starting ansible pull on first boot, then disabling itself (optionally)

%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_sysconfdir}

install -p -m 644 %{SOURCE0} %{buildroot}/%{_unitdir}
install -p -m 644 %{SOURCE10} %{buildroot}/%{_sbindir}
install -p -m 644 %{SOURCE20} %{buildroot}/%{_sysconfdir}

%files
%config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0644, root, root) %{_unitdir}/%{name}.service
%attr(0754, root, root) %{_sbindir}/%{name}

%pre

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%changelog
* Thu Jun 1 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 1.0.2-1
- Resolve dumb error with not making parent directory.

* Thu Jun 1 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 1.0.1-1
- Change the directory due to issues with purge in ansible-pull.

* Wed May 31 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 1-1
- Initial RPM release
