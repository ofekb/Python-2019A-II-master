```bash
# cd = change directory
C:\Users\Student\Desktop>cd
C:\Users\Student\Desktop

C:\Users\Student\Desktop>cd ..

C:\Users\Student>cd
C:\Users\Student

C:\Users\Student>cd ../..

C:\>cd
C:\

C:\>cd C:\Users\Student\Desktop


# dir = show current directory content
C:\Users\Student\Desktop>dir
 Volume in drive C is System
 Volume Serial Number is 1680-9B6F

 Directory of C:\Users\Student\Desktop

10/31/2018  03:28 PM    <DIR>          .
10/31/2018  03:28 PM    <DIR>          ..
12/06/2017  03:01 PM             1,112 Adobe Lightroom.lnk
11/29/2016  02:55 PM             1,159 Android Studio.lnk
12/27/2016  11:28 AM             2,775 Arena.lnk
10/31/2018  03:16 PM    <DIR>          Day 02 - 31.10.2018
12/06/2017  02:57 PM             1,115 Dream weaver.lnk
09/08/2016  11:45 PM             1,022 Eclipse.lnk
10/31/2018  03:28 PM    <DIR>          hello
10/31/2018  01:21 PM               226 HTMLPage1.html
12/06/2017  03:00 PM             2,526 Illustrator.lnk
12/06/2017  02:59 PM             1,079 InDesign.lnk
10/31/2018  01:17 PM                 0 index.html.txt
02/07/2018  07:37 PM               889 Notepad++.lnk
02/07/2018  07:45 PM               942 Padre, the Perl IDE.lnk
12/06/2017  03:02 PM             1,091 Photoshop.lnk
12/06/2017  03:03 PM             1,157 Premiere Pro.lnk
09/13/2016  01:24 PM             1,889 Quartus Prime.lnk
11/23/2016  01:21 PM             2,357 Statistics.lnk
10/31/2018  02:05 PM    <DIR>          Test
09/11/2016  10:28 AM             1,507 Visual Studio.lnk
07/31/2018  02:46 PM             3,177 VMD.lnk
              17 File(s)         24,023 bytes
               5 Dir(s)  156,065,185,792 bytes free


# mkdir = make directory
C:\Users\Student\Desktop>mkdir test1

C:\Users\Student\Desktop>dir
 Volume in drive C is System
 Volume Serial Number is 1680-9B6F

 Directory of C:\Users\Student\Desktop

10/31/2018  03:31 PM    <DIR>          .
10/31/2018  03:31 PM    <DIR>          ..
12/06/2017  03:01 PM             1,112 Adobe Lightroom.lnk
11/29/2016  02:55 PM             1,159 Android Studio.lnk
12/27/2016  11:28 AM             2,775 Arena.lnk
10/31/2018  03:16 PM    <DIR>          Day 02 - 31.10.2018
12/06/2017  02:57 PM             1,115 Dream weaver.lnk
09/08/2016  11:45 PM             1,022 Eclipse.lnk
10/31/2018  03:28 PM    <DIR>          hello
10/31/2018  01:21 PM               226 HTMLPage1.html
12/06/2017  03:00 PM             2,526 Illustrator.lnk
12/06/2017  02:59 PM             1,079 InDesign.lnk
10/31/2018  01:17 PM                 0 index.html.txt
02/07/2018  07:37 PM               889 Notepad++.lnk
02/07/2018  07:45 PM               942 Padre, the Perl IDE.lnk
12/06/2017  03:02 PM             1,091 Photoshop.lnk
12/06/2017  03:03 PM             1,157 Premiere Pro.lnk
09/13/2016  01:24 PM             1,889 Quartus Prime.lnk
11/23/2016  01:21 PM             2,357 Statistics.lnk
10/31/2018  02:05 PM    <DIR>          Test
10/31/2018  03:31 PM    <DIR>          test1
09/11/2016  10:28 AM             1,507 Visual Studio.lnk
07/31/2018  02:46 PM             3,177 VMD.lnk
              17 File(s)         24,023 bytes
               6 Dir(s)  156,065,185,792 bytes free

# echo = print to the console
C:\Users\Student\Desktop>echo hello
hello

C:\Users\Student\Desktop>echo cd
cd

# %cd% - uses the `cd` as a command, and not as a string
C:\Users\Student\Desktop>echo you are now in this path: %cd%
you are now in this path: C:\Users\Student\Desktop
```
