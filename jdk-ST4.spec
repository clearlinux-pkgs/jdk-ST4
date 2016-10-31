Name     : jdk-ST4
Version  : 4.0.8
Release  : 6
URL      : https://repo1.maven.org/maven2/org/antlr/ST4/4.0.8/ST4-4.0.8.jar
Source0  : https://repo1.maven.org/maven2/org/antlr/ST4/4.0.8/ST4-4.0.8.jar
Source1  : https://repo1.maven.org/maven2/org/antlr/ST4/4.0.8/ST4-4.0.8.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: jdk-ST4-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-ST4 package.
Group: Data

%description data
data components for the jdk-ST4 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/ST4.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/ST4.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/ST4.xml \
%{buildroot}/usr/share/maven-poms/ST4.pom \
%{buildroot}/usr/share/java/ST4.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/ST4.jar
/usr/share/maven-metadata/ST4.xml
/usr/share/maven-poms/ST4.pom
