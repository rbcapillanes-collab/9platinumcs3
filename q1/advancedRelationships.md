# Advanced Class Relationships

## Previous Activities

[classAttrib](classAttributesMethods.md)

[classRel](classRelationships.md)

## Existing System Description: 
Class 1: CriminalCases

Class 2: DefendantVerdict 

Problems and Limitations: The main problems with the current system design are the attribute redundancy, method duplication, inappropriate entity modeling, and lack of separation of concerns. The two classes, CriminalCases and DefendantVerdict, redundantly store CaseName as an attribute and have the same methods of retrieving case summary information, GetCaseSummary() and caseSummary(). Moreover, the DefendantVerdict class is used to define a temporary judicial action or event outcome as an entity and confuses the case’s attributes, verdict flags, and text details. Additionally, the key entities in the system, such as Plaintiff, Defendant, Judge, Hearings, are stored as string or boolean data types, which hides their ownership and does not allow creating objects with high cohesion and scalability in court management domain.

## Inhertinace Relationship

Parent: CriminalCases

Child: DefendantVerdict

Explanation: CriminalCases is the broader scope of everything involving, as it suggests, A legal Criminal case. Meanwhile, DefendantVerdict focus on the scope of the Defendant duirng said CriminalCase. 

## Inheritance UML

![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation

Relationship:

Explanation:

## Advanced UML Diagram

![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation

[Source Code](advancedRelationships.py)

## Test Run

![Test](images/advancedTestRun.png)

## Object Diagram

![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
