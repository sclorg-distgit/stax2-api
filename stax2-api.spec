%global pkg_name stax2-api
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:             %{?scl_prefix}%{pkg_name}
Version:          3.1.1
Release:          10.9%{?dist}
Summary:          Experimental API extending basic StAX implementation
License:          BSD
URL:              http://docs.codehaus.org/display/WSTX/StAX2
BuildArch:        noarch

Source0:          http://repository.codehaus.org/org/codehaus/woodstox/%{pkg_name}/%{version}/%{pkg_name}-%{version}-sources.jar
Source1:          http://repository.codehaus.org/org/codehaus/woodstox/%{pkg_name}/%{version}/%{pkg_name}-%{version}.pom

BuildRequires:    %{?scl_prefix_java_common}maven-local
BuildRequires:    %{?scl_prefix_java_common}bea-stax-api

%description
StAX2 is an experimental API that is intended to extend
basic StAX specifications in a way that allows implementations
to experiment with features before they end up in the actual
StAX specification (if they do). As such, it is intended
to be freely implementable by all StAX implementations same way
as StAX, but without going through a formal JCP process.


%package javadoc
Summary:          API documentation for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -c -n %{pkg_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
# fixing incomplete source directory structure
mkdir -p src/main/java
mv -f org src/main/java/
cp %{SOURCE1} pom.xml
%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 3.1.1-10.9
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 3.1.1-10.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 3.1.1-10.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-10.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-10.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-10.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-10.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-10.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-10.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.1.1-10
- Mass rebuild 2013-12-27

* Tue Aug 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-9
- Migrate away from mvn-rpmbuild

* Wed Jul 31 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.1.1-8
- Rebuild for new sources

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.1.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 29 2011 Jaromir Capik <jcapik@redhat.com> - 3.1.1-2
- bea-stax has it's own depmap now -> removing the local one

* Tue Sep 13 2011 Jaromir Capik <jcapik@redhat.com> - 3.1.1-1
- Initial version
