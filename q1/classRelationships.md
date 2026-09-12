# Class Relationships: Association and Multiplicity

## Previous Work
[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
Class: CriminalCases

Description: The CriminalCase class represents an individual criminal court case within a legal management system. It manages essential case information and controls operational workflows based on whether the case is active or closed.

## New Related Class
Class: DefendantVerdict

Description: DefendantVerdict class shows the verdict of the defendant of the CriminalCase and a short summary of what happened during the case, which includes the facts of the case, the defendant, the defendants accused crime.

## Association
Relationship: DefendantVerdict BELONGS to CriminalCases

Explanation: DefendantVerdict is the defendant-focused view of the case and also is a direct continuation of the case while CriminalCases is just the broad summary of the case.

## Multiplicity
Multiplicity: Zero or more

Explanation: Its because a single court starts empty and can add, track, or manage zero to many cases as time passing

## UML Class Relationship Diagram
[Class Relationship Diagram]<img width="1414" height="2000" alt="1178" src="https://github.com/user-attachments/assets/0bdf26a3-1dc1-4d69-8ddc-4774141e34e8" />


## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
[Relationship Test Run]<img width="956" height="547" alt="Capture" src="https://github.com/user-attachments/assets/841062fd-efdd-4ffa-b055-ce0b8fd28dbb" />


## Object Relationship Diagram
[Object Relationship Diagram][Uploading Green and Grey Abstract Creative Portfolio Document.png…]()




## Analysis
### What is the association between your two classes?"
ANS: CriminalCases contains entire scope of a case, while DefendantVerdict is assigned to defendant focused. Basically, DefendantVerdict BELONGS to CriminalCases

### What multiplicity did you choose and why?
ANS: Zero or more because a single court starts empty and can add, track, or manage zero to many cases as time passing

### How did you implement the relationship in Python?
ANS: By making an empty list inside the class CriminalCases and the using a method to append DefendantVerdict objects into it.

### Why did you store an object reference instead of copying its data?
ANS: Because storing objects makes sure it syncs and it also saves memory.


### If your relationship uses many, why is a list appropriate?
ANS: Because it can freely change sizes and content, as details are added and/or removed. It allows for easy storage and tracking.
