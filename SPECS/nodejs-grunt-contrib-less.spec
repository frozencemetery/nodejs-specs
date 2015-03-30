# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

# Well, upstream doesn't ship tests with the tarball:
# https://github.com/gruntjs/grunt-contrib-less/issues/228
%global enable_tests 0

%global barename grunt-contrib-less

Name:               nodejs-grunt-contrib-less
Version:            0.12.0
Release:            1%{?dist}
Summary:            Compile LESS files to CSS

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-contrib-less
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(chalk)
BuildRequires:      npm(grunt-lib-contrib)
BuildRequires:      npm(grunt)
BuildRequires:      npm(less)

Requires:           npm(chalk)
Requires:           npm(grunt-lib-contrib)
Requires:           npm(grunt)
Requires:           npm(less)

%if 0%{?enable_tests}
BuildRequires:      npm(grunt-contrib-nodeunit)
# We patch this guy out since it:
# 1) Has 8 unpackaged dependencies itself
# 2) is really just static analysis, not for tests.
#BuildRequires:      npm(grunt-contrib-jshint)
BuildRequires:      npm(grunt)
BuildRequires:      npm(grunt-contrib-internal)
BuildRequires:      npm(grunt-contrib-clean)
BuildRequires:      nodejs-grunt-cli
%endif


%description
Compile LESS files to CSS.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep chalk '>=0.4.0'
%nodejs_fixdep maxmin '>=0.2.0'
%nodejs_fixdep less '>=1.7.0'

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-contrib-less
cp -pr package.json tasks \
    %{buildroot}%{nodejs_sitelib}/grunt-contrib-less

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/grunt-contrib-less/

%changelog
* Tue Nov 25 2014 Ralph Bean <rbean@redhat.com> - 0.12.0-1
- Latest upstream.
- Fixdep on maxmin and less (upstream re-pinned it with no other changes).

* Mon Nov 24 2014 Ralph Bean <rbean@redhat.com> - 0.11.4-2
- Add some notes about running the tests.  Still not enabled.
- Pull a nodejs_fixdep on npm(chalk).

* Thu Oct 23 2014 Ralph Bean <rbean@redhat.com> - 0.11.4-1
- Latest upstream.
- Build as noarch.

* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.9.0-1
- Initial packaging for Fedora.
