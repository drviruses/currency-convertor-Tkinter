# currency-convertor-Tkinter
Currency convertor using Tkinter Python

Prerequisite:
          Tkinter in your sysytem
          Sql lite in your system
          ttkthemes library
          
          for tkinter run this on command line : https://tkdocs.com/tutorial/install.html refer this link for installation
          for sql lite : 
                  Install SQLite on Windows
                  Step 1 − Go to https://www.sqlite.org/download.html, and download precompiled binaries from Windows section.

                  Step 2 − Download sqlite-shell-win32-*.zip and sqlite-dll-win32-*.zip zipped files.

                  Step 3 − Create a folder C:\>sqlite and unzip above two zipped files in this folder, which will give you sqlite3.def, sqlite3.dll and sqlite3.exe files.

                  Step 4 − Add C:\>sqlite in your PATH environment variable and finally go to the command prompt and issue sqlite3 command, which should display the following result.

                  C:\>sqlite3
                  SQLite version 3.7.15.2 2013-01-09 11:53:05
                  Enter ".help" for instructions
                  Enter SQL statements terminated with a ";"
                  sqlite>
                  
                  
                  
                  Install SQLite on Linux
                  Today, almost all the flavours of Linux OS are being shipped with SQLite. So you just issue the following command to check if you already have SQLite installed on your machine.

                  $sqlite3
                  SQLite version 3.7.15.2 2013-01-09 11:53:05
                  Enter ".help" for instructions
                  Enter SQL statements terminated with a ";"
                  sqlite>
                  If you do not see the above result, then it means you do not have SQLite installed on your Linux machine. Following are the following steps to install SQLite −

                  Step 1 − Go to SQLite download page https://www.sqlite.org/download.html and download sqlite-autoconf-*.tar.gz from source code section.

                  Step 2 − Run the following command −

                  $tar xvfz sqlite-autoconf-3071502.tar.gz
                  $cd sqlite-autoconf-3071502
                  $./configure --prefix=/usr/local
                  $make
                  $make install
                  The above command will end with SQLite installation on your Linux machine. Which you can verify as explained above.



                  Install SQLite on Mac OS X
                  Though the latest version of Mac OS X comes pre-installed with SQLite but if you do not have installation available then just follow these following steps −

                  Step 1 − Go to SQLite download page, and download sqlite-autoconf-*.tar.gz from source code section.

                  Step 2 − Run the following command −

                  $tar xvfz sqlite-autoconf-3071502.tar.gz
                  $cd sqlite-autoconf-3071502
                  $./configure --prefix=/usr/local
                  $make
                  $make install
                  The above procedure will end with SQLite installation on your Mac OS X machine. Which you can verify by issuing the following command −

                  $sqlite3
                  SQLite version 3.7.15.2 2013-01-09 11:53:05
                  Enter ".help" for instructions
                  Enter SQL statements terminated with a ";"
                  sqlite>
                                                
