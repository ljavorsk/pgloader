Name:           pgloader
Version:        3.6.1
Release:        1%{?dist}
Summary:        Data loading tool for PostgreSQL

License:        PostgreSQL
URL:            https://pgloader.io/
Source0:        https://github.com/dimitri/%{name}/releases/download/v%{version}/%{name}-bundle-%{version}.tgz

BuildRequires:  make sbcl
BuildRequires:  freetds-devel
BuildRequires:  openssl-devel
Requires:       openssl-devel

%description
Data loading tool that allows to implement continuous migration
from current database to PostreSQL.

It uses the COPY PostreSQL protocol to stream the data into the server

pgloader can read data from CSV and DBF files, or SQLite, MySQL,
MS SQL Server, PostgreSQL, Redshift databases.

%package devel
Summary:    Pgloader development header and library files

Requires:   %{name} = %{version}-%{release}

%description devel
Devel package used to building some package against pgloader

%prep
%setup -q -n %{name}-bundle-%{version}


%build
%{set_build_flags}
%define debug_package %{nil}
make save


%install
%{__install} -m 755 -d %{buildroot}/%{_bindir}
%{__install} -m 755 bin/%{name} %{buildroot}%{_bindir}/pgloader

%files
%doc README.md local-projects/%{name}-%{version}/docs
%license local-projects/%{name}-%{version}/LICENSE
%{_bindir}/%{name}


%changelog
* Wed Aug 21 2019 Lukas Javorsky <ljavorsk@redhat.com> - 3.6.1-1
- Initial version of package
