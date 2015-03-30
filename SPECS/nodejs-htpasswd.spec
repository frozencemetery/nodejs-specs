%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename htpasswd

Name:               nodejs-htpasswd
Version:            2.1.6
Release:            1%{?dist}
Summary:            Node.js module for Apache style password encryption using md5.

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/%{barename}
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

%if 0%{?enable_tests}
BuildRequires:      npm(nodeunit)
%endif


%description
Node.js module for Apache style password encryption using md5.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any.
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep coffee-script "^1.6.0"

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
* Tue Mar 24 2015 Robbie Harwood <rharwood@redhat.com> - 2.1.6-1
- Initial packaging for Fedora.
