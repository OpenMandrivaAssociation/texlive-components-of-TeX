# revision 15878
# category Package
# catalog-ctan /info/components-of-TeX
# catalog-date 2009-01-09 17:16:29 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-components-of-TeX
Version:	20090109
Release:	9
Summary:	Components of TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/components-of-TeX
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/components-of-TeX.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/components-of-TeX.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090109-2
+ Revision: 750414
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090109-1
+ Revision: 718112
- texlive-components-of-TeX
- texlive-components-of-TeX
- texlive-components-of-TeX
- texlive-components-of-TeX

