%define major 0
%define libname %mklibname ofa %{major}
%define develname %mklibname ofa -d
%define staticdevelname %mklibname ofa -d -s

Summary:	Open Fingerprint Architecture library
Name:		libofa
Version:	0.9.3
Release:	%mkrel 10
License:	GPL
Group:		System/Libraries
URL:		http://code.google.com/p/musicip-libofa/
Source0:	http://musicip-libofa.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		libofa-build-fix.patch
Patch1:		libofa-gcc43.diff
BuildRequires:	fftw3-devel
BuildRequires:	libcurl-devel
BuildRequires:	libexpat-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
Currently, MusicDNS and the Open Fingerprint Architecture are being used to:

	* identify duplicate tracks, even when the metadata is different, MusicIP
	  identifies the master recording.
    * fix metadata
	* find out more about tracks by connecting to MusicBrainz- the worlds
	  largest music metabase community

%package -n	%{develname}
Summary:	Files needed for developing applications which use litunepimp
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%mklibname ofa 0 -d

%description -n	%{develname}
The %{name}-devel package includes the header files and .so libraries
necessary for developing libofa enabled tagging applications.

If you are going to develop libofa enabled tagging 
applications you should install %{name}-devel. You'll also need 
to have the %{name} package installed.

%package -n	%{staticdevelname}
Summary:        Static libraries for libtunepimp
Group:          Development/C
Provides:       %{name}-static-devel = %{version}-%{release}
Requires:       %{develname} = %{version}-%{release}
Obsoletes:	%mklibname ofa 0 -d -s

%description -n	%{staticdevelname}
The %{name}-devel package includes the static libraries
necessary for developing libofa enabled tagging
applications using the %{name} library.

If you are going to develop libofa enabled tagging applications,
you should install %{name}-devel.  You'll also need to have the %{name}
package installed.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -p /sbin/ldconfig -n %{libname}
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig -n %{libname}
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS README COPYING
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/libofa.pc
%{_libdir}/*.so
%{_libdir}/*.la

%files -n %{staticdevelname}
%defattr(-,root,root)
%{_libdir}/*.a
