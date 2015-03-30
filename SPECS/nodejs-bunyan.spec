%{?nodejs_find_provides_and_requires}

# Several test dependencies are not packaged
%global enable_tests 0

%global barename bunyan

Name:               nodejs-bunyan
Version:            1.3.4
Release:            1%{?dist}
Summary:            a JSON logging library for node.js services

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/%{barename}
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch
BuildRequires:      nodejs-packaging >= 6

# Optional dependencies (not packaged)
# Requires:           npm(dtrace-provider)
# Requires:           npm(mv)
# Requires:           npm(safe-json-stringify)

%if 0%{?enable_tests}
BuildRequires:      npm(ben) # not packaged
BuildRequires:      npm(nodeunit)
BuildRequires:      npm(vasync) # not packaged
BuildRequires:      npm(verror) # not packaged
%endif


%description
a JSON logging library for node.js services and a bunyan CLI tool for
nicely viewing those logs

%prep
%setup -q -n package

# Remove bundled node_modules if there are any.
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{barename}
cp -pr package.json lib/ \
   %{buildroot}%{nodejs_sitelib}/%{barename}

mkdir -p %{buildroot}/%{_bindir}
cp -p bin/bunyan %{buildroot}/%{_bindir}
chmod 0755 %{buildroot}/%{_bindir}/bunyan

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE.txt README.md docs TODO.md
%{nodejs_sitelib}/%{barename}/
%{_bindir}/bunyan

%changelog
* Fri Mar 27 2015 Robbie Harwood <rharwood@redhat.com> - 1.3.4-1
- Initial packaging for Fedora.
