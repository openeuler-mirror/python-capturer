%global pyname capturer

Name:           python-%{pyname}
Version:        3.0
Release:        1
Summary:        Easily capture stdout/stderr of the current process and subprocesses

License:        MIT
URL:            https://%{pyname}.readthedocs.io
Source0:        https://github.com/xolox/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
The capturer package makes it easy to capture the stdout and stderr streams of
the current process and subprocesses. Output can be relayed to the terminal in
real time but is also available to the Python program for additional processing.


%package doc
Summary:        Documentation for the python capturer module
BuildRequires:  python%{python3_pkgversion}-humanfriendly >= 8.0
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation for the python capturer module


%package -n python%{python3_pkgversion}-%{pyname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-humanfriendly >= 8.0
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pyname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-humanfriendly >= 8.0
%endif

Suggests:       %{name}-doc = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{pyname}
The capturer package makes it easy to capture the stdout and stderr streams of
the current process and subprocesses. Output can be relayed to the terminal in
real time but is also available to the Python program for additional processing.


%prep
%autosetup -p1


%build
%py3_build

rm build/lib/%{pyname}/tests.py
sphinx-build-%{python3_version} -nb html -d docs/build/doctrees docs docs/build/html
rm docs/build/html/.buildinfo


%install
%py3_install


%check
PYTHONUNBUFFERED=1 py.test-%{python3_version} %{pyname}/tests.py


%files doc
%license LICENSE.txt
%doc docs/build/html

%files -n python%{python3_pkgversion}-%{pyname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pyname}/
%{python3_sitelib}/%{pyname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri Jun 25 2021 xuhe <xuhe@kylinos.cn> - 3.0-1
- Package init

