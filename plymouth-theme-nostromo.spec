Summary:	Plymouth "Nostromo" theme
Name:		plymouth-theme-nostromo
Version:	1.3
Release:	0.1
License:	GPL v3
Group:		Applications
Source0:	https://github.com/brenns10/plymouth-theme-nostromo/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6d6256a6718d5ebaa71db691cc8681f4
URL:		https://github.com/brenns10/plymouth-theme-nostromo
Requires:	plymouth-scripts
Requires:	plymouth-plugin-script
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Plymouth theme based on the boot screen of the computers on
Nostromo, the ship on which Alien takes place.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/nostromo

install *.png nostromo.plymouth nostromo.script \
	$RPM_BUILD_ROOT%{_datadir}/plymouth/themes/nostromo/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{_datadir}/plymouth/themes/nostromo
%{_datadir}/plymouth/themes/nostromo/*.png
%{_datadir}/plymouth/themes/nostromo/nostromo.plymouth
%{_datadir}/plymouth/themes/nostromo/nostromo.script
