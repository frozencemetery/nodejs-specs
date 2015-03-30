%{?nodejs_find_provides_and_requires}

# Several test dependencies are not packaged.
%global enable_tests 0

%global barename crc

Name:               nodejs-crc
Version:            3.2.1
Release:            1%{?dist}
Summary:            Various CRC JavaScript implementations

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/%{barename}
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

%if 0%{?enable_tests}
BuildRequires:      npm(beautify-benchmark) # not packaged
BuildRequires:      npm(benchmark) # not packaged
BuildRequires:      npm(buffer-crc32)
BuildRequires:      npm(chai)
BuildRequires:      npm(coffee-errors) # not packaged
BuildRequires:      npm(coffee-script)
BuildRequires:      npm(mocha)
BuildRequires:      npm(seedrandom) # not packaged
%endif


%description
Module for calculating Cyclic Redundancy Check (CRC).

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

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/%{barename}/

%changelog
* Wed Mar 25 2015 Robbie Harwood <rharwood@redhat.com> - 3.2.1-1
- Initial packaging for Fedora.
