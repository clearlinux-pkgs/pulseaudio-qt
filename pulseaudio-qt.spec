#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v24
# autospec commit: a88ffdc
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : pulseaudio-qt
Version  : 1.7.0
Release  : 4
URL      : https://download.kde.org/stable/pulseaudio-qt/pulseaudio-qt-1.7.0.tar.xz
Source0  : https://download.kde.org/stable/pulseaudio-qt/pulseaudio-qt-1.7.0.tar.xz
Source1  : https://download.kde.org/stable/pulseaudio-qt/pulseaudio-qt-1.7.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.1 LGPL-3.0
Requires: pulseaudio-qt-lib = %{version}-%{release}
Requires: pulseaudio-qt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : pkg-config
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KF5 PulseAudio Qt Bindings - libpulse bindings for Qt
pulseaudio-qt is a Qt-style wrapper for [libpulse](https://freedesktop.org/software/pulseaudio/doxygen/).

%package dev
Summary: dev components for the pulseaudio-qt package.
Group: Development
Requires: pulseaudio-qt-lib = %{version}-%{release}
Provides: pulseaudio-qt-devel = %{version}-%{release}
Requires: pulseaudio-qt = %{version}-%{release}

%description dev
dev components for the pulseaudio-qt package.


%package lib
Summary: lib components for the pulseaudio-qt package.
Group: Libraries
Requires: pulseaudio-qt-license = %{version}-%{release}

%description lib
lib components for the pulseaudio-qt package.


%package license
Summary: license components for the pulseaudio-qt package.
Group: Default

%description license
license components for the pulseaudio-qt package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n pulseaudio-qt-1.7.0
cd %{_builddir}/pulseaudio-qt-1.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744398562
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6 \
-DBUILD_TESTING=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1744398562
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pulseaudio-qt
cp %{_builddir}/pulseaudio-qt-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/pulseaudio-qt/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/pulseaudio-qt-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/pulseaudio-qt/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/pulseaudio-qt-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/pulseaudio-qt/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/pulseaudio-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/pulseaudio-qt/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/pulseaudio-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/pulseaudio-qt/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/Card
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/CardPort
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/Client
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/Context
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/Device
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/IndexedPulseObject
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/Models
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/Module
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/Port
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/Profile
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/PulseObject
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/Server
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/Sink
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/SinkInput
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/Source
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/SourceOutput
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/Stream
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/StreamRestore
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/VolumeObject
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/card.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/cardport.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/client.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/context.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/device.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/indexedpulseobject.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/models.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/module.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/port.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/profile.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/pulseaudioqt_export.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/pulseobject.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/server.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/sink.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/sinkinput.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/source.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/sourceoutput.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/stream.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/streamrestore.h
/usr/include/KF6/KF6PulseAudioQt/PulseAudioQt/volumeobject.h
/usr/include/KF6/pulseaudioqt_version.h
/usr/lib64/cmake/KF6PulseAudioQt/KF6PulseAudioQtConfig.cmake
/usr/lib64/cmake/KF6PulseAudioQt/KF6PulseAudioQtConfigVersion.cmake
/usr/lib64/cmake/KF6PulseAudioQt/KF6PulseAudioQtTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6PulseAudioQt/KF6PulseAudioQtTargets.cmake
/usr/lib64/libKF6PulseAudioQt.so
/usr/lib64/pkgconfig/KF6PulseAudioQt.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF6PulseAudioQt.so.1.7.0
/usr/lib64/libKF6PulseAudioQt.so.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pulseaudio-qt/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/pulseaudio-qt/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/pulseaudio-qt/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/pulseaudio-qt/e458941548e0864907e654fa2e192844ae90fc32
