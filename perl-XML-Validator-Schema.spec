%define modname	XML-Validator-Schema
%define modver	1.10

Summary:	Validate XML with a subset of W3C XML Schema
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	19
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/XML/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Tree::DAG_Node)
BuildRequires:	perl(XML::Filter::BufferText)
BuildRequires:	perl(XML::SAX)

%description
This module allows you to validate XML documents against a W3C XML Schema.
This module does not implement the full W3C XML Schema recommendation
(http://www.w3.org/XML/Schema), but a useful subset. See the "SCHEMA
SUPPORT" section below.

*IMPORTANT NOTE*:	To get line and column numbers in the error messages
generated by this module you must install XML::Filter::ExceptionLocator and
use XML::SAX::ExpatXS as your SAX parser. This module is much more useful
if you can tell where your errors are, so using these modules is highly
recommeded!

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

