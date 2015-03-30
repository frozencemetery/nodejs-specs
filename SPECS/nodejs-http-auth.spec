%{?nodejs_find_provides_and_requires}

# Cannot enable tests because test pieces are not packaged
%global enable_tests 0

%global barename http-auth

Name:               nodejs-http-auth
Version:            2.2.5
Release:            3%{?dist}
Summary:            Node.js package for HTTP basic and digest access authentication.

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/%{barename}
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

Requires:           npm(coffee-script)
Requires:           npm(node-uuid)
Requires:           npm(htpasswd)

%if 0%{?enable_tests}
BuildRequires:      npm(nodeunit)
BuildRequires:      npm(express)
BuildRequires:      npm(http-proxy) # not packaged
BuildRequires:      npm(request)
%endif


%description
Node.js package for HTTP basic and digest access authentication.

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
cp -pr package.json data/ lib/ \
    %{buildroot}%{nodejs_sitelib}/%{barename}

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE README.md examples/
%{nodejs_sitelib}/%{barename}/

%changelog
* Tue Mar 24 2015 Robbie Harwood <rharwood@redhat.com> - 2.2.5-3
- Include htpasswd dependency.

* Tue Mar 24 2015 Robbie Harwood <rharwood@redhat.com> - 2.2.5-2
- Correct dependencies.

* Tue Mar 24 2015 Robbie Harwood <rharwood@redhat.com> - 2.2.5-1
- Initial packaging for Fedora.
