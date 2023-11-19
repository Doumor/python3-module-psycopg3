%define pypi_name psycopg

%def_without check

Name:    python3-module-%{pypi_name}3
Version: 3.1.12
Release: alt1

Summary: Psycopg 3 is a modern implementation of a PostgreSQL adapter for Python
License: LGPLv3
Group:   Development/Python3
URL:     https://github.com/psycopg/psycopg

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module postgresql-test-rpm-macros
%endif

Requires: libpq5

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup
# disable remove deps for typechecking and linting
sed -r -i 's/("(black|flake8|pytest-cov)\b.*",)/# \1/' setup.py

# remove pproxy dep, only used for tests
sed -r -i 's/("(pproxy)\b.*",)/# \1/' setup.py

# remove version for anyio
sed -i 's/\(anyio\).*$/\1",/' setup.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest ../tests/ -k "not test_typing and not test_module"


%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/psycopg/
%python3_sitelibdir/psycopg-3.2.0.dev1.dist-info

%changelog
* Thu Oct 12 2023 Danilkin Danila <danild@altlinux.org> 3.1.12-alt1
- Initial build for Sisyphus
