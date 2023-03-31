Name:		texlive-tikz-bayesnet
Version:	38295
Release:	2
Summary:	Draw Bayesian networks, graphical models and directed factor graphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-bayesnet
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-bayesnet.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-bayesnet.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The package provides a library supporting the display of
Bayesian networks, graphical models and (directed) factor
graphs in LaTeX.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/tikz-bayesnet

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
