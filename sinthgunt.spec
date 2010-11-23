Summary:	Easy to use gui for ffmpeg
Name:		sinthgunt
Version:	2.0.3
Release:	%mkrel 1
Source0:	http://sinthgunt.googlecode.com/files/%{name}-%{version}.tar.gz
Url:		http://code.google.com/p/sinthgunt/
License:	GPLv3
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch
BuildRequires:	python-devel 
Requires:	ffmpeg python pygtk2 pygtk2.0-libglade

%description
Sinthgunt is an open source graphical user interface for ffmpeg, a computer 
program that can convert digital audio and video into numerous formats. 
Using pre-configured conversion settings, it makes the task of converting 
between different media formates very easy.

%prep
%setup -q
chmod -x *.txt

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
python setup.py install --skip-build --root $RPM_BUILD_ROOT
python setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

rm -f %buidlroot%_datadir/sinthgunt/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
%{_bindir}/*sinthgunt*
%{python_sitelib}/*
%{_datadir}/%{name}
%{_datadir}/applications/sinthgunt.desktop
%{_datadir}/pixmaps/sinthgunt.png
