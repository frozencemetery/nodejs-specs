%{?nodejs_find_provides_and_requires}

# Not all test dependencies are packaged
%global enable_tests 0

%global barename mime-db

Name:               nodejs-mime-db
Version:            1.8.0
Release:            2%{?dist}
Summary:            Media Type Database

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/%{barename}
Source0:            https://github.com/jshttp/%{barename}/archive/v%{version}.tar.gz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

%if 0%{?enable_tests}
BuildRequires:      npm(bluebird)
BuildRequires:      npm(co)
BuildRequires:      npm(cogent) # not packaged
BuildRequires:      npm(csv-parse) # not packaged
BuildRequires:      npm(gnode) # not packaged
BuildRequires:      npm(istanbul)
BuildRequires:      npm(mocha)
BuildRequires:      npm(raw-body)
BuildRequires:      npm(stream-to-array) # not packaged
%endif


%description
This is a database of all mime types. It consists of a
single, public JSON file and does not include any logic, allowing it
to remain as un-opinionated as possible with an API. It aggregates
data from the following sources:
http://www.iana.org/assignments/media-types/media-types.xhtml
http://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/conf/mime.types

%prep
%setup -q -n %{barename}-%{version}

# Remove bundled node_modules if there are any.
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{barename}
cp -pr package.json index.js db.json \
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
* Mon Mar 30 2015 Robbie Harwood <rharwood@redhat.com> - 1.8.0-2
- Switch to github tarball which includes tests.

* Thu Mar 26 2015 Robbie Harwood <rharwood@redhat.com> - 1.8.0-1
- Initial packaging for Fedora.
