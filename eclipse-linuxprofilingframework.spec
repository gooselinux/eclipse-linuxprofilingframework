%define src_repo_tag   R0_5_0
%define eclipse_base   %{_libdir}/eclipse
%define install_loc    %{_libdir}/eclipse/dropins/linuxprofilingframework
%define qualifier      201003171651

# Package in %%{_libdir} but no native code so no debuginfo
%global debug_package %{nil}

Name:           eclipse-linuxprofilingframework
Version:        0.3.0
Release:        5%{?dist}
Summary:        Eclipse Linux Tools Profiling Framework

Group:          Development/Tools
License:        EPL
URL:            http://eclipse.org/linuxtools
# sh -x ./eclipse-linuxprofilingframework-fetch-src.sh %{src_repo_tag}
Source0:        %{name}-fetched-src-%{src_repo_tag}.tar.bz2
Source1:        %{name}-fetch-src.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Only x86 and x86_64 for RHEL
ExclusiveArch: %{ix86} x86_64

BuildRequires: eclipse-pde >= 1:3.5.0
Requires: eclipse-platform >= 1:3.5.0
BuildRequires: eclipse-cdt >= 1:6.0.0
Requires: eclipse-cdt >= 1:6.0.0

%description
Plugins common to Eclipse Linux Tools profiling tools.

%prep
%setup -q -n %{name}-fetched-src-%{src_repo_tag}

%build
%{eclipse_base}/buildscripts/pdebuild -d cdt -f org.eclipse.linuxtools.profiling \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \

%install
rm -rf %{buildroot}
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}

unzip -q -d $RPM_BUILD_ROOT%{install_loc} \
     build/rpmBuild/org.eclipse.linuxtools.profiling.zip

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc org.eclipse.linuxtools.profiling-feature/epl-v10.html
%{install_loc}

%changelog
* Fri Mar 19 2010 Jeff Johnston <jjohnstn@redhat.com> 0.3.0-5
- Resolves: #575104
- Rebase to Linux tools 0.5.0 version.

* Wed Dec 16 2009 Alexander Kurtakov <akurtako@redhat.com> 0.3.0-4
- Correct x86 arch.

* Wed Dec 16 2009 Alexander Kurtakov <akurtako@redhat.com> 0.3.0-3
- Build only on x86/x86_64.

* Thu Aug 20 2009 Elliott Baron <ebaron@fedoraproject.org> 0.3.0-2
- Remove ".feature" from feature ID passed to pdebuild.

* Thu Aug 20 2009 Elliott Baron <ebaron@fedoraproject.org> 0.3.0-1
- Upstream 0.3.0 release.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 15 2009 Elliott Baron <ebaron@redhat.com> 0.2.0-2
- Fixing tag.

* Wed May 13 2009 Elliott Baron <ebaron@redhat.com> 0.2.0-1
- Upstream 0.2.0 release.

* Wed Apr 8 2009 Andrew Overholt <overholt@redhat.com> 0.1.0-4
- Don't generate debuginfo (rhbz#494719).

* Mon Mar 23 2009 Elliott Baron <ebaron@redhat.com> 0.1.0-3
- Rebuild for changes in pdebuild to not ship p2 metadata.

* Fri Mar 6 2009 Elliott Baron <ebaron@redhat.com> 0.1.0-2
- Changing to arch dependent for CDT dependency.
- CDT should be >= 5.0.0

* Thu Mar 5 2009 Elliott Baron <ebaron@redhat.com> 0.1.0-1
- Final 0.1 upstream release.
- Removed "Valgrind" from dialog titles.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 28 2009 Andrew Overholt <overholt@redhat.com> 0.1.0-0.2
- No CDT on ppc64 -> ExcludeArch.

* Tue Jan 13 2009 Andrew Overholt <overholt@redhat.com> 0.1.0-0.1
- Initial release.  Pre-0.1.0 upstream.
