%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename ee-first

Name:               nodejs-ee-first
Version:            1.1.0
Release:            1%{?dist}
Summary:            return the first event in a set of ee/event pairs

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/%{barename}
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

%if 0%{?enable_tests}
BuildRequires:      npm(istanbul)
BuildRequires:      npm(mocha)
BuildRequires:      npm(should)
%endif


%description
Get the first event in a set of event emitters and event pairs, then
clean up after itself.

%prep
%setup -q -n package

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
grunt test
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/%{barename}/

%changelog
* Wed Mar 25 2015 Robbie Harwood <rharwood@redhat.com> - 0.3.0-1
- Initial packaging for Fedora.
