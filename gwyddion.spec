%define major 0
%define api 2
%define libname %mklibname %{name} %{api} %{major}
%define libgwyapp %mklibname gwyapp %{api} %{major}
%define libgwydgets %mklibname gwydgets %{api} %{major}
%define libgwydraw %mklibname gwydraw %{api} %{major}
%define libgwymodule %mklibname gwymodule %{api} %{major}
%define libgwyprocess %mklibname gwyprocess %{api} %{major}
%define devname %mklibname %{name} %{api} -d

Summary:	A SPM (scanning probe microscopy) data visualization and analysis tool
Name:		gwyddion
Version:	2.45
Release:	1
License:	GPLv2+
Group:		Sciences/Physics
URL:		http://gwyddion.net/
Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz.sig
#Patch0:	http://gwyddion.net/download/2.45/gwyddion-2.45-gtk-doc-install.patch

BuildRequires:	ruby
BuildRequires:	bzip2-devel
BuildRequires:	cfitsio-devel
BuildRequires:	intltool
BuildRequires:	kdelibs-devel > 4
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkglext-1.0)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	pkgconfig(IlmBase)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libzip)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(minizip)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	python2-numpy #pythonegg(numpy)

BuildRequires:	epydoc
BuildRequires:	gtk-doc
#BuildRequires:	fpc #-base

%description
# adapted from the homepage
Gwyddion is a modular program for SPM (scanning probe microscopy) data
visualization and analysis. Primarily it is intended for analysis of height
fields obtained by scanning probe microscopy techniques (AFM, MFM, STM,
SNOM/NSOM) and it supports many SPM data formats. However, it can also be
used for general height field and image processing, for instance for analysis
of profilometry data.

Gwyddion aims to provide a modular program for 2D data processing and analysis
that can be easily extended by third-party modules and scripts. Moreover, the
status of free software enables to provide the source code to developers and
users, which makes the further program improvement easier.

Its graphical user interface is based on Gtk+.

%files -f %{name}.lang
%doc AUTHORS NEWS README THANKS
%{_bindir}/%{name}
%{_bindir}/%{name}-thumbnailer
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-thumbnailer.1*
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_libdir}/%{name}/modules/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/thumbnailers/gwyddion.thumbnailer
%{python_sitearch}/gwy.so

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for Gwyddion
Group:		System/Libraries

%description -n %{libname}
Shared library for Gwyddion and its modules.

%files -n %{libname}
%{_libdir}/lib%{name}%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwyapp}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < %{version}

%description -n %{libgwyapp}
Shared library for Gwyddion and its modules.

%files -n %{libgwyapp}
%{_libdir}/libgwyapp%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwydgets}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < %{version}

%description -n %{libgwydgets}
Shared library for Gwyddion and its modules.

%files -n %{libgwydgets}
%{_libdir}/libgwydgets%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwydraw}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < %{version}

%description -n %{libgwydraw}
Shared library for Gwyddion and its modules.

%files -n %{libgwydraw}
%{_libdir}/libgwydraw%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwymodule}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < %{version}

%description -n %{libgwymodule}
Shared library for Gwyddion and its modules.

%files -n %{libgwymodule}
%{_libdir}/libgwymodule%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwyprocess}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < %{version}

%description -n %{libgwyprocess}
Shared library for Gwyddion and its modules.

%files -n %{libgwyprocess}
%{_libdir}/libgwyprocess%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers, libraries and tools for Gwyddion module development
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{libgwyapp} = %{EVRD}
Requires:	%{libgwydgets} = %{EVRD}
Requires:	%{libgwydraw} = %{EVRD}
Requires:	%{libgwymodule} = %{EVRD}
Requires:	%{libgwyprocess} = %{EVRD}

Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{name}-devel < %{version}
Conflicts:	%{name}-devel < %{version}

%description -n %{devname}
Header files, libraries and tools for Gwyddion module and plug-in development.
This package also contains the API docmentation and sample plug-ins in various
programming languages.

%files -n %{devname}
%doc devel-docs/CODING-STANDARDS
%doc data/%{name}.vim
%{_includedir}/%{name}/
%{_datadir}/gtk-doc/html/*
#%{_datadir}/gtksourceview-2.0/language-specs/pygwy.lang
%{_libdir}/*.so
%{_libdir}/pkgconfig/gwyddion.pc
%{_libdir}/%{name}/include/gwyconfig.h
# Plug-ins and plug-in devel stuff
%{_libdir}/%{name}/perl/
%{_libdir}/%{name}/python/
%{_libdir}/%{name}/ruby/
%{_libexecdir}/%{name}/plugins/

#----------------------------------------------------------------------------

%package thumbnailer-gconf
Summary:	GConf schemas for gwyddion-thumbnailer integration
Group:		Graphical desktop/GNOME
Requires:	%{name} = %{EVRD}

%description thumbnailer-gconf
GConf schemas that register gwyddion-thumbnailer as thumbnailer for SPM files
in GNOME and XFce.

%files thumbnailer-gconf
%{_sysconfdir}/gconf/schemas/gwyddion-thumbnailer.schemas

#----------------------------------------------------------------------------

%package thumbnailer-kde4
Summary:	KDE4 gwyddion thumbnailer module
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description thumbnailer-kde4
Gwyddion-thumbnailer based KDE thumbnail creator extension module for SPM
files.

%files thumbnailer-kde4
%{_libdir}/kde4/gwythumbcreator.so

#----------------------------------------------------------------------------

%prep
%setup -q

# apply all patches
#% patch0 -p1 -b .orig

%build
export PYTHON=%{__python2} 

autoreconf -ifv
%configure \
	--enable-pygwy \
	--with-kde4-thumbnailer \
	--enable-gtk-doc \
	--enable-library-bloat
%make

%install
%makeinstall_std

# localizations
%find_lang %{name}

# Perl, Python, and Ruby modules are private, remove the Perl man page.
rm -f %{buildroot}%{_mandir}/man3/Gwyddion::dump.*

