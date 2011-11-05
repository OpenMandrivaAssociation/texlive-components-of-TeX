# revision 15878
# category Package
# catalog-ctan /info/components-of-TeX
# catalog-date 2009-01-09 17:16:29 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-components-of-TeX
Version:	20090109
Release:	1
Summary:	Components of TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/components-of-TeX
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/components-of-TeX.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/components-of-TeX.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
An introduction to the components and files users of TeX may
encounter.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/components-of-TeX/README
%doc %{_texmfdistdir}/doc/generic/components-of-TeX/etexkomp.tex
%doc %{_texmfdistdir}/doc/generic/components-of-TeX/figkomp.tex
%doc %{_texmfdistdir}/doc/generic/components-of-TeX/figtotal.tex
%doc %{_texmfdistdir}/doc/generic/components-of-TeX/names.sty
%doc %{_texmfdistdir}/doc/generic/components-of-TeX/texrep.sty
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
