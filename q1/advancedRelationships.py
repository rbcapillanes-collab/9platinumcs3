class CriminalCases:
    def __init__(self, caseID: str, CaseName: str, CaseYear: int, IsClosed: bool = False):
        self._caseID = caseID 

        self.CaseName = CaseName
        self.CaseYear = CaseYear

        self._IsClosed = IsClosed

    def StatusUpdate(self, status: bool):
        self._isClosed == status

    def AssignJudge(self, JudgeName: str):
        pass

    def GetCaseSummary(self):
        return f"Case ID: {self._caseID}, Name: {self.CaseName}, Year: {self.CaseYear}, Closed: {self._IsClosed}"

class AgainstPerson(CriminalCases):
    def __init__(self, caseID: str, CaseName: str, CaseYear: int, VictimName: str, InjurySeverity: str, IsWeaponUsed: bool, ProtectedOrderIssued: bool = False,  IsClosed: bool = False, ):
        super().__init__(caseID, CaseName, CaseYear, IsClosed)
        self.__VictimName = VictimName
        self.__InjurySeverity = InjurySeverity
        self.__IsWeaponedUsed = IsWeaponUsed
        self.__ProtecticeOrderIssued = ProtectedOrderIssued

    def IssueProtectiveOrder(self, ExpDate: str):
        self.__ProtecticeOrderIssued = true 

    def AssesThreatLevel(self, score: int):
        return score

    def GetCaseSummary(self):
        BaseSummary = super().GetCaseSummary
        return f"{BaseSummary}, Victim: {self.__victim_name}, Injury: {self.__injury_severity}, Weapon Used: {self.__is_weapon_used}, Protective Order: {self.__protective_order_issued}"
