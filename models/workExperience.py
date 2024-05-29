@dataclass
class WorkExperience:
    startDate: datetime
    endDate: datetime
    translations: List[Translation]
    skills: List[Skill]
