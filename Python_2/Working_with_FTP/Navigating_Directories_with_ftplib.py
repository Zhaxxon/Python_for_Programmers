from ftplib import FTP
ftp = FTP()
ftp.login()
ftp.retrlines('LIST')
#total 28
#drwxrwxrwx   2 0       0     4096 Sep  6  2015 .snapshot
#drwxr-xr-x   2 202019  5564  4096 Sep  6  2015 CSE421
#drwxr-xr-x   2 0       0     4096 Jul 23  2008 bin
#drwxr-xr-x   2 0       0     4096 Mar 15  2007 etc
#drwxr-xr-x   6 89987   546   4096 Sep  6  2015 mirror
#drwxrwxr-x   7 6980    546   4096 Jul  3  2014 pub
#drwxr-xr-x  26 0       11    4096 Apr 29 20:31 users
#'226 Transfer complete.'

ftp.cwd('mirror')
#'250 CWD command successful.'

ftp.retrlines('LIST')
#total 16
#drwxr-xr-x  3 89987  546  4096 Sep  6  2015 BSD
#drwxr-xr-x  5 89987  546  4096 Sep  6  2015 Linux
#drwxr-xr-x  4 89987  546  4096 Sep  6  2015 Network
#drwxr-xr-x  4 89987  546  4096 Sep  6  2015 X11
#'226 Transfer complete.'