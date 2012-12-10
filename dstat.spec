Summary: Versatile vmstat, iostat and ifstat replacement
Name: dstat
Version: 0.7.2
Release: 1
License: GPL
Group: System/Kernel and hardware
URL: http://dag.wieers.com/home-made/dstat/
Source: http://dag.wieers.com/home-made/dstat/dstat-%{version}.tar.bz2
BuildArch: noarch

%description
Dstat is a versatile replacement for vmstat, iostat and ifstat. Dstat
overcomes some of the limitations and adds some extra features.

Dstat allows you to view all of your system resources instantly,
you can eg. compare disk usage in combination with interrupts from
your IDE controller, or compare the network bandwidth numbers
directly with the disk throughput (in the same interval).

Dstat also cleverly gives you the most detailed information in
columns and clearly indicates in what magnitude and unit the output
is displayed. Less confusion, less mistakes.

Dstat is also unique in letting you aggregate block device throughput
for a certain diskset or network bandwidth for a group of interfaces,
ie. you can see the throughput for all the block devices that make up
a single filesystem or storage system.

You can customize your dstat output from /etc/dstat.conf and you can
write your own dstat modules to plug into the dstat output.

Dstat's output, in its current form, is not very useful to be post-
processed by other tools. It's mostly meant for allowing humans to
interprete real-time data as easy as possible.

%prep
%setup -q

%install
%makeinstall

mkdir -p %buildroot%_mandir/man1
install -m 644 docs/dstat.1 %buildroot%_mandir/man1/dstat.1

%files
%doc AUTHORS ChangeLog COPYING README TODO 
%{_bindir}/dstat
%_datadir/%name
%doc %{_mandir}/man1/dstat.1*


%changelog
* Sat Dec 24 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.7.2-1
+ Revision: 745103
- version update 0.7.2

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-2mdv2011.0
+ Revision: 610288
- rebuild

* Mon Feb 22 2010 Frederik Himpe <fhimpe@mandriva.org> 0.7.1-1mdv2010.1
+ Revision: 509624
- update to new version 0.7.1

* Sat Dec 26 2009 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-1mdv2010.1
+ Revision: 482481
- 0.7.0 (fixes CVE-2009-3894,4081)

* Sun Jan 04 2009 Olivier Thauvin <nanardon@mandriva.org> 0.6.9-1mdv2009.1
+ Revision: 324540
- 0.6.9

* Fri Sep 12 2008 Olivier Thauvin <nanardon@mandriva.org> 0.6.8-1mdv2009.0
+ Revision: 284101
- 0.6.8

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.6.7-3mdv2009.0
+ Revision: 244553
- rebuild

* Tue Feb 26 2008 Erwan Velu <erwan@mandriva.org> 0.6.7-1mdv2008.1
+ Revision: 175415
- 0.6.7
- 0.6.7

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Apr 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.6-1mdv2008.0
+ Revision: 18963
- new version

* Fri Apr 20 2007 Olivier Thauvin <nanardon@mandriva.org> 0.6.5-1mdv2008.0
+ Revision: 15940
- 0.6.5

