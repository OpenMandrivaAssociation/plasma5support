%define libname %mklibname KF6Plasma5Support
%define devname %mklibname KF6Plasma5Support -d
%define git 20230918

Name: kf6-plasma5support
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/plasma/plasma5support/-/archive/master/plasma5support-master.tar.bz2#/plasma5support-%{git}.tar.bz2
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
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
Requires: %{libname} = %{EVRD}

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

%prep
%autosetup -p1 -n plasma5support-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/plasma5support.*
%{_datadir}/plasma5support

%files -n %{devname}
%{_includedir}/KF6/*
%{_libdir}/cmake/KF6Plasma5Support
%{_qtdir}/doc/KF6Plasma5Support.*

%files -n %{libname}
%{_libdir}/libKF6Plasma5Support.so*
%{_qtdir}/qml/org/kde/plasma/plasma5support
