# Class Attributes and Methods
## Previous Design

Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision
No major changes were needed from my original design.

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| CaseName | String | Public | General identification |
| CaseYear | Integer | Public | Further identification and precision |
| IsClosed | Boolean | Private | To prevent illegal tampering |
| Plaintiff | String | Private  | To protect identity and to remain protected from unauthorized edit |

## Updated UML Class Diagram
[Class Diagram] <img width="1587" height="2245" alt="Oxblood Red Modern Apple Fruit Poster" src="https://github.com/user-attachments/assets/511becc2-237f-443d-96ee-30eba0e1eeed" />


## Python Implementation
[View Python Source](classImplementation.py)

## Test Run
[Test Run] <img width="1366" height="729" alt="OOPActTestRun" src="https://github.com/user-attachments/assets/6856a696-ffae-4a72-bfb5-d52f8a5a9f27" />


## Object Diagram
[Object Diagram] <img width="1920" height="1080" alt="object diagram" src="https://github.com/user-attachments/assets/54613a76-c1dc-457b-8a53-00505aa24964" />


## Analysis
### Why did you make your chosen attribute private?
ANS: So that when used, it cant be incorrectly changed since incorrect information may cause harm.

### Which method changes the state of your object?
ANS: IsClosed(Status: Bol)

### How did your two objects demonstrate that instances are independent?
ANS: When I changed the IsClosed of Object 1, Object 2 didnt change at all. 

### What is the difference between your class diagram and your object diagram?|
ANS: The class diagram is simply just the blueprint and is one singular element, while the object diagram has 2 objects made from the singular-blueprint class diagram.
