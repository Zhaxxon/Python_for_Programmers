from ftplib import FTP

ftp = FTP('ftp.debian.org')
print(ftp.login())
#'230 Login successful.'

print(ftp.cwd('debian')  )
#'250 Directory successfully changed.'


out = 'README'
with open(out, 'wb') as f:
    ftp.retrbinary('RETR ' + 'README.html', f.write)


import ftplib
import os

ftp = ftplib.FTP('ftp.debian.org')
ftp.login()
ftp.cwd('debian')
filenames = ftp.nlst()

for filename in filenames:
    host_file = os.path.join(
        'ftp_test', filename)
    try:
        with open(host_file, 'wb') as local_file:
            ftp.retrbinary('RETR ' + filename, local_file.write)
    except ftplib.error_perm:
        pass

ftp.quit()