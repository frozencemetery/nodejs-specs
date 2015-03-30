%{?nodejs_find_provides_and_requires}

# Cannot enable tests because test pieces are not packaged
%global enable_tests 0

%global barename is

Name:               nodejs-is
Version:            0.3.0
Release:            2%{?dist}
Summary:            The definitive JavaScript type testing library

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/is
Source0:            https://github.com/enricomarino/%{barename}/archive/v%{version}.tar.gz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

%if 0%{?enable_tests}
BuildRequires:      npm(tape)
BuildRequires:      npm(foreach) # not packaged
BuildRequires:      npm(covert) # not packaged
%endif


%description
To be or not to be? This is the library!

%prep
%setup -q -n %{barename}-%{version}

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/is
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/is

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
npm test
%endif


%files
%doc LICENSE.md README.md
%{nodejs_sitelib}/is/

%changelog
* Mon Mar 30 2015 Robbie Harwood <rharwood@redhat.com> - 0.3.0-2
- Switch to github tarball.
- Update tests invocation.

* Mon Mar 23 2015 Robbie Harwood <rharwood@redhat.com> - 0.3.0-1
- Initial packaging for Fedora.
