# Test result
We asked sandboxllm 61 questions and the results are as follows:
- Total: 61
- Passed: 58
- Pass rate: 95.08%

The following is a detailed list of questions:
| Corpus Filename                                  | Question                                                     | Answer                                                       | Expected answer                                                       | Passed? |
| ----------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ----- |
| 1c4989acfd741d3d1612b3495e087a2c.json.txt | Does this sample hit the Yara rule? Please answer no or yes. | Yes.                                                         | TRUE                                                         | yes   |
| 1c4989acfd741d3d1612b3495e087a2c.json.txt | Does this sample hit the IDS traffic rule? Please answer no or yes. | No                                                           | FALSE                                                        | yes   |
| 1c4989acfd741d3d1612b3495e087a2c.json.txt | Does this sample have high-risk behaviors? Please answer no or yes. | Yes.                                                         | TRUE                                                         | yes   |
| 1c4989acfd741d3d1612b3495e087a2c.json.txt | Does this sample dropped files? Please answer no or yes.     | This question鏃犳硶浠庢姤鍛婁腑鎵惧埌銆?,False"              | yes                                                          |       |
| 1c4989acfd741d3d1612b3495e087a2c.json.txt | What is the md5 of this sample?                              | The md5 of this sample is 1c4989acfd741d3d1612b3495e087a2c.  | ['1c4989acfd741d3d1612b3495e087a2c']                         | yes   |
| 1c4989acfd741d3d1612b3495e087a2c.json.txt | How long does it take to analyze this sample?                | It takes 124 seconds to analyze this sample.                 | ['124']                                                      | yes   |
| 1c4989acfd741d3d1612b3495e087a2c.json.txt | Which Yara rules does this sample hit?                       | This sample hits the following YARA rules:\n-  "embedded_win_api", which matches due to the presence of win32 API  function names like "U2hlbGxFeGVjdXRl".\n- "powershell",  which matches without a specific description provided. The hit content  includes base64-encoded strings 'UG93ZXJTaGVsbA==' and 'cG93ZXJzaGVsbA==',  which are likely decodings of "PowerShell" in different  capitalization formats. | ['embedded_win_api', 'powershell']                           | yes   |
| 1c4989acfd741d3d1612b3495e087a2c.json.txt | What are the high-risk behaviors of this sample?             | The high-risk behavior of this sample is  "martian_command_process", which means a command shell or script  process was created by an unexpected parent process. | ['martian_command_process']                                  | yes   |
| 1c4989acfd741d3d1612b3495e087a2c.json.txt | What are the suspicious behaviors of this sample?            | The suspicious behaviors of this sample include creating guard pages,  creating a hidden window, using a very long command line, and a command shell  or script process being created by an unexpected parent process. | ['guard page', 'hidden window', 'long command line']         | yes   |
| 2be5b0bcd650b276dd197f02f194876d.json.txt | Does this sample hit the Yara rule? Please answer no or yes. | Yes.                                                         | TRUE                                                         | yes   |
| 2be5b0bcd650b276dd197f02f194876d.json.txt | Does this sample hit the IDS traffic rule? Please answer no or yes. | No                                                           | FALSE                                                        | yes   |
| 2be5b0bcd650b276dd197f02f194876d.json.txt | Does this sample have high-risk behaviors? Please answer no or yes. | No                                                           | FALSE                                                        | yes   |
| 2be5b0bcd650b276dd197f02f194876d.json.txt | Does this sample dropped files? Please answer no or yes.     | yes                                                          | TRUE                                                         | yes   |
| 2be5b0bcd650b276dd197f02f194876d.json.txt | What is the md5 of this sample?                              | The md5 of this sample is 2be5b0bcd650b276dd197f02f194876d.  | ['2be5b0bcd650b276dd197f02f194876d']                         | yes   |
| 2be5b0bcd650b276dd197f02f194876d.json.txt | How long does it take to analyze this sample?                | It takes 82 seconds to analyze this sample.                  | ['82']                                                       | yes   |
| 2be5b0bcd650b276dd197f02f194876d.json.txt | Which Yara rules does this sample hit?                       | The sample hits the following YARA rule: "powershell".       | ['powershell']                                               | yes   |
| 2be5b0bcd650b276dd197f02f194876d.json.txt | What are the high-risk behaviors of this sample?             | The sample does not exhibit any high-risk behaviors. The reported  behaviors are either normal or suspicious: create_file_intemp (normal),  create_log_file (normal), and create_guard_page (suspicious). | ['does not']                                                 | yes   |
| 2be5b0bcd650b276dd197f02f194876d.json.txt | What are the suspicious behaviors of this sample?            | The suspicious behavior of this sample includes creating guard pages,  which is often used to hinder reverse engineering and debugging. | ['guard page']                                               | yes   |
| 2be5b0bcd650b276dd197f02f194876d.json.txt | What files does this sample drop?                            | This sample drops a file named 049802f3d3a6803f_setdefaultwallpaper.log,  located in C:\Windows\Temp\SetDefaultWallpaper.log, with a size of 201 bytes  and MD5 hash 053a5156c13ad0a20a7aa42ca42dd16a. The file type is identified as  "ASCII text, with CRLF line terminators". | ['049802f3d3a6803f']                                         | yes   |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | Does this sample hit the Yara rule? Please answer no or yes. | Yes.                                                         | TRUE                                                         | yes   |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | Does this sample hit the IDS traffic rule? Please answer no or yes. | No                                                           | FALSE                                                        | yes   |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | Does this sample have high-risk behaviors? Please answer no or yes. | Yes                                                          | TRUE                                                         | yes   |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | Does this sample dropped files? Please answer no or yes.     | yes                                                          | TRUE                                                         | yes   |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | Does this sample have network behavior? Please answer no or yes. | Yes.                                                         | TRUE                                                         | yes   |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | What is the md5 of this sample?                              | The md5 of this sample is 24c94559b2c3b1a22b0b8a4b6447df2d.  | ['24c94559b2c3b1a22b0b8a4b6447df2d']                         | yes   |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | How long does it take to analyze this sample?                | It takes 119 seconds to analyze this sample.                 | ['119']                                                      | yes   |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | Which Yara rules does this sample hit?                       | The sample hits the following YARA rules:\n- The sample hits yara rule  "powershell", description is "(no description)", and the  hit content is ['UG93ZXJzaGVsbA=='] | ['powershell']                                               | yes   |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | What are the high-risk behaviors of this sample?             | The high-risk behaviors of this sample include: dropper, which indicates  the sample drops a binary and executes it; martian_command_process, which  means a command shell or script process was created by an unexpected parent  process; and persistence_autorun_task, indicating the sample scheduled a  start by creating scheduled tasks. | ['a binary', 'command shell', 'scheduled task']              | yes   |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | What files does this sample drop?                            | The sample drops the following files: ddf3085658167a79_hotline.vbs,  e72b788676bbe447_ubisoft64.vbs, 34944b82a449df4f_report.ps1, and  1ef07109704d9ab0_ubisoft64.ps1. | ['ddf3085658167a79', 'e72b788676bbe447', '34944b82a449df4f',  '1ef07109704d9ab0'] | yes   |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | What is the most common extension for the files dropped by this sample? | .vbs                                                         | ['ps1']                                                      | no    |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | Which IP addresses was visited by this sample?               | 45.154.98.194                                                | ['45.154.98.194']                                            | yes   |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | Which domain names are queried in this sample?               | The domain name queried in this sample is services.work.gd.  | ['services.work.gd']                                         | yes   |
| 24c94559b2c3b1a22b0b8a4b6447df2d.json.txt | What are the query results of services.work.gd?              | The query result of services.work.gd is 45.154.98.194.       | ['45.154.98.194']                                            | yes   |
| 699489a273ecf23f09fea4babde36521.json.txt | Does this sample hit the Yara rule? Please answer no or yes. | This question鏃犳硶浠庢姤鍛婁腑鎵惧埌銆?,False"              | yes                                                          |       |
| 699489a273ecf23f09fea4babde36521.json.txt | Does this sample hit the IDS traffic rule? Please answer no or yes. | No                                                           | FALSE                                                        | yes   |
| 699489a273ecf23f09fea4babde36521.json.txt | Does this sample have high-risk behaviors? Please answer no or yes. | Yes.                                                         | TRUE                                                         | yes   |
| 699489a273ecf23f09fea4babde36521.json.txt | Does this sample dropped files? Please answer no or yes.     | yes                                                          | TRUE                                                         | yes   |
| 699489a273ecf23f09fea4babde36521.json.txt | Does this sample have network behavior? Please answer no or yes. | yes                                                          | TRUE                                                         | yes   |
| 699489a273ecf23f09fea4babde36521.json.txt | What is the md5 of this sample?                              | The md5 of this sample is 699489a273ecf23f09fea4babde36521.  | ['699489a273ecf23f09fea4babde36521']                         | yes   |
| 699489a273ecf23f09fea4babde36521.json.txt | How long does it take to analyze this sample?                | The analysis duration is 114 seconds.                        | ['114']                                                      | yes   |
| 699489a273ecf23f09fea4babde36521.json.txt | What are the high-risk behaviors of this sample?             | The high-risk behaviors of this sample include: creates_user_folder_exe,  process_martian, and self_delete_bat. | ['creates_user_folder_exe', 'process_martian', 'self_delete_bat'] | yes   |
| 699489a273ecf23f09fea4babde36521.json.txt | What files does this sample drop?                            | The sample drops the following files:\n-  b240a9bb4f72d886_zilkofux.0.cs\n- c6fc91e5b6d5391b_zilkofux.cmdline\n-  955f70ea652c851f_zilkofux.out\n-  51f663012e3953d5_csc5696f1fe2da649dc9fc5816f5d65b326.tmp\n-  ef8a6ee994950ce3_zilkofux.dll\n- 13b9d99d97449e76_zilkofux.out | ['c6fc91e5b6d5391b', '955f70ea652c851f', '51f663012e3953d5',  'ef8a6ee994950ce3', '13b9d99d97449e76'] | yes   |
| 699489a273ecf23f09fea4babde36521.json.txt | What is this sample self-deleting file?                      | The sample self-deletes the file  C:\Users\Admin\AppData\Local\Temp\zilkofux\zilkofux.cmdline. | ['zilkofux.cmdline']                                         | yes   |
| 699489a273ecf23f09fea4babde36521.json.txt | What is the file created by this sample in the user directory? | The sample creates an executable file named "zilkofux.dll" in  the user directory. The full path of the file is  "c:\Users\Admin\AppData\Local\Temp\zilkofux\zilkofux.dll". | ['zilkofux.dll']                                             | yes   |
| 699489a273ecf23f09fea4babde36521.json.txt | Which IP addresses was visited by this sample?               | The sample visited the IP address 82.61.9.223.               | ['82.61.9.223']                                              | yes   |
| 699489a273ecf23f09fea4babde36521.json.txt | What is the protocol between the sample and 82.61.9.223?     | The protocol between the sample and 82.61.9.223 is tcp.      | ['tcp']                                                      | yes   |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | Does this sample hit the Yara rule? Please answer no or yes. | This question鏃犳硶浠庢姤鍛婁腑鎵惧埌銆?,False"              | yes                                                          |       |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | Does this sample hit the IDS traffic rule? Please answer no or yes. | Yes.                                                         | FALSE                                                        | no    |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | Does this sample have high-risk behaviors? Please answer no or yes. | yes                                                          | TRUE                                                         | yes   |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | Does this sample dropped files? Please answer no or yes.     | yes                                                          | TRUE                                                         | yes   |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | Does this sample have network behavior? Please answer no or yes. | yes                                                          | TRUE                                                         | yes   |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | What is the md5 of this sample?                              | The md5 of this sample is bc38dc28ee84904c66a5655b02c7aea2.  | ['bc38dc28ee84904c66a5655b02c7aea2']                         | yes   |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | How long does it take to analyze this sample?                | The analysis of this sample takes 133 seconds.               | ['133']                                                      | yes   |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | What is the machine name of the virtual machine              | The machine name is win7_office2013.                         | ['win7_office2013']                                          | yes   |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | What are the high-risk behaviors of this sample?             | The high-risk behaviors of this sample include: creating an executable  file in a user folder, creating martian processes, and deleting executed  files from disk. | ['executable file', 'martian processes', 'delete', 'executed files'] | no    |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | What files does this sample drop?                            | This sample drops the following files during analysis:\n-  f2c563322c4d6a4c_gndvu4bb.0.cs\n- 514d1775e96df441_gndvu4bb.cmdline\n-  c6a747c1a08365ed_gndvu4bb.out\n-  0417cd88fd2d8feb_csc4ec2cd084e67483982d285952963989a.tmp\n-  c9c055a1290d6f73_gndvu4bb.dll\n- 939abf80f24d35fe_gndvu4bb.out | ['f2c563322c4d6a4c', '514d1775e96df441', 'c6a747c1a08365ed',  '0417cd88fd2d8feb', 'c9c055a1290d6f73', '939abf80f24d35fe'] | yes   |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | What is this sample self-deleting file?                      | The sample self-deleting file is  C:\Users\Admin\AppData\Local\Temp\gndvu4bb\gndvu4bb.cmdline. | ['gndvu4bb.cmdline']                                         | yes   |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | What is the file created by this sample in the user directory? | The file created by this sample in the user directory is  c:\Users\Admin\AppData\Local\Temp\gndvu4bb\gndvu4bb.dll. | ['gndvu4bb.dll']                                             | yes   |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | Which IP and domain was visited by this sample?              | The sample visited the IP 198.185.159.145 and the domain bemnyc.com. | ['198.185.159.145', 'bemnyc.com']                            | yes   |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | What is the protocol between the sample and bemnyc.com?      | The protocol between the sample and bemnyc.com is HTTP.      | ['http']                                                     | yes   |
| bc38dc28ee84904c66a5655b02c7aea2.json.txt | Which dns query IP of the domain: bemnyc.com did the sample finally  choose to establish a session with? | The sample chose the IP 198.185.159.145 to establish a session with the  domain bemnyc.com. | ['198.185.159.145']                                          | yes   |


