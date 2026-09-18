class Evidence: 
    def __init__(self, EvidenceID: str, Description: str, StorageLocation: str, DateCollected: str): 
        self.__EvidenceID = EvidenceID
        self.__Description = Description
        self.__StorageLocation = StorageLocation
        self.__DateCollected = DateCollected

    def VerifyChainOfCustody(self) -> bool:
        return True

    def LogStorageLocation(self, loc: str):
        self.__StorageLocation = loc 

    def GetEvidenceDetails(self) -> str:
        return f"ID: {self.__EvidenceID}, Description: {self.__Description}, Location: {self.__StorageLocation}, Date: {self.__DateCollected}"


class CriminalCase:
    def __init__(self, CaseName: str, CaseYear: int, CaseID: int, Judge: str = "Unassigned", IsClosed: bool = False):
        self.CaseName = CaseName        
        self.CaseYear = CaseYear        
        self.CaseID = CaseID       

        self.__Judge = Judge          
          
        self._IsClosed = IsClosed        

        self.evidence = Evidence("EV-101", "DNA Sample", "Locker A1", "2023-05-12")

    def StatusUpdate(self, status: bool):
        self._IsClosed = status

    def AssignJudge(self, judgeName: str):
        self.__Judge = judgeName

    def GetCaseSummary(self) -> str:
        return f"Case ID: {self.CaseID}, Name: {self.CaseName}, Year: {self.CaseYear}, Closed: {self._IsClosed}, Judge: {self.__Judge}"


class AgainstPerson(CriminalCase):
    def __init__(self, CaseName: str, CaseYear: int, CaseID: int, VictimName: str, InjurySeverity: str, IsWeaponUsed: bool, ProtectiveOrderIssued: bool = False, Judge: str = "Unassigned", IsClosed: bool = False):
        super().__init__(CaseName, CaseYear, CaseID, Judge, IsClosed)
        self.__VictimName = VictimName
        self.__InjurySeverity = InjurySeverity
        self.__IsWeaponUsed = IsWeaponUsed
        self.__ProtectiveOrderIssued = ProtectiveOrderIssued

    def IssueProtectiveOrder(self, expDate: str):
        self.__ProtectiveOrderIssued = True 

    def AssesThreatLevel(self, score: int) -> int:
        return score

    def GetCaseSummary(self) -> str:
        BaseSummary = super().GetCaseSummary()
        return f"{BaseSummary}, Victim: {self.__VictimName}, Injury: {self.__InjurySeverity}, Weapon Used: {self.__IsWeaponUsed}, Protective Order: {self.__ProtectiveOrderIssued}"


class Judge: 
    def __init__(self, Name: str):
        self.Name = Name 

    def PresideOverCase(self, case: CriminalCase):
        print(f"Judge {self.Name} is currently presiding over case '{case.CaseName}' (ID: {case.CaseID})")


print("=== Test 1 — Inheritance ===")
person_case = AgainstPerson(
    CaseName="State vs. Doe", 
    CaseYear=2023, 
    CaseID=2023001, 
    VictimName="John Smith", 
    InjurySeverity="Severe", 
    IsWeaponUsed=True
)

print("Child object (AgainstPerson) accessing parent attributes directly:")
print(f"Parent Case ID: {person_case.CaseID}")
print(f"Parent Case Name: {person_case.CaseName}")
print(f"Parent Case Year: {person_case.CaseYear}")
print(f"Full Child Summary: {person_case.GetCaseSummary()}\n")

print("=== Test 2 — Composition ===")
print("CriminalCase contains Evidence:")
print(f"Evidence inside Case: {person_case.evidence.GetEvidenceDetails()}\n")

print("=== Test 3 — Dependency ===")
judge = Judge("Hon. Sarah Jenkins")
judge.PresideOverCase(person_case)