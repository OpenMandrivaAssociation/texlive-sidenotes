# revision 26610
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-sidenotes
Version:	20120808
Release:	1
Summary:	TeXLive sidenotes package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sidenotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sidenotes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sidenotes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive sidenotes package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sidenotes/sidenotes.sty
%doc %{_texmfdistdir}/doc/latex/sidenotes/README
%doc %{_texmfdistdir}/doc/latex/sidenotes/sidenotes.pdf
%doc %{_texmfdistdir}/doc/latex/sidenotes/sn.bib
%doc %{_texmfdistdir}/doc/latex/sidenotes/sn_usage_biblatex.pdf
%doc %{_texmfdistdir}/doc/latex/sidenotes/sn_usage_biblatex.tex
%doc %{_texmfdistdir}/doc/latex/sidenotes/sn_usage_bibtex.pdf
%doc %{_texmfdistdir}/doc/latex/sidenotes/sn_usage_bibtex.tex
#- source
%doc %{_texmfdistdir}/source/latex/sidenotes/sidenotes.dtx
%doc %{_texmfdistdir}/source/latex/sidenotes/sidenotes.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
