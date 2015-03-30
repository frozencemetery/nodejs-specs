%{?nodejs_find_provides_and_requires}

# See tests section below
%global enable_tests 0

%global barename elasticsearch

Name:               nodejs-elasticsearch
Version:            3.1.3
Release:            1%{?dist}
Summary:            The official low-level Elasticsearch client for Node.js and the browser.

Group:              Development/Libraries
License:            ASL 2.0
URL:                https://www.npmjs.org/package/%{barename}
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

Requires:           npm(chalk)
Requires:           npm(bluebird)
Requires:           npm(forever-agent)
Requires:           npm(lodash)
Requires:           npm(lodash-node)

%if 0%{?enable_tests}
# it is unlikely that these are packaged and the right version for everything
BuildRequires:       npm(aliasify)
BuildRequires:       npm(async)
BuildRequires:       npm(blanket)
BuildRequires:       npm(browserify)
BuildRequires:       npm(expect.js)
BuildRequires:       npm(express)
BuildRequires:       npm(find-root)
BuildRequires:       npm(glob)
BuildRequires:       npm(grunt)
BuildRequires:       npm(grunt-browserify)
BuildRequires:       npm(grunt-cli)
BuildRequires:       npm(grunt-contrib-clean)
BuildRequires:       npm(grunt-contrib-compress)
BuildRequires:       npm(grunt-contrib-concat)
BuildRequires:       npm(grunt-contrib-copy)
BuildRequires:       npm(grunt-contrib-jshint)
BuildRequires:       npm(grunt-contrib-uglify)
BuildRequires:       npm(grunt-contrib-watch)
BuildRequires:       npm(grunt-esvm)
BuildRequires:       npm(grunt-mocha-cov)
BuildRequires:       npm(grunt-open)
BuildRequires:       npm(grunt-prompt)
BuildRequires:       npm(grunt-run)
BuildRequires:       npm(grunt-s3)
BuildRequires:       npm(grunt-saucelabs)
BuildRequires:       npm(jquery)
BuildRequires:       npm(js-yaml)
BuildRequires:       npm(load-grunt-config)
BuildRequires:       npm(load-grunt-tasks)
BuildRequires:       npm(mocha)
BuildRequires:       npm(mocha-lcov-reporter)
BuildRequires:       npm(mocha-screencast-reporter)
BuildRequires:       npm(moment)
BuildRequires:       npm(nock)
BuildRequires:       npm(open)
BuildRequires:       npm(optimist)
BuildRequires:       npm(semver)
BuildRequires:       npm(sinon)
BuildRequires:       npm(split)
BuildRequires:       npm(through2)
BuildRequires:       npm(through2-map)
BuildRequires:       npm(xmlbuilder)
%endif


%description
One-to-one mapping with REST API and the other official clients
Generalized, pluggable architecture.  Configurable, automatic
discovery of cluster nodes Persistent, Keep-Alive connections Load
balancing (with pluggable selection strategy) across all available
nodes.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any.
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep chalk ">=0.4.0 <1.0.0"
%nodejs_fixdep bluebird "^2.3.11"
%nodejs_fixdep forever-agent ">=0.5.0 <1.0.0"
%nodejs_fixdep lodash ">=2.4.1 <4.0.0"

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{barename}
cp -pr package.json src/ \
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
* Wed Mar 25 2015 Robbie Harwood <rharwood@redhat.com> - 3.1.3-1
- Initial packaging for Fedora.
