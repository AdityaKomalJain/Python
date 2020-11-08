import io
import datetime as dt
import re
import os
import shutil
import sys

bkp_ext = 'av-imp' # choose a backup extension of your choice
rename_delimit = '_bkp_ts_' # choose a backup time stamp extension of your choice
dst = "D:\Backup//" # your back up directory with path

def back_it_up():
    # List out your directories you want the script to look into for the files to be backed-up
    for all_items in []:
        counter = 0    # counter for counting number of files backed up in a directory
        try:
            for root,folder,files in os.walk(all_items,topdown=True):
                for f in files:
                    if os.path.splitext(f)[0].split('_')[-1] == bkp_ext:    # splitting the file name to find out if out back up extension is present there or not
                        fname = os.path.splitext(f)[0].replace('_'+bkp_ext,'') # set file name
                        ext = os.path.splitext(f)[1]                           # set extension
                        c_time_stamp = dt.datetime.now().strftime("%Y-%m-%d%H-%M-%S") #set time stamp
                        dstf = fname+rename_delimit+ c_time_stamp + ext #set destination path with file name
                        shutil.copy(root+f,'D://Backup//'+dstf) # copy file to backup
                        os.rename(root+f,root+fname+ext) # rename backed up file to remove the bkp_ext
                        with open('D://Backup//bkp_logs.txt','a') as write_logs:   # write logs _ create the file first
                            write_logs.writelines('\nFile_Name - {}, TimeStamp - {}'.format(root+fname+ext,c_time_stamp))
                        counter = counter + 1
        except (NameError, FileNotFoundError, IOError, RuntimeError, ValueError, OSError) as r: #exception handling
            with open('D://Backup//bkp_failur_logs.txt','a') as write_logs: # write failure logs _ create the file first
                write_logs.writelines('\nException - {}, TimeStamp - {}'.format(r,dt.datetime.now().strftime("%Y-%m-%d%H-%M-%S")))
        finally:
            print("\n Execution Complete for {} \n Files Found : {}".format(all_items,counter))

back_it_up()
