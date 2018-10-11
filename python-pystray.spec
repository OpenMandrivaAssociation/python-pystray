# Testsuite needs human interaction.
%bcond_with test

%global common_sum Provides system tray integration
%global common_desc This library allows you to create a system tray icon.

%global upname pystray


Name:		python-%{upname}
Version:	0.14.3
Release:	7%{?dist}
Summary:	%{common_sum}

License:	LGPLv3+
URL:		https://github.com/moses-palmer/%{upname}
Source0:	%{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

%description
%{common_desc}


%package -n python3-%{upname}
Summary:	%{common_sum}

BuildRequires:	python3-devel >= 3.4
BuildRequires:	python3-pillow
BuildRequires:	python3-setuptools
BuildRequires:	python3-six
BuildRequires:	python3-xlib >= 0.17

Requires:	python3-pillow
Requires:	python3-six
Requires:	python3-xlib		>= 0.17

%{?python_provide:%python_provide python3-%{upname}}

%description -n python3-%{upname}
%{common_desc}


%package -n python3-%{upname}-doc
Summary:	Documentation-files for python3-%{upname}

BuildRequires:	fdupes
BuildRequires:	python3-sphinx >= 1.3.1

%description -n python3-%{upname}-doc
This package contains the Documentation-files for python3-%{upname}.


%prep
%autosetup -n %{upname}-%{version}

# Remove pre-built and bundled crap.
%{__rm} -fr *.egg*


%build
%py3_build
sphinx-build-3 docs docs/build-%{python3_version}/html
%fdupes -s docs/build-%{python3_version}
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


%files -n python3-%{upname}
%license COPYING*
%doc README.rst
%{python3_sitelib}/%{upname}
%{python3_sitelib}/%{upname}-%{version}-py%{python3_version}.egg-info

%files -n python3-%{upname}-doc
%doc CHANGES.rst docs/build-%{python3_version}/html


%changelog
* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.14.3-7
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14.3-5
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.14.3-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

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
