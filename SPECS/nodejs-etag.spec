%{?nodejs_find_provides_and_requires}

# Several test dependencies are not packaged.
%global enable_tests 0

%global barename etag

Name:               nodejs-etag
Version:            1.5.1
Release:            2%{?dist}
Summary:            Create simple ETags

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/%{barename}
Source0:            https://github.com/jshttp/etag/archive/v%{version}.tar.gz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

%if 0%{?enable_tests}
BuildRequires:      npm(benchmark) # not packaged
BuildRequires:      npm(beautify-benchmark) # not packaged
BuildRequires:      npm(istanbul)
BuildRequires:      npm(mocha)
BuildRequires:      npm(seedrandom) # not packaged
%endif


%description
Create simple ETags

%prep
%setup -q -n %{barename}-%{version}

# Remove bundled node_modules if there are any.
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{barename}
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/%{barename}

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
npm test
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/%{barename}/

%changelog
* Mon Mar 30 2015 Robbie Harwood <rharwood@redhat.com> - 1.5.1-2
- Switch to github tarball.
- Update tests invocation.

* Wed Mar 25 2015 Robbie Harwood <rharwood@redhat.com> - 1.5.1-1
- Initial packaging for Fedora.
