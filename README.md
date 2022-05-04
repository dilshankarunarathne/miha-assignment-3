# Assignment 3
The current COVID-19 (Novel Coronavirus) situation represents a 
threat to society since it can result in Pneumonia complications, 
which can result in mortality. To reduce the transmission of coronavirus, 
three basic mitigation approaches have been found. Testing, self-isolation, 
and contact tracking are the three methods. Almost every country that has 
experienced this pandemic has implemented these mitigating measures to 
combat the virus's global spread. Your job is to create a coronavirus 
contact tracing program. A file containing contact information is sent 
to you. As rows, this data provides contact information. Each row provides 
the two people's NIC numbers as well as the contact date. Given that one 
of one person's contacts is a COVID-19 suspect, you must output the NIC 
numbers of those who are inside the cluster of that person's contact 
so that they may be quarantined.

# NOTE:
* The cluster will be detected during the last 14 days of a person being 
recognized as a COVID-19 suspect. For example, if a person with the NIC 
number 1994010101 is recognized as a COVID-19 suspect on June 4th, the 
cluster will be detected from May 20th onwards.
* People from all levels of contact are represented in the cluster 
(Not only the direct contact).
* As the COVID-19 suspect identification date, you will only be provided 
dates that are greater than the dates found in the contact history data. 
(It's assumed that once a person is recognized as a COVID19 suspect, he'll 
be isolated and no contact history will be discovered.)
* Only 2020 dates are included in the contact history file. 
* You are not permitted to utilize any of the libraries.

# Input Format 
File input: List of contacts and the date of contact separated by commas 
in each row of the input file named Input.txt.  
Terminal input: NIC number of the COVID-19 suspect and the date of 
recognition separated by a space.

# Output Format
output file: List of NIC numbers of people in the contact cluster of the 
COVID-19 suspect in sorted order. Filename is Output.txt

# Example Input
Input.txt  
![](\static\1.png)
  
Terminal:
1994000005 01-05-2020  

# Example Output
Output.txt
![](\static\2.png)

## Credit goes to MIHA