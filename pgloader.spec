# Disabling the debug package generation
# Build error if not disabled
%global debug_package %{nil}

Name:           pgloader
Version:        3.6.1
Release:        1%{?dist}
Summary:        Data loading tool for PostgreSQL

License:        PostgreSQL
URL:            https://pgloader.io/
Source0:        https://github.com/dimitri/%{name}/releases/download/v%{version}/%{name}-bundle-%{version}.tgz

# sbcl package is not supported on other architectures
# Bug in BZ needs to be added after review for every non-supported arch
# then only bz number commented here
ExclusiveArch: %{arm} %{ix86} x86_64 ppc sparcv9 aarch64

BuildRequires:  make
BuildRequires:  sbcl
BuildRequires:  freetds-devel
BuildRequires:  openssl-devel
# Builds the man pages with sphinx-build
BuildRequires:  python-sphinx
Requires:       openssl-devel

%description
Data loading tool that allows to implement continuous migration
from current database to PostreSQL.

It uses the COPY PostreSQL protocol to stream the data into the server.

Pgloader can read data from CSV and DBF files, or SQLite, MySQL,
MS SQL Server, PostgreSQL, Redshift databases.

%prep
%setup -q -n %{name}-bundle-%{version}

%build
%{set_build_flags}
%{make_build} save
%{make_build} -C local-projects/%{name}-%{version}/docs/ man

%install
%{__install} -m 755 -d %{buildroot}/%{_bindir}
%{__install} -m 755 bin/%{name} %{buildroot}%{_bindir}/pgloader
%{__install} -m 755 -d %{buildroot}/%{_mandir}/man1
%{__install} -m 644 %{_builddir}/%{name}-bundle-%{version}/local-projects/%{name}-%{version}/docs/_build/man/pgloader.1 %{buildroot}%{_mandir}/man1

%files
%doc README.md
%{_mandir}/man1/pgloader.1.gz
%license local-projects/%{name}-%{version}/LICENSE
%{_bindir}/%{name}


%changelog
* Wed Aug 21 2019 Lukas Javorsky <ljavorsk@redhat.com> - 3.6.1-1
- Initial version of package
