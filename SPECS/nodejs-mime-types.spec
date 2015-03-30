%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename mime-types

Name:               nodejs-mime-types
Version:            2.0.10
Release:            1%{?dist}
Summary:            The ultimate javascript content-type utility.

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/%{barename}
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

Requires:           npm(mime-db)

%if 0%{?enable_tests}
BuildRequires:      npm(istanbul)
BuildRequires:      npm(mocha)
%endif


%description
Similar to node-mime, except: No fallbacks. Instead of naively
returning the first available type, mime-types simply returns false,
so do var type = mime.lookup('unrecognized') ||
'application/octet-stream'.  No new Mime() business, so you could do
var lookup = require('mime-types').lookup.  Additional mime types are
added such as jade and stylus via mime-db No .define() functionality
Otherwise, the API is compatible.

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
* Thu Mar 25 2015 Robbie Harwood <rharwood@redhat.com> - 2.0.10-1
- Initial packaging for Fedora.
