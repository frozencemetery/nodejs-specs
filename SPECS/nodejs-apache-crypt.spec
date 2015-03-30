%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename apache-crypt

Name:               nodejs-apache-crypt
Version:            1.0.8
Release:            2%{?dist}
Summary:            Node.js module for Apache style password encryption using crypt(3).

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/%{barename}
Source0:            https://github.com/gevorg/%{barename}/archive/%{version}.tar.gz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

%if 0%{?enable_tests}
BuildRequires:      npm(nodeunit)
%endif


%description
Node.js module for Apache style password encryption using crypt(3).

%prep
%setup -q -n %{barename}-%{version}

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
npm test
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/%{barename}/

%changelog
* Mon Mar 30 2015 Robbie Harwood <rharwood@redhat.com> - 1.0.8-2
- Switch to github tarball.
- Update tests invocation.

* Tue Mar 24 2015 Robbie Harwood <rharwood@redhat.com> - 1.0.8-1
- Initial packaging for Fedora.
