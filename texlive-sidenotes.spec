# revision 24275
# category Package
# catalog-ctan /macros/latex/contrib/sidenotes
# catalog-date 2011-10-12 17:03:26 +0200
# catalog-license lppl1.3
# catalog-version 0.53
Name:		texlive-sidenotes
Version:	0.53
Release:	1
Summary:	Typeset notes containing rich content, in the margin
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sidenotes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sidenotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sidenotes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sidenotes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package allows typesetting of texts with notes, figures,
citations, captions and tables in the margin. This is common
(for example) in science text books.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sidenotes/sidenotes.sty
%doc %{_texmfdistdir}/doc/latex/sidenotes/README
%doc %{_texmfdistdir}/doc/latex/sidenotes/sidenotes.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sidenotes/sidenotes.dtx
%doc %{_texmfdistdir}/source/latex/sidenotes/sidenotes.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
