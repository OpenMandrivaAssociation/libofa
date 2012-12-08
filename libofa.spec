%define major 0
%define libname %mklibname ofa %{major}
%define develname %mklibname ofa -d

Summary:	Open Fingerprint Architecture library
Name:		libofa
Version:	0.9.3
Release:	16
License:	GPLv2
Group:		System/Libraries
URL:		http://code.google.com/p/musicip-libofa/
Source0:	http://musicip-libofa.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		libofa-build-fix.patch
Patch1:		libofa-gcc43.diff
Patch2:		libofa-0.9.3-pkgconfig-drop-expat.patch
Patch3:		libofa-0.9.3-curl.patch
Patch4:		libofa-0.9.3-fedora-gcc47.patch
BuildRequires:	fftw3-devel
BuildRequires:	libcurl-devel
BuildRequires:	libexpat-devel

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

%package -n	%{develname}
Summary:	Files needed for developing applications which use litunepimp
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{version}
Obsoletes:	%mklibname ofa 0 -d

%description -n	%{develname}
The %{name}-devel package includes the header files and .so libraries
necessary for developing libofa enabled tagging applications.

If you are going to develop libofa enabled tagging
applications you should install %{name}-devel. You'll also need
to have the %{name} package installed.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1


%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS README COPYING
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/pkgconfig/libofa.pc
%{_libdir}/*.so


%changelog
* Wed Mar 21 2012 Andrew Lukoshko <andrew.lukoshko@rosalab.ru> 0.9.3-15mdv2011.0
- fixed build with recent curl versions

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-14mdv2011.0
+ Revision: 661508
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-13mdv2011.0
+ Revision: 602587
- rebuild

* Mon Feb 08 2010 Funda Wang <fwang@mandriva.org> 0.9.3-12mdv2010.1
+ Revision: 502215
- apply fedora patch instead

* Mon Feb 08 2010 Funda Wang <fwang@mandriva.org> 0.9.3-11mdv2010.1
+ Revision: 502088
- expat is not need for libofa

* Sun Jan 17 2010 Funda Wang <fwang@mandriva.org> 0.9.3-10mdv2010.1
+ Revision: 492817
- rebuild
- rediff patch

* Wed Aug 12 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.3-9mdv2010.0
+ Revision: 415583
- fix compilation with gcc 4.4

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-8mdv2009.0
+ Revision: 229894
- added a gcc43 patch
- new url

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-6mdv2008.1
+ Revision: 178983
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Jul 21 2007 Funda Wang <fwang@mandriva.org> 0.9.3-4mdv2008.0
+ Revision: 54121
- fix static devel package requires

* Sat Jul 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.3-3mdv2008.0
+ Revision: 52068
- new devel library policy
- spec file clean
- Import libofa



* Mon Jul 31 2006 Helio Castro <helio@mandriva.com> 0.5.0-2mdv2007.0
- Put right requires for fftw3-devel

* Sat Jul 22 2006 Emmanuel Andry <eandry@mandriva.org> 0.5.0-1mdv2007.0
- Initial Mandriva release
