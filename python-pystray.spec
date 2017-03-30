%if 0%{?fedora} || 0%{?rhel} >= 8
%bcond_without python3
%global _pkgdocdir_py2 %{_docdir}/python2-%{upname}
%global _pkgdocdir_py3 %{_docdir}/python3-%{upname}
%else
%bcond_with python3
%global _pkgdocdir_py2 %{_docdir}/python2-%{upname}-%{version}
%global _pkgdocdir_py3 %{_docdir}/python3-%{upname}-%{version}
%endif

# Testsuite needs human interaction.
%bcond_with test

%global common_sum Provides system tray integration
%global common_desc This library allows you to create a system tray icon.

%global upname pystray


Name:		python-%{upname}
Version:	0.14.3
Release:	1%{?dist}
Summary:	%{common_sum}

License:	LGPLv3+
URL:		https://github.com/moses-palmer/%{upname}
Source0:	%{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

%description
%{common_desc}


%package -n python2-%{upname}
Summary:	%{common_sum}

BuildRequires:	python-pillow
BuildRequires:	python-setuptools
BuildRequires:	python-six
BuildRequires:	python-xlib		>= 0.17
BuildRequires:	python2-devel		>= 2.7

Requires:	python-pillow
Requires:	python-six
Requires:	python-xlib		>= 0.17

%{?python_provide:%python_provide python2-%{upname}}

%description -n python2-%{upname}
%{common_desc}


%package -n python2-%{upname}-doc
Summary:	Documentation-files for python2-%{upname}

BuildRequires:	fdupes
BuildRequires:	python-sphinx		>= 1.3.1

%description -n python2-%{upname}-doc
This package contains the Documentation-files for python2-%{upname}.


%if %{with python3}
%package -n python3-%{upname}
Summary:	%{common_sum}

BuildRequires:	python3-devel		>= 3.4
BuildRequires:	python3-pillow
BuildRequires:	python3-setuptools
BuildRequires:	python3-six
BuildRequires:	python3-xlib		>= 0.17

Requires:	python3-pillow
Requires:	python3-six
Requires:	python3-xlib		>= 0.17

%{?python_provide:%python_provide python3-%{upname}}

%description -n python3-%{upname}
%{common_desc}


%package -n python3-%{upname}-doc
Summary:	Documentation-files for python3-%{upname}

BuildRequires:	fdupes
BuildRequires:	python3-sphinx		>= 1.3.1

%description -n python3-%{upname}-doc
This package contains the Documentation-files for python3-%{upname}.
%endif # with python3


%prep
%autosetup -n %{upname}-%{version}

# Remove pre-built and bundled crap.
%{__rm} -fr *.egg*


%build
%py2_build
%{_bindir}/sphinx-build-%{python2_version} docs docs/build-%{python2_version}/html
%fdupes -s docs/build-%{python2_version}
%if %{with python3}
%py3_build
%{_bindir}/sphinx-build-%{python3_version} docs docs/build-%{python3_version}/html
%fdupes -s docs/build-%{python3_version}
%endif # with python3
for f in .buildinfo .doctrees .inv ; do
	%{_bindir}/find docs/ -name "*${f}*" -print0 |			\
		%{_bindir}/xargs -0 %{__rm} -frv
done


%install
%py2_install
%{__mkdir} -p %{buildroot}%{_pkgdocdir_py2}
%{__cp} -pr CHANGES.rst README.rst docs/build-%{python2_version}/html	\
	%{buildroot}%{_pkgdocdir_py2}
%if %{with python3}
%py3_install
%{__mkdir} -p %{buildroot}%{_pkgdocdir_py3}
%{__cp} -pr CHANGES.rst README.rst docs/build-%{python3_version}/html	\
	%{buildroot}%{_pkgdocdir_py3}
%endif # with python3


%if %{with test}
%check
%{__python2} setup.py test
%if %{with python3}
%{__python3} setup.py test
%endif # with python3
%endif # with test


%files -n python2-%{upname}
%license COPYING*
%doc %dir %{_pkgdocdir_py2}
%doc %{_pkgdocdir_py2}/README.rst
%{python2_sitelib}/%{upname}
%{python2_sitelib}/%{upname}-%{version}-py%{python2_version}.egg-info


%files -n python2-%{upname}-doc
%license %{_datadir}/licenses/python2-%{upname}*
%doc %{_pkgdocdir_py2}


%if %{with python3}
%files -n python3-%{upname}
%license COPYING*
%doc %dir %{_pkgdocdir_py3}
%doc %{_pkgdocdir_py3}/README.rst
%{python3_sitelib}/%{upname}
%{python3_sitelib}/%{upname}-%{version}-py%{python3_version}.egg-info


%files -n python3-%{upname}-doc
%license %{_datadir}/licenses/python3-%{upname}*
%doc %{_pkgdocdir_py3}
%endif # with python3


%changelog
* Thu Mar 30 2017 Björn Esser <besser82@fedoraproject.org> - 0.14.3-1
- New upstream release (rhbz#1437277)

* Wed Mar 29 2017 Björn Esser <besser82@fedoraproject.org> - 0.14.2-1
- Initial import (rhbz#1436347)

* Tue Mar 28 2017 Björn Esser <besser82@fedoraproject.org> - 0.14.2-0.2
- Added versioned (Build)Requires

* Mon Mar 27 2017 Björn Esser <besser82@fedoraproject.org> - 0.14.2-0.1
- New upstream release

* Mon Mar 27 2017 Björn Esser <besser82@fedoraproject.org> - 0.14.1-0.1
- Initial rpm-release (rhbz#1436347)
