%{?nodejs_find_provides_and_requires}

# Several test dependencies are not packaged.
%global enable_tests 0

%global barename depd

Name:               nodejs-depd
Version:            1.0.0
Release:            2%{?dist}
Summary:            Deprecate all the things

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/%{barename}
Source0:            https://github.com/dougwilson/nodejs-%{barename}/archive/v%{version}.tar.gz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

%if 0%{?enable_tests}
BuildRequires:      npm(beautify-benchmark) # not packaged
BuildRequires:      npm(benchmark) # not packaged
BuildRequires:      npm(istanbul)
BuildRequires:      npm(mocha)
BuildRequires:      npm(should)
%endif


%description
With great modules comes great responsibility; mark things deprecated!

%prep
%setup -q -n nodejs-%{barename}-%{version}

# Remove bundled node_modules if there are any.
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{barename}
cp -pr package.json index.js lib/ \
    %{buildroot}%{nodejs_sitelib}/%{barename}

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
npm test
%endif


%files
%doc LICENSE Readme.md
%{nodejs_sitelib}/%{barename}/

%changelog
* Mon Mar 30 2015 Robbie Harwood <rharwood@redhat.com> - 1.0.0-2
- Switch to github tarball.
- Correct test invocation.

* Wed Mar 25 2015 Robbie Harwood <rharwood@redhat.com> - 1.0.0-1
- Initial packaging for Fedora.
