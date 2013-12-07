# revision 30094
# category Package
# catalog-ctan /graphics/pgf/contrib/tikz-bayesnet
# catalog-date 2013-04-24 11:34:47 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-tikz-bayesnet
Version:	0.1
Release:	4
Summary:	Draw Bayesian networks, graphical models and directed factor graphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-bayesnet
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-bayesnet.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-bayesnet.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The package provides a library supporting the display of
Bayesian networks, graphical models and (directed) factor
graphs in LaTeX.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/tikz-bayesnet/LICENSE_GPL
%doc %{_texmfdistdir}/doc/latex/tikz-bayesnet/LICENSE_LPPL
%doc %{_texmfdistdir}/doc/latex/tikz-bayesnet/README.rst
%doc %{_texmfdistdir}/doc/latex/tikz-bayesnet/example.tex
%doc %{_texmfdistdir}/doc/latex/tikz-bayesnet/model_citation_influence.tex
%doc %{_texmfdistdir}/doc/latex/tikz-bayesnet/model_lda.tex
%doc %{_texmfdistdir}/doc/latex/tikz-bayesnet/model_pca.tex
%doc %{_texmfdistdir}/doc/latex/tikz-bayesnet/model_pca2.tex
%doc %{_texmfdistdir}/doc/latex/tikz-bayesnet/tikzlibrarybayesnet.code.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
