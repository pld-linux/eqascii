Summary:	EQuation ASCII renderer
Summary(pl):	Program wy¶wietlaj±cy równania jako ASCII
Name:		eqascii
Version:	0.3.1
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	http://dione.ids.pl/~pborys/software/linux/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eqascii is an ascii equation renderer, which as a command argument
accepts an equation in a form similar to LaTeX equation description.
It outputs the result to stdout.

%description -l pl
eqascii jest programem wy¶wietlaj±cym równania przy u¿yciu znaków
ASCII, przyjmuj±cym równania w notacji podobnej do LaTeXa.

%prep
%setup -q -n %{name}

%build
%{__make} DEBUG="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install eqascii $RPM_BUILD_ROOT%{_bindir}
install eqascii.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf HISTORY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz test
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
