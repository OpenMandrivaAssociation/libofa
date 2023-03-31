%define major	0
%define libname	%mklibname ofa %{major}
%define devname	%mklibname ofa -d

Summary:	Open Fingerprint Architecture library
Name:		libofa
Version:	0.9.3
Release:	31
License:	GPLv2
Group:		System/Libraries
Url:		http://code.google.com/p/musicip-libofa/
Source0:	http://musicip-libofa.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		libofa-build-fix.patch
Patch1:		libofa-gcc43.diff
Patch2:		libofa-0.9.3-pkgconfig-drop-expat.patch
Patch3:		libofa-0.9.3-curl.patch
Patch4:		libofa-0.9.3-fedora-gcc47.patch
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(libcurl)

%description
Currently, MusicDNS and the Open Fingerprint Architecture are being used to:

	* identify duplicate tracks, even when the metadata is different, MusicIP
	  identifies the master recording.
    * fix metadata
	* find out more about tracks by connecting to MusicBrainz- the worlds
	  largest music metabase community

%package -n	%{libname}
Summary:        Open Fingerprint Architecture library
Group:          System/Libraries
Provides:	%{name} = %{EVRD}

%description -n	%{libname}
Currently, MusicDNS and the Open Fingerprint Architecture are being used to:

	* identify duplicate tracks, even when the metadata is different, MusicIP
	  identifies the master recording.
    * fix metadata
	* find out more about tracks by connecting to MusicBrainz- the worlds
	  largest music metabase community

%package -n	%{devname}
Summary:	Files needed for developing applications which use litunepimp
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
The %{name}-devel package includes the header files and .so libraries
necessary for developing libofa enabled tagging applications.

%prep
%setup -q
%autopatch -p1
mv configure.in configure.ac

%build
%configure --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libofa.so.%{major}*

%files -n %{devname}
%doc AUTHORS README COPYING
%{_includedir}/*
%{_libdir}/pkgconfig/libofa.pc
%{_libdir}/*.so

