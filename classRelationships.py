class CriminalCases:
    def __init__(self, CaseName, CaseYear, IsClosed, Plaintiff):
        self.CaseName = CaseName
        self.CaseYear = CaseYear
        self.defendant_verdicts = []

        self.__IsClosed = IsClosed
        self.__Plaintiff = Plaintiff
    
    def add_defendant_verdict(self, defendant_verdict):
        self.defendant_verdicts.append(defendant_verdict)

    def StatusUpdate(self, status: bool):
        self.__IsClosed = status

    def AssignJudge(self, JudgeName):
        if not self.__IsClosed:
            return f"Judge {JudgeName} has been assigned to the case {self.CaseName}."
        return f"Cannot assign a judge to the case {self.CaseName} as it is closed."

    def GetCaseSummary(self):
        status = "Closed" if self.__IsClosed else "Open"
        return f"Case: {self.CaseName}, Year: {self.CaseYear}, Plaintiff: {self.__Plaintiff}, Status: {status}"


class DefendantVerdict:
    def __init__(self, DefendantName, Verdict, Reason, SentenceDetails=""):
        self.DefendantName = DefendantName
        self.Reason = Reason
        self.__Verdict = Verdict
        self.__SentenceDetails = SentenceDetails
        self.statusVerdict(Verdict)
    
    def statusVerdict(self, Verdict):
        if Verdict is True:
            self.__Sentence = False #Innocent
        else: 
            self.__Sentence = True #Guilty

    def showSentence(self):
        if self.__Sentence:
            return f"GUILTY: Defendant {self.DefendantName} is guilty. Sentence Details: {self.__SentenceDetails}"
        else:
            return f"INNOCENT: Defendant {self.DefendantName} is innocent. No sentence details available."

    def caseSummary(self):
        return f"Defendant: {self.DefendantName}, Verdict: {self.__Verdict}, Reason: {self.Reason}, Sentence Details: {self.__SentenceDetails}"

if __name__ == "__main__":
    print("--- BEFORE RELATIONSHIP ---")
    case1 = CriminalCases("State vs. Doe", 2023, False, "State")

    defendant1 = DefendantVerdict("John Doe", False, "DNA Evidence", "10 years imprisonment")
    defendant2 = DefendantVerdict("Jane Smith", True, "Alibi Confirmed", "")
    defendant3 = DefendantVerdict("Mary Grace Piattos", False, "Fingerprint match", "2 years probation")

    print(f"Main Object: {case1.GetCaseSummary()}")
    print("Adding objects...")
    print(f"Related Object 1: {defendant1.caseSummary()}")
    print(f"Related Object 2: {defendant2.caseSummary()}")
    print(f"Related Object 3: {defendant3.caseSummary()}")
    print("Relationship established.\n")

    print("--- BUILDING RELATIONSHIP ---")
    print("Adding related objects to the main object...")
    case1.add_defendant_verdict(defendant1)
    case1.add_defendant_verdict(defendant2)
    case1.add_defendant_verdict(defendant3)
    print("Relationship built successfully.\n")

    print("--- AFTER RELATIONSHIP ---")
    print(f"Main Object: {case1.GetCaseSummary()}")
    print("Related Objects:")
    for item in case1.defendant_verdicts:
        print(f"-> {item.caseSummary()}")
        print(f"   Sentence Details: {item.showSentence()}")
    