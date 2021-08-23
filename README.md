# RYULab
This LAB setup to detect DDOS attack on SDN controller using Snort.
The LAB consist of  2 VM. 1 will host the RYU controller and second VM will have the Mininet install.
The VM for this LAB using Oracle Virtual Box
VM with RYU controller will assigned with ip : 192.168.16.4 and the mininet VM using IP 192.168.16.5
VM with the RYU also installed with Snort version 3.0, to test any suspecious traffic from the Openflow Switch toward the controller.

Requirement:
Install the Mininet in on of the VM. In this lab, the VM name Mininet VM
Install the RYU controller in the second VM, name it as RYU VM. Install Snort in this VM too.
Add the 2 rules can be found from Snort Rule.txt into Snort.
For Snort installation can follow guide by Noah dietrich: https://snort-org-site.s3.amazonaws.com/production/document_files/files/000/008/108/original/Snort_3_on_Ubuntu_18_and_20.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIXACIED2SPMSC7GA%2F20210823%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210823T155231Z&X-Amz-Expires=172800&X-Amz-SignedHeaders=host&X-Amz-Signature=28bc84a80f0edd7a5e42957808daf0840fec2e62da2f1740cdfda1a784c822eb

RYU::
In the RYU directory run below RYU application to initiate the SDN controller
Ryu-manager –verbose app/simple_switch.py
::Mininet
Run the topology in mininet run the command below
Sudo mn – custom ~/<mininet/custom>directory for the file/mytopo1.py –topo custom –controller=remote, ip=<IP of the remote controller>
Example as below: 
Sudo mn – custom ~/mininet/custom/mytopo1.py –topo custom –controller=remote, ip=192.168.16.4
