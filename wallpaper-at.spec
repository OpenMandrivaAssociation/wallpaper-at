%define name wallpaper-at
%define version 0.3
%define release %mkrel 5

Summary:	Wallpapers by Andreas Tille
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		%{name}-%{version}.tar.bz2
License:	GNU Free Documentation License
Group:		Graphics
BuildArchitectures:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

URL:		http://www.steve.org.uk/Software/wallpapers/

%description
This package contains some hopefully nice images to use as a background
or a screen saver.  They were taken by Andreas Tille on various trips to
Iceland (http://www.physik.uni-halle.de/~e2od5/island/).

%package 1280x1024
Summary:	Wallpapers by Andreas Tille @ 1280x1024
Group:		Graphics
Provides:	wallpaper-at

%description 1280x1024
This package contains some hopefully nice images to use as a background
or a screen saver.  They were taken by Andreas Tille on various trips to
Iceland (http://www.physik.uni-halle.de/~e2od5/island/).

The images in this package are best suited for use in a 5:4 aspect ratio,
e.g. 1280x1024.

%package 1600x1200
Summary:	Wallpapers by Andreas Tille @ 1600x1200
Group:		Graphics
Provides:	wallpaper-at

%description 1600x1200
This package contains some hopefully nice images to use as a background
or a screen saver.  They were taken by Andreas Tille on various trips to
Iceland (http://www.physik.uni-halle.de/~e2od5/island/).

The images in this package are best suited for use in a 4:3 aspect ratio,
e.g. 1600x1200, 1152x864, 1024x768, 800x600, or 640x480.

%package 1600x900
Summary:	Wallpapers by Andreas Tille @ 1600x900
Group:		Graphics
Provides:	wallpaper-at

%description 1600x900
This package contains some hopefully nice images to use as a background
or a screen saver.  They were taken by Andreas Tille on various trips to
Iceland (http://www.physik.uni-halle.de/~e2od5/island/).

The images in this package are best suited for use in a 16:9 aspect ratio,
e.g. 1600x900.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/wallpapers
cp --recursive -f 1280x1024/ $RPM_BUILD_ROOT/%{_datadir}/wallpapers
cp --recursive -f 1600x1200/ $RPM_BUILD_ROOT/%{_datadir}/wallpapers
cp --recursive -f 1600x900/  $RPM_BUILD_ROOT/%{_datadir}/wallpapers

%clean
rm -rf ${RPM_BUILD_ROOT}

%files 1280x1024
%defattr(-,root,root)
%doc LICENSE README
%dir %{_datadir}/wallpapers/1280x1024
%{_datadir}/wallpapers/1280x1024/oexarafoss.jpg
%{_datadir}/wallpapers/1280x1024/namafjall2.jpg
%{_datadir}/wallpapers/1280x1024/sheeps.jpg
%{_datadir}/wallpapers/1280x1024/gras.jpg
%{_datadir}/wallpapers/1280x1024/gothafoss.jpg
%{_datadir}/wallpapers/1280x1024/swarti.jpg
%{_datadir}/wallpapers/1280x1024/myvatnevening.jpg
%{_datadir}/wallpapers/1280x1024/elephant.jpg
%{_datadir}/wallpapers/1280x1024/geysir.jpg
%{_datadir}/wallpapers/1280x1024/dandel.jpg
%{_datadir}/wallpapers/1280x1024/paul1.jpg
%{_datadir}/wallpapers/1280x1024/paul2.jpg
%{_datadir}/wallpapers/1280x1024/viti2.jpg
%{_datadir}/wallpapers/1280x1024/saaleck.jpg
%{_datadir}/wallpapers/1280x1024/leirhnjukur.jpg
%{_datadir}/wallpapers/1280x1024/sanssouci.jpg
%{_datadir}/wallpapers/1280x1024/ruegen.jpg
%{_datadir}/wallpapers/1280x1024/thyme.jpg
%{_datadir}/wallpapers/1280x1024/geysirbubble.jpg
%{_datadir}/wallpapers/1280x1024/hafragil.jpg
%{_datadir}/wallpapers/1280x1024/dirholaey.jpg
%{_datadir}/wallpapers/1280x1024/blesi.jpg
%{_datadir}/wallpapers/1280x1024/namafjall.jpg
%{_datadir}/wallpapers/1280x1024/hveravellir.jpg
%{_datadir}/wallpapers/1280x1024/memleben.jpg
%{_datadir}/wallpapers/1280x1024/laugarvatn.jpg

%files 1600x1200
%defattr(-,root,root)
%doc LICENSE README
%dir %{_datadir}/wallpapers/1600x1200
%{_datadir}/wallpapers/1600x1200/namafjall2.jpg
%{_datadir}/wallpapers/1600x1200/sheeps.jpg
%{_datadir}/wallpapers/1600x1200/darsz.jpg
%{_datadir}/wallpapers/1600x1200/gothafoss.jpg
%{_datadir}/wallpapers/1600x1200/swarti.jpg
%{_datadir}/wallpapers/1600x1200/myvatnevening.jpg
%{_datadir}/wallpapers/1600x1200/geysir.jpg
%{_datadir}/wallpapers/1600x1200/dandel.jpg
%{_datadir}/wallpapers/1600x1200/paul1.jpg
%{_datadir}/wallpapers/1600x1200/paul2.jpg
%{_datadir}/wallpapers/1600x1200/viti2.jpg
%{_datadir}/wallpapers/1600x1200/saaleck.jpg
%{_datadir}/wallpapers/1600x1200/leirhnjukur.jpg
%{_datadir}/wallpapers/1600x1200/sanssouci.jpg
%{_datadir}/wallpapers/1600x1200/ruegen.jpg
%{_datadir}/wallpapers/1600x1200/thyme.jpg
%{_datadir}/wallpapers/1600x1200/geysirbubble.jpg
%{_datadir}/wallpapers/1600x1200/hafragil.jpg
%{_datadir}/wallpapers/1600x1200/koeln.jpg
%{_datadir}/wallpapers/1600x1200/hampton_curt.jpg
%{_datadir}/wallpapers/1600x1200/dirholaey.jpg
%{_datadir}/wallpapers/1600x1200/blesi.jpg
%{_datadir}/wallpapers/1600x1200/namafjall.jpg
%{_datadir}/wallpapers/1600x1200/hveravellir.jpg
%{_datadir}/wallpapers/1600x1200/brocken.jpg
%{_datadir}/wallpapers/1600x1200/memleben.jpg
%{_datadir}/wallpapers/1600x1200/laugarvatn.jpg
%{_datadir}/wallpapers/1600x1200/bicyle.jpg

%files 1600x900
%defattr(-,root,root)
%doc LICENSE README
%dir %{_datadir}/wallpapers/1600x900
%{_datadir}/wallpapers/1600x900/sheeps.jpg
%{_datadir}/wallpapers/1600x900/paul1.jpg
%{_datadir}/wallpapers/1600x900/paul2.jpg
%{_datadir}/wallpapers/1600x900/sanssouci.jpg
%{_datadir}/wallpapers/1600x900/brocken.jpg

