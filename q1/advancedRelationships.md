# Advanced Class Relationships

## Previous Activities

[classAttrib](classAttributesMethods.md)

[classRel](classRelationships.md)

## Existing System Description: 
Class 1: CriminalCases

Class 2: DefendantVerdict 

Problems and Limitations: The main problems with the current system design are the attribute redundancy, method duplication, inappropriate entity modeling, and lack of separation of concerns. The two classes, CriminalCases and DefendantVerdict, inefficiently store CaseName as an attribute and have the same methods of retrieving case summary information, GetCaseSummary() and caseSummary(). Moreover, the DefendantVerdict class is used to define a temporary judicial action or event outcome as an entity and confuses the case’s attributes, verdict flags, and text details. And most importantly, a problem I should've noticed when reading the instructions that I cant use my class DefendantVerdict because I cant use a HAS-A(aka assosciation relationship) so I plan to change my child class to AgainstPerson. 

## Inhertinace Relationship

Parent: CriminalCases

Child: AgainstPerson

Explanation: CriminalCases is a broader term, in which there are multiple types of it. One being Crimes against a person. To simplify, AgainstPerson is a type of CriminalCase that can be done.  

## Inheritance UML

![Inheritance](images/inheritanceDiagram.png)
<img width="1414" height="2000" alt="InheritanceDiagram" src="https://github.com/user-attachments/assets/15534632-3a1a-4db4-8bc9-60d13fee3ab4" />


## Composition/Aggregation

Relationship: Composition

Explanation: CriminalCase has a strong composition (HAS-A) relationship with Evidence as an evidence record cannot exist on its own in the system.

## Advanced UML Diagram

![Advanced UML](images/advancedClassDiagram.png) <img width="1414" height="2000" alt="advancedClassDiagram" src="https://github.com/user-attachments/assets/fd4fdc5c-021c-410a-90a6-64303eb2d5bf" />


## Python Implementation

[Source Code](advancedRelationships.py)

## Test Run

![Test](images/advancedTestRun.png) <img width="1652" height="350" alt="igiveup" src="https://github.com/user-attachments/assets/575cc10a-e6ae-4121-864a-17c704c8e3c5" />


## Object Diagram

![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
