# Testsuite needs human interaction.
%bcond_with test

%global upname pystray


Name:		python-%{upname}
Version:	0.19.5
Release:	3
Summary:	Python module for system tray integration

License:	LGPLv3+
URL:		https://github.com/moses-palmer/%{upname}
Source0:	%{url}/archive/v%{version}.tar.gz#/%{upname}-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(six)
BuildRequires:	python%{pyver}dist(python-xlib) >= 0.17

Requires:	python%{pyver}dist(pillow)
Requires:	python%{pyver}dist(six)
Requires:	python%{pyver}dist(python-xlib) >= 0.17
BuildArch:	noarch

%description
This library allows you to create a system tray icon in Python.

%package doc
Summary:	Documentation-files for python3-%{upname}
BuildRequires:	python-sphinx >= 1.3.1

%description doc
This package contains the Documentation-files for python-%{upname}.

%prep
%autosetup -n %{upname}-%{version}

# Remove pre-built and bundled crap.
%{__rm} -fr *.egg*

%build
%py3_build
sphinx-build docs docs/build-%{python3_version}/html
for f in .buildinfo .doctrees .inv ; do
	%{_bindir}/find docs/ -name "*${f}*" -print0 |			\
		%{_bindir}/xargs -0 %{__rm} -frv
done


%install
%py3_install

%if %{with test}
%check
%{__python3} setup.py test
%endif # with test


%files
%license COPYING*
%doc README.rst
%{python3_sitelib}/%{upname}
%{python3_sitelib}/%{upname}-%{version}-py%{python3_version}.egg-info

%files doc
%doc CHANGES.rst docs/build-%{python3_version}/html
