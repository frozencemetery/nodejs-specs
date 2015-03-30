%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename node.extend

Name:               nodejs-node-dot-extend
Version:            1.0.10
Release:            2%{?dist}
Summary:            A port of jQuery.extend that actually works on node.js

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/node.extend
Source0:            https://github.com/dreamerslab/%{barename}/archive/v%{version}.tar.gz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

Requires:           npm(is)

%if 0%{?enable_tests}
BuildRequires:      npm(tape)
%endif


%description
A port of jQuery.extend that actually works on node.js

%prep
%setup -q -n %{barename}-%{version}

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/node.extend
cp -pr package.json index.js lib \
   %{buildroot}%{nodejs_sitelib}/node.extend

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
npm test
%endif


%files
%doc Readme.md
%{nodejs_sitelib}/node.extend/

%changelog
* Mon Mar 23 2015 Robbie Harwood <rharwood@redhat.com> - 1.0.10-2
- Switch to github tarball.
- Correct tests command.

* Mon Mar 23 2015 Robbie Harwood <rharwood@redhat.com> - 1.0.10-1
- Initial packaging for Fedora.
