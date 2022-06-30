from dataclasses import dataclass


@dataclass
class Posting:
    posting_id: int
    nfj_id: str  # id from NFJ,
    title: str
    company_id: int
    salary_id: int


@dataclass
class Company:
    company_id: int
    name: str
    url: str


@dataclass
class Requirement:
    posting_id: int
    technology_id: int
    must: bool


@dataclass
class Technology:
    technology_id: int
    name: int


@dataclass
class Salary:
    salary_id: int
    pay_type_id: int
    high: int
    low: int
    paid_holiday: bool


@dataclass
class PayType:
    pay_type_id: int
    name: str


@dataclass
class PostingLocations:
    posting_id: int
    location_id: int


@dataclass
class LocationType:
    location_id: int
    city: str
    remote: bool
    remote_level: int


@dataclass
class PostingLevel:
    posting_id: int
    level_id: int


@dataclass
class Levels:
    level_id: int
    name: str
