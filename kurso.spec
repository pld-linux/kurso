Summary:	Esperanto language course
Summary(pl):	Kurs jêzyka esperanto
Name:		kurso
Version:	20040531
Release:	0.1
License:	GPL (w/o sources - sic! - so non-distributable, possibly illegal)
Group:		X11/Applications/Science
Source0:	http://www.cursodeesperanto.com.br/%{name}.tar.gz
# NoSource0-md5:	480a07c5daf67e5fa0527f252f328af0
NoSource:	0
URL:		http://www.cursodeesperanto.com.br/bazo/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
Esperanto language course.

%description -l pl
Kurs jêzyka esperanto.

%prep
%setup -q -c -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/kurso,%{_libdir},%{_sysconfdir}}

mkdir inst
cd inst

tar -zxf ../kurso-inst.tar.gz

cp bin/kurso3 $RPM_BUILD_ROOT%{_bindir}
cp lib/libborqt-6.9-qt2.3.so $RPM_BUILD_ROOT%{_libdir}

rm -rf bin lib
cp -r * $RPM_BUILD_ROOT%{_datadir}/kurso

cd ..

cat > $RPM_BUILD_ROOT%{_sysconfdir}/kurso.conf << EOF
path=%{_datadir}/kurso
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kurso3
%attr(755,root,root) %{_libdir}/*
%{_datadir}/kurso
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/kurso.conf
