%define major 0
%define api 2
%define libname %mklibname %{name} %{api} %{major}
%define libgwyapp %mklibname gwyapp %{api} %{major}
%define libgwydgets %mklibname gwydgets %{api} %{major}
%define libgwydraw %mklibname gwydraw %{api} %{major}
%define libgwymodule %mklibname gwymodule %{api} %{major}
%define libgwyprocess %mklibname gwyprocess %{api} %{major}
%define devname %mklibname %{name} %{api} -d

Summary:	An SPM data visualization and analysis tool
Name:		gwyddion
Version:	2.35
Release:	2
License:	GPLv2+
Group:		Sciences/Other
Url:		http://gwyddion.net/
Source0:	http://prdownloads.sourceforge.net/gwyddion/%{name}-%{version}.tar.xz
Source1:	http://prdownloads.sourceforge.net/gwyddion/%{name}-%{version}.tar.xz.sig

BuildRequires:	python-numpy
BuildRequires:	ruby
BuildRequires:	bzip2-devel
BuildRequires:	kdelibs4-devel
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
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(minizip)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(zlib)

%description
Gwyddion is a modular SPM (Scanning Probe Microsopy) data visualization and
analysis tool written with Gtk+.

It can be used for all most frequently used data processing operations
including: leveling, false color plotting, shading, filtering, denoising, data
editing, integral transforms, grain analysis, profile extraction, fractal
analysis, and many more.  The program is primarily focused on SPM data analysis
(e.g. data obtained from AFM, STM, NSOM, and similar microscopes).  However, it
can also be used for analysis of SEM (Scanning Electron Microscopy) data or any
other 2D data.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/%{name}-thumbnailer
%doc AUTHORS NEWS README THANKS
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
Conflicts:	%{_lib}gwyddion2_0 < 2.34

%description -n %{libgwyapp}
Shared library for Gwyddion and its modules.

%files -n %{libgwyapp}
%{_libdir}/libgwyapp%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwydgets}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < 2.34

%description -n %{libgwydgets}
Shared library for Gwyddion and its modules.

%files -n %{libgwydgets}
%{_libdir}/libgwydgets%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwydraw}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < 2.34

%description -n %{libgwydraw}
Shared library for Gwyddion and its modules.

%files -n %{libgwydraw}
%{_libdir}/libgwydraw%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwymodule}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < 2.34

%description -n %{libgwymodule}
Shared library for Gwyddion and its modules.

%files -n %{libgwymodule}
%{_libdir}/libgwymodule%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgwyprocess}
Summary:	Shared library for Gwyddion
Group:		System/Libraries
Conflicts:	%{_lib}gwyddion2_0 < 2.34

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
Obsoletes:	%{name}-devel < 2.34
Conflicts:	%{name}-devel < 2.34

%description -n %{devname}
Header files, libraries and tools for Gwyddion module and plug-in development.
This package also contains the API docmentation and sample plug-ins in various
programming languages.

%files -n %{devname}
%doc devel-docs/CODING-STANDARDS
%doc data/%{name}.vim
%{_includedir}/%{name}/
%{_datadir}/gtk-doc/html/*
%{_datadir}/gtksourceview-2.0/language-specs/pygwy.lang
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

%build
%configure2_5x \
	--without-pascal \
	--disable-rpath \
	--with-kde4-thumbnailer \
	--with-fftw3 \
	--with-gl \
	--enable-library-bloat
%make

%install
%makeinstall_std

%find_lang %{name}

# I cannot express this as %%files in a sensible manner, especially not when
# python byte-compilation kicks in.  Set permissions in the filesystem.
find %{buildroot}%{_libexecdir}/%{name} -type f -print0 | xargs -0 chmod 755
find %{buildroot}%{_libexecdir}/%{name} -type f -name \*.rgi -print0 | xargs -0 chmod 644

# Perl, Python, and Ruby modules are private, remove the Perl man page.
rm -f %{buildroot}%{_mandir}/man3/Gwyddion::dump.*

