%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename serve-favicon

Name:               nodejs-serve-favicon
Version:            2.2.0
Release:            2%{?dist}
Summary:            favicon serving middleware with caching

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/%{barename}
Source0:            https://github.com/expressjs/%{barename}/archive/v%{version}.tar.gz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

Requires:           npm(etag)
Requires:           npm(fresh)
Requires:           npm(ms)
Requires:           npm(parseurl)

%if 0%{?enable_tests}
BuildRequires:      npm(istanbul)
BuildRequires:      npm(mocha)
BuildRequires:      npm(proxyquire)
BuildRequires:      npm(supertest)
%endif


%description
User agents request favicon.ico frequently and indiscriminately, so
you may wish to exclude these requests from your logs by using this
middleware before your logger middleware.  This module caches the icon
in memory to improve performance by skipping disk access.  This module
provides an ETag based on the contents of the icon, rather than file
system properties.  This module will serve with the most compatible
Content-Type.

%prep
%setup -q -n %{barename}-%{version}

# Remove bundled node_modules if there are any.
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep fresh "~0.2.2"
%nodejs_fixdep ms ">=0.6.2 <1.0.0"
%nodejs_fixdep parseurl "^1.0.1"

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
* Wed Mar 25 2015 Robbie Harwood <rharwood@redhat.com> - 2.2.0-2
- Switch to Github tarball.
- Correct test invocation.

* Wed Mar 25 2015 Robbie Harwood <rharwood@redhat.com> - 2.2.0-1
- Initial packaging for Fedora.
