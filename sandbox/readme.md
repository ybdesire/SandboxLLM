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


