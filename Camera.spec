Summary:	GNUstep Camera app
Name:		Camera
Version:	0.8
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://download.gna.org/gsimageapps/Camera-0.8.tar.bz2
# Source0-md5:	d1bdcabda19091bc846246cd21f22996
Patch0:		%{name}-processArgs.patch
URL:		http://home.gna.org/gsimageapps/
BuildRequires:	gnustep-base-devel >= 1.13.0
BuildRequires:	gnustep-gui-devel >= 0.11.0
BuildRequires:	libgphoto2-devel
Requires:	gnustep-base >= 1.13.0
Requires:	gnustep-gui >= 0.11.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple tool to download photos from a digital camera (uses libgphoto)

%prep
%setup -q -n Camera
%patch0 -p1

%build
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes

%{__make} install \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/Camera
%dir %{_libdir}/GNUstep/Applications/Camera.app
%attr(755,root,root) %{_libdir}/GNUstep/Applications/Camera.app/Camera
%dir %{_libdir}/GNUstep/Applications/Camera.app/Resources
%{_libdir}/GNUstep/Applications/Camera.app/Resources/*.desktop
%{_libdir}/GNUstep/Applications/Camera.app/Resources/*.png
%{_libdir}/GNUstep/Applications/Camera.app/Resources/*.jpg
%{_libdir}/GNUstep/Applications/Camera.app/Resources/*.gorm
%{_libdir}/GNUstep/Applications/Camera.app/Resources/*.plist
