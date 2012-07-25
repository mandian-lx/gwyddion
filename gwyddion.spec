#
# spec file for package gwyddion based on SUSE build service project science
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define libname %mklibname %name 2 0

Name:           gwyddion
Version:        2.29
Release:        1
License:        GPLv2
Summary:        An SPM data visualization and analysis tool
Group:          Sciences/Other

Url:            http://gwyddion.net/
Source0:        http://prdownloads.sourceforge.net/gwyddion/%{name}-%{version}.tar.xz
Source1:        http://prdownloads.sourceforge.net/gwyddion/%{name}-%{version}.tar.xz.sig

BuildRequires:  desktop-file-utils >= 0.9
BuildRequires:  findutils
BuildRequires:  gettext
BuildRequires:  gtkglext-devel
BuildRequires:  gtksourceview-devel
BuildRequires:  kdelibs4-devel >= 4.0
BuildRequires:  libtiff-devel >= 3.6
BuildRequires:  perl >= 5.005
BuildRequires:  python-devel >= 2.2
BuildRequires:  pygtk2.0-devel
BuildRequires:  python-numpy
BuildRequires:  ruby >= 1.8
BuildRequires:  GL-devel
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(glib-2.0) >= 2.8
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.8
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango) >= 1.10
BuildRequires:  fftw3-devel
BuildRequires:  pkgconfig(gconf-2.0)

%define pkglibdir %{_libdir}/%{name}
%define pkglibexecdir %{_libexecdir}/%{name}
%define pkgdatadir %{_datadir}/%{name}
%define pkgincludedir %{_includedir}/%{name}
%define gtkdocdir %{_datadir}/gtk-doc/html
%define gconfdir %{_sysconfdir}/gconf/schemas

%package -n %{libname}
Summary:        Libraries for Gwyddion
Group:          System/Libraries

%package devel
Summary:        Headers, libraries and tools for Gwyddion module development
Group:          Development/C
Requires:       %{libname} = %{version}
# This pulls everything else
Requires:       fftw3-devel
Requires:       gtkglext-devel
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gtk+-2.0) >= 2.8
Requires:       pkgconfig(pango)

%package thumbnailer-gconf
Summary:        GConf schemas for gwyddion-thumbnailer integration
Group:          Graphical desktop/GNOME
Requires:       %{name} = %{version}

%package thumbnailer-kde4
Summary:        KDE4 gwyddion thumbnailer module
Group:          Graphical desktop/KDE
Requires:       %{name} = %{version}

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

%description -n %{libname}
Libraries for Gwyddion and its modules.

%description devel
Header files, libraries and tools for Gwyddion module and plug-in development.
This package also contains the API docmentation and sample plug-ins in various
programming languages.

%description thumbnailer-gconf
GConf schemas that register gwyddion-thumbnailer as thumbnailer for SPM files
in GNOME and XFce.

%description thumbnailer-kde4
Gwyddion-thumbnailer based KDE thumbnail creator extension module for SPM
files.

%prep
%setup -q

%build
%configure2_5x --without-pascal --disable-rpath \
               --with-kde4-thumbnailer --with-fftw3 --with-gl \
               --enable-library-bloat
%make

%install
%makeinstall_std
%find_lang %{name}

# I cannot express this as %%files in a sensible manner, especially not when
# python byte-compilation kicks in.  Set permissions in the filesystem.
find %{buildroot}%{pkglibexecdir} -type f -print0 | xargs -0 chmod 755
find %{buildroot}%{pkglibexecdir} -type f -name \*.rgi -print0 | xargs -0 chmod 644

# Perl, Python, and Ruby modules are private, remove the Perl man page.
rm -f %{buildroot}%{_mandir}/man3/Gwyddion::dump.*