# 1. Install cuckoo
1. Create a new user
```
$ sudo adduser cuckoo
```
2. We are using VirtualBox, so run the following shell to make sure the new user belongs to the “vboxusers” group
```
$ sudo usermod -a -G vboxusers cuckoo
```
3. pip install cuckoo in `virtualenv`
```
$ virtualenv venv
$ . venv/bin/activate
(venv)$ pip install -U pip setuptools
(venv)$ pip install -U cuckoo
```
4. install dpkt
```
sudo pip install --ignore-installed dpkt
```
5. install tcpdump
```
sudo setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump
getcap /usr/sbin/tcpdump
```
6. install pydeep
```
sudo wget http://sourceforge.net/projects/ssdeep/files/ssdeep-2.13/ssdeep-2.13.tar.gz/download -O ssdeep-2.13.tar.gz --no-check-certificate
tar -zxvf ssdeep-2.13.tar.gz
cd ssdeep-2.13/
sudo ./configure
sudo make
sudo make install
ssdeep -V
cd ../
```
7. install volatility
```
git clone https://github.com/volatilityfoundation/volatility.git
cd volatility
sudo python setup.py build
pip install pycrypto distorm3
sudo python setup.py install
```

# 2. Create a virtual machine
1. Use Windows 7 (x64) or Windows 10 (x64) image, we can download them from [MSDN-ITellMe](https://msdn.itellyou.cn/).
2. After install Windows, the most important things to do are to turn off Windows Firewall and Automatic Updates. These will affect the behavior of the malware and thus Cuckoo's analysis of these behaviors. Then disable UAC and cancel administrator account password.
3. As of version 0.4, it is able to interact with Cuckoo via the XMLRPC protocol. See details: [cuckoo-network](https://cuckoo-sandbox.readthedocs.io/zh-cn/latest/installation/guest/network.html)
4. Copy `$CWD/agent/agent.py` to virtual machine, and run it.
5. Create a VirtualBox snapshot:
```
$ VBoxManage snapshot "<Name of VM>" take "<Name of snapshot>" --pause
```
and snapshot can be shut down and restored with the following commands: 
```
$ VBoxManage controlvm "<Name of VM>" poweroff
$ VBoxManage snapshot "<Name of VM>" restorecurrent
```
# 3. Submit samples
Use the following command to submits samples:
```
$ cuckoo submit --package ps1 --machine windows10_x64 --platform windows --timeout 120 --memory  /dir/to/samples
```
# 4. Copy report log
Following is an example of an analysis directory structure:
```
.
|-- analysis.log
|-- binary
|-- dump.pcap
|-- memory.dmp
|-- files
|   |-- 1234567890_dropped.exe
|-- logs
|   |-- 1232.bson
|   |-- 1540.bson
|   `-- 1118.bson
|-- reports
|   |-- report.html
|   |-- report.json
`-- shots
    |-- 0001.jpg
    |-- 0002.jpg
    |-- 0003.jpg
    `-- 0004.jpg
```
Then copy `REPORT_DIR/reports/report.json` to a new directory named **reports**.

# 5. deploying corpus generator environment
1. Make sure that the Python version is greater than or equal to Python 3.6.
2. Download **corpus.py**, and make a new directory named **corpus**.
3. Copy **reports** to current directory.
4. The **corpus** and **reports** on git are the test dataset.

# 6. generate corpus
Run the following shell:
```
python3 corpus.py
```
# 7. check corpus
When step 2 is completed, the corpus files are automatically generated in the corpus directory, each in the format `[original filename].txt`.

