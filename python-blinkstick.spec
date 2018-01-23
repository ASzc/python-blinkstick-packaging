%global srcname blinkstick
%global sum Python package to control BlinkStick USB devices
%global upstreamname blinkstick-python
%global commitid a9227d01a9771c0e7aee811a15b824a357f6f09c

Name:           python-%{srcname}
Version:        1.1.8
Release:        1%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://github.com/arvydas/%{upstreamname}
Source0:        https://github.com/arvydas/%{upstreamname}/archive/%{commitid}.zip

BuildArch:      noarch
BuildRequires:  python2-devel python3-devel

%description
BlinkStick Python interface to control devices connected to the computer.

What is BlinkStick? It's a smart USB LED pixel. More info about it here:

http://www.blinkstick.com


%package -n python2-%{srcname}
Summary:        %{sum}
Requires:       pyusb
Requires:       python-%{srcname}-udev
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
BlinkStick Python interface to control devices connected to the computer.

What is BlinkStick? It's a smart USB LED pixel. More info about it here:

http://www.blinkstick.com


%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       python3-pyusb
Requires:       python-%{srcname}-udev
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
BlinkStick Python interface to control devices connected to the computer.

What is BlinkStick? It's a smart USB LED pixel. More info about it here:

http://www.blinkstick.com


%package -n python-%{srcname}-udev
Summary:        udev rule to allow non-root access to BlinkStick USB devices

%description -n python-%{srcname}-udev
udev rule to allow non-root access to BlinkStick USB devices


%prep
%autosetup -n %{upstreamname}-%{commitid}

%build
%py2_build
%py3_build

mkdir -p %{_sysconfdir}/udev/rules.d/
echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="20a0", ATTR{idProduct}=="41e5", MODE:="0666"' > %{_sysconfdir}/udev/rules.d/85-blinkstick.rules

%install
%py2_install
mv %{buildroot}/%{_bindir}/blinkstick %{buildroot}/%{_bindir}/blinkstick-%{python2_version}
ln -s %{_bindir}/blinkstick-%{python2_version} %{buildroot}/%{_bindir}/blinkstick-2
%py3_install
mv %{buildroot}/%{_bindir}/blinkstick %{buildroot}/%{_bindir}/blinkstick-%{python3_version}
ln -s %{_bindir}/blinkstick-%{python3_version} %{buildroot}/%{_bindir}/blinkstick-3
ln -s %{_bindir}/blinkstick %{buildroot}/%{_bindir}/blinkstick-3

%files -n python2-%{srcname}
%license LICENSE.txt
%doc README.rst
%{_bindir}/blinkstick-2
%{_bindir}/blinkstick-%{python2_version}
%{python2_sitelib}/*

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{_bindir}/blinkstick
%{_bindir}/blinkstick-3
%{_bindir}/blinkstick-%{python3_version}
%{python3_sitelib}/*

%files -n python-%{srcname}-udev
%{_sysconfdir}/udev/rules.d/85-blinkstick.rules

%changelog
* Tue Jan 23 2018 Alex Szczuczko <aszczucz@redhat.com> - 1.1.8-1
- Initial package
