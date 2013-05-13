Name:		ksuperkey
Summary:	A service to an open application launcher in KDE with Super key
Version:	0.3
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv3+
# And also https://github.com/hanschen/ksuperkey
Url:		http://kde-apps.org/content/show.php/ksuperkey?content=154569
Source:		http://kde-apps.org/CONTENT/content-files/154569-%{name}-%{version}.tar.gz
BuildRequires:	kde4-macros
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)

%description
KSuperKey allows you to open the application launcher in KDE Plasma Desktop
using the Super key (also known as the "Windows key"). If you hold down the
Super key it will still act as a modifier key, allowing you to use it for
other keyboard shortcuts.

KSuperKey is a small application that runs in the background as a daemon.
It was forked from xcape by Albin Olsson: https://github.com/alols/xcape

%files
%{_kde_bindir}/%{name}
%{_kde_autostart}/%{name}.desktop

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%setup_compile_flags
%make

%install
%makeinstall_std

# Autostart service code, from git (should be removed when 0.4 is released)
mkdir -p %{buildroot}%{_kde_autostart}
cat > %{buildroot}%{_kde_autostart}/%{name}.desktop << EOF
[Desktop Entry]
Exec=ksuperkey
X-DBUS-StartupType=none
Name=ksuperkey
Type=Service
X-KDE-StartupNotify=false
OnlyShowIn=KDE;
X-KDE-autostart-phase=2
EOF

