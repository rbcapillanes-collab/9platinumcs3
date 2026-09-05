# SG4 - Understanding Classes and Objects

## Class Name
CriminalCase

## Class Description
The CriminalCase class represents an individual criminal court case within a legal management system. It manages essential case information and controls operational workflows based on whether the case is active or closed.

## Properties
| Property | Data Type | Description |
|---|---|---|
| caseName | string | The official title or name of the criminal case |
| caseYear | int | The year when the case was officially recorded |
| isClosed | boolean | Indicates whether the case is resolved (true) or active (false) |
| plaintiff | string | The name of the party or government entity filing the charges |

## Methods
| Method | Description |
|---|---|
| statusUpdate(status : boolean) | Updates the isClosed property to true or false based on the input parameter |
| assignJudge() | Assigns a judge to oversee the case, allowed only if isClosed is false |
| scheduleHearing() | Schedules a court hearing date, allowed only if isClosed is false |
| getCaseSummary() | Returns a detailed summary including court decisions, facts, and key dates |

## Class Diagram
[Class Diagram] <img width="1587" height="2245" alt="Oxblood Red Modern Apple Fruit Poster" src="https://github.com/user-attachments/assets/ecb4cf51-a185-4e79-b0d6-799d1632200e" />


## Design Explanation
### Why did you choose this class?
I chose the CriminalCase class because legal and judicial systems rely heavily on structured record-keeping to manage court workflows accurately. 

### Which property is the most important? Why?
The isClosed property is the most important because it dictates the state of the object. 


### Which method is the most useful? Why?
The statusUpdate(status : boolean) method is the most useful because it directly manages the lifecycle transition of a case. 
