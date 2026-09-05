class CriminalCases: 
    def __init__(self, CaseName, CaseYear, IsClosed, Plaintiff):
        self.CaseName = CaseName
        self.CaseYear = CaseYear

        self.__IsClosed = IsClosed
        self.__Plaintiff = Plaintiff

    def StatusUpdate(self, status: bool):
        self.__IsClosed = status

    def AssignJudge(self, JudgeName):
        if not self.__IsClosed: 
            return f"Judge {JudgeName} has been assigned to the case {self.CaseName}."
        return f"Cannot assign a judge to the case {self.CaseName} as it is closed."

    def GetCaseSummary(self):
        status = "Closed" if self.__IsClosed else "Open"
        return f"Case: {self.CaseName}, Year: {self.CaseYear}, Plaintiff: {self.__Plaintiff}, Status: {status}"


case1 = CriminalCases("State vs. Doe", 2023, False, "State")
case2 = CriminalCases("Smith vs. Johnson", 2022, True, "Smith")

print("--BEFORE--")
print(f"Object 1: {case1.GetCaseSummary()}")
print(f"Object 2: {case2.GetCaseSummary()}")

print("\n--Changing Case 1 status to Closed--")
case1.StatusUpdate(True)

print("\n--AFTER--")
print(f"Object 1 (Updated): {case1.GetCaseSummary()}")
print(f"Object 2 (Unchanged): {case2.GetCaseSummary()}")