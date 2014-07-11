# revision 32970
# category Package
# catalog-ctan /macros/latex/contrib/sidenotes
# catalog-date 2014-02-14 10:39:07 +0100
# catalog-license lppl1.3
# catalog-version 0.96a
Name:		texlive-sidenotes
Epoch:		1
Version:	0.96a
Release:	3
Summary:	Typeset notes containing rich content, in the margin
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sidenotes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sidenotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sidenotes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sidenotes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows typesetting of texts with notes, figures,
citations, captions and tables in the margin. This is common
(for example) in science text books.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sidenotes/caesar_book.cls
%{_texmfdistdir}/tex/latex/sidenotes/sidenotes.sty
%doc %{_texmfdistdir}/doc/latex/sidenotes/README
%doc %{_texmfdistdir}/doc/latex/sidenotes/caesar_example.pdf
%doc %{_texmfdistdir}/doc/latex/sidenotes/caesar_example.tex
%doc %{_texmfdistdir}/doc/latex/sidenotes/sidenotes.pdf
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
