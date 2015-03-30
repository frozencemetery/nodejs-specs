%{?nodejs_find_provides_and_requires}

# Tests disabled because not all required components are packaged
%global enable_tests 0

%global barename less-middleware

Name:               nodejs-less-middleware
Version:            1.0.4
Release:            3%{?dist}
Summary:            LESS.js middleware for connect.

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/less-middleware
Source0:            https://github.com/emberfeather/less.js-middleware/archive/%{version}.tar.gz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

Requires:           npm(less)
Requires:           npm(mkdirp)
Requires:           npm(node.extend)

%if 0%{?enable_tests}
BuildRequires:      npm(mocha) # not packaged
BuildRequires:      npm(supertest) # too new
BuildRequires:      npm(express) # too new
BuildRequires:      npm(fs-extra) # too old
%endif


%description
This middleware was created to allow processing of Less files for
Connect JS framework and by extension the Express JS framework.

%prep
%setup -q -n less.js-middleware-%{version}

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep less '^1.7.0'

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/less-middleware
cp -pr package.json lib \
   %{buildroot}%{nodejs_sitelib}/less-middleware

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
npm test
%endif


%files
%doc license readme.md
%{nodejs_sitelib}/less-middleware/

%changelog
* Mon Mar 23 2015 Robbie Harwood <rharwood@redhat.com> - 1.0.4-3
- Work around .x interaction with fixdep.

* Mon Mar 23 2015 Robbie Harwood <rharwood@redhat.com> - 1.0.4-2
- Switch to github tarball.
- Update test invocations.

* Mon Mar 23 2015 Robbie Harwood <rharwood@redhat.com> - 1.0.4-1
- Initial packaging for Fedora.
