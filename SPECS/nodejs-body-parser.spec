%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename body-parser

Name:               nodejs-body-parser
Version:            1.10.2
Release:            1%{?dist}
Summary:            Node.js body parsing middleware

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/%{barename}
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

Requires:           npm(bytes)
Requires:           npm(depd)
Requires:           npm(iconv-lite)
Requires:           npm(media-typer)
Requires:           npm(on-finished)
Requires:           npm(qs)
Requires:           npm(raw-body)
Requires:           npm(type-is)

%if 0%{?enable_tests}
BuildRequires:      npm(istanbul)
BuildRequires:      npm(methods)
BuildRequires:      npm(mocha)
BuildRequires:      npm(supertest)
%endif


%description
Node.js body parsing middleware.  This does not handle multipart
bodies, due to their complex and typically large nature.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any.
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep bytes ">=0.3.0 <=1.0.0"
%nodejs_fixdep iconv-lite ">=0.2.11 <1.0.0"
%nodejs_fixdep qs ">=0.6.6 <3.0.0"
%nodejs_fixdep raw-body ">=1.1.4 <2.0.0"

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{barename}
cp -pr package.json index.js lib/ \
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
* Fri Mar 27 2015 Robbie Harwood <rharwood@redhat.com> - 1.10.2-1
- Initial packaging for Fedora.
