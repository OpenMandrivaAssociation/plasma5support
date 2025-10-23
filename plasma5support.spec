%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname Plasma5Support
%define devname %mklibname Plasma5Support -d
#define git 20240222
%define gitbranch Plasma/6.1
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: plasma5support
Version: 6.5.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/plasma5support/-/archive/%{gitbranch}/plasma5support-%{gitbranchd}.tar.bz2#/plasma5support-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{version}/plasma5support-%{version}.tar.xz
%endif
Summary: Migration aids for KF5 -> KF6 migration
URL: https://invent.kde.org/plasma/plasma5support
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6UnitConversion)
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(KSysGuard)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xkbcommon)
Requires: %{libname} = %{EVRD}
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed 2025-05-02 after 6.0
%rename kf6-plasma5support

%description
Migration aids for KF5 -> KF6 migration

%package -n %{libname}
Summary: Migration aids for KF5 -> KF6 migration
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Migration aids for KF5 -> KF6 migration

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Migration aids for KF5 -> KF6 migration

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/plasma5support.*
%{_datadir}/plasma5support
%dir %{_datadir}/plasma/weather_legacy
%{_datadir}/plasma/weather_legacy/noaa_station_list.xml

%files -n %{devname}
%{_includedir}/Plasma5Support
%{_includedir}/plasma5support
%{_includedir}/plasma/geolocation
%{_libdir}/cmake/Plasma5Support
%{_qtdir}/doc/Plasma5Support.*
%{_libdir}/libweather_ion.so

%files -n %{libname}
%{_libdir}/libPlasma5Support.so*
%{_libdir}/libplasma-geolocation-interface.so*
%{_libdir}/libweather_ion.so.*
%{_qtdir}/qml/org/kde/plasma/plasma5support
%{_qtdir}/plugins/plasma5support
