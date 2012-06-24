Summary:	EQuation ASCII renderer
Summary(pl):	Program wy�wietlaj�cy r�wnania jako ASCII
Name:		eqascii
Version:	0.3.1
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://dione.ids.pl/~pborys/software/linux/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eqascii is an ascii equation renderer, which as a command argument
accepts an equation in a form similar to LaTeX equation description.
It outputs the result to stdout.

%description -l pl
eqascii jest programem wy�wietlaj�cym r�wnania przy u�yciu znak�w
ASCII, przyjmuj�cym r�wnania w notacji podobnej do LaTeXa.

%package devel
Summary:	EQuation ASCII renderer for programmers
Summary(pl):	Biblioteka do zamiany r�wna� na posta� ASCII
Group:		Development/Libraries
# note:	there is no reason to require eqascii

%description devel
Package contains static library, header file and documentation useful
for developing programs that draw equations in text mode.

%description devel -l pl
Pakiet zawiera bibliotek� statyczn�, plik nag��wkowy i dokumentacj�
przydatne przy pisaniu program�w wy�wietlaj�cych wzory jako ASCII.

%prep
%setup -q -n %{name}

%build
%{__make} DEBUG="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir},%{_mandir}/man{1,3}}

install eqascii $RPM_BUILD_ROOT%{_bindir}
install eqascii.1 $RPM_BUILD_ROOT%{_mandir}/man1
install eqascii.3 $RPM_BUILD_ROOT%{_mandir}/man3
install eqascii.a $RPM_BUILD_ROOT%{_libdir}
install eqascii.h $RPM_BUILD_ROOT%{_includedir}

gzip -9nf HISTORY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz test
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/*.h
%{_mandir}/man3/*