%files -f %{name}.lang
%defattr(755,root,root)
%{_bindir}/%{name}
%{_bindir}/%{name}-thumbnailer
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS
%{pkgdatadir}/pixmaps/*.png
%{pkgdatadir}/pixmaps/*.ico
%{pkgdatadir}/gradients/*
%{pkgdatadir}/glmaterials/*
%{pkgdatadir}/pygwy/*
%{pkgdatadir}/ui/*
%dir %{pkgdatadir}/pixmaps
%dir %{pkgdatadir}/gradients
%dir %{pkgdatadir}/glmaterials
%dir %{pkgdatadir}/pygwy
%dir %{pkgdatadir}/ui
%dir %{pkgdatadir}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-thumbnailer.1*
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{pkglibdir}/modules/file/*.so
%{pkglibdir}/modules/graph/*.so
%{pkglibdir}/modules/layer/*.so
%{pkglibdir}/modules/process/*.so
%{pkglibdir}/modules/tool/*.so
%{pkglibdir}/modules/*.so
%dir %{pkglibdir}/modules/file
%dir %{pkglibdir}/modules/graph
%dir %{pkglibdir}/modules/layer
%dir %{pkglibdir}/modules/process
%dir %{pkglibdir}/modules/tool
%dir %{pkglibdir}/modules
%dir %{pkglibdir}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/thumbnailers/gwyddion.thumbnailer
%{python_sitearch}/gwy.so

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc devel-docs/CODING-STANDARDS
%doc data/%{name}.vim
%{pkgincludedir}/app/*.h
%{pkgincludedir}/libdraw/*.h
%{pkgincludedir}/libprocess/*.h
%{pkgincludedir}/libgwyddion/*.h
%{pkgincludedir}/libgwydgets/*.h
%{pkgincludedir}/libgwymodule/*.h
%dir %{pkgincludedir}/app
%dir %{pkgincludedir}/libdraw
%dir %{pkgincludedir}/libprocess
%dir %{pkgincludedir}/libgwyddion
%dir %{pkgincludedir}/libgwydgets
%dir %{pkgincludedir}/libgwymodule
%dir %{pkgincludedir}
%{_libdir}/*.so
%{_libdir}/pkgconfig/gwyddion.pc
# Documentation
%doc %{gtkdocdir}/libgwyapp/*
%doc %{gtkdocdir}/libgwydraw/*
%doc %{gtkdocdir}/libgwyprocess/*
%doc %{gtkdocdir}/libgwyddion/*
%doc %{gtkdocdir}/libgwydgets/*
%doc %{gtkdocdir}/libgwymodule/*
%doc %dir %{gtkdocdir}/libgwyapp
%doc %dir %{gtkdocdir}/libgwydraw
%doc %dir %{gtkdocdir}/libgwyprocess
%doc %dir %{gtkdocdir}/libgwyddion
%doc %dir %{gtkdocdir}/libgwydgets
%doc %dir %{gtkdocdir}/libgwymodule
%doc %dir %{gtkdocdir}
%doc %dir %{_datadir}/gtk-doc
%{pkglibdir}/include/gwyconfig.h
%dir %{pkglibdir}/include
# Plug-ins and plug-in devel stuff
%{pkglibdir}/perl/Gwyddion/*
%dir %{pkglibdir}/perl/Gwyddion
%dir %{pkglibdir}/perl
%{pkglibdir}/python/Gwyddion/*
%dir %{pkglibdir}/python/Gwyddion
%dir %{pkglibdir}/python
%{pkglibdir}/ruby/gwyddion/*
%dir %{pkglibdir}/ruby/gwyddion
%dir %{pkglibdir}/ruby
# Use filesystem permissions here.
%defattr(-,root,root,755)
%{pkglibexecdir}/plugins/file/*
%{pkglibexecdir}/plugins/process/*
%dir %{pkglibexecdir}/plugins/file
%dir %{pkglibexecdir}/plugins/process
%dir %{pkglibexecdir}/plugins
%dir %{pkglibexecdir}

%files thumbnailer-gconf
%{_sysconfdir}/gconf/schemas/gwyddion-thumbnailer.schemas

%files thumbnailer-kde4
%defattr(-,root,root)
%{_libdir}/kde4/gwythumbcreator.so
