from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from pathlib import Path

@dataclass
class Assignment:
    id: str
    name: str
    
@dataclass
class Student:
    sid: int  # Student id
    name: str  # Capitalized
    name_tokens: list[str]  # Each capitalized
    email: str
    submissions: list['Submission']


@dataclass
class TestResult:
    passing: int
    failing: int
    erroring: int
    skipped: int
    passing_tests: list["TestCase"]
    erroring_tests: list["TestCase"]
    skipped_tests: list["TestCase"]
    failing_tests: list["TestCase"]


@dataclass
class TestCase:
    name: str
    classname: str
    time: str
    failure: Optional[str]
    error: Optional[str]


@dataclass
class Submission:
    download_url: str
    date: datetime
    student: Student
    assignment: Assignment
    file: Optional[Path]

    def get_filename(self):
        return f"{self.assignment.name}-{self.student.name}-{self.student.sid}"

