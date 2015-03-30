%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename requirefrom

Name:               nodejs-requirefrom
Version:            0.2.0
Release:            1%{?dist}
Summary:            Require from a directory relative to node_modules, flattening your require paths.

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/%{barename}
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

%description
Require from a directory relative to node_modules, flattening your
require paths. Using requireFrom you won\'t have to manage complex
relative paths between each component of your node app.

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
%doc readme.md
%{nodejs_sitelib}/%{barename}/

%changelog
* Tue Mar 24 2015 Robbie Harwood <rharwood@redhat.com> - 0.2.0-1
- Initial packaging for Fedora.
