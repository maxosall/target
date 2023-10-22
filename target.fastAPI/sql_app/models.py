

from enum import Enum
from click import DateTime
from sqlalchemy import Boolean, Column, Double, ForeignKey, Integer, String, func
from sql_app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('group', back_populates='group')


class Country(Enum):
    AF = "Afghanistan"
    AL = 'Albania'
    DZ = 'Algeria'
    AD = 'Andorra'
    AO = 'Angola'
    AG = 'Antigua'
    AR = 'Argentina'
    AM = 'Armenia'
    AU = 'Australia'
    AT = 'Austria'
    AZ = 'Azerbaijan'
    BS = 'Bahamas' 
    BH = 'Bahrain' 
    BD = 'Bangladesh' 
    BB = 'Barbados' 
    BY = 'Belarus' 
    BE = 'Belgium' 
    BZ = 'Belize'
    BJ = 'Benin' 
    BT = 'Bhutan' 
    BO = 'Bolivia' 
    BA = 'Bosnia' 
    BW = 'Botswana'  
    BR = 'Brazil'  
    BN = 'Brunei Darussalam'
    BG = 'Bulgaria'  
    BF = 'Burkina Faso'
    BI = 'Burundi'  
    CV = 'Cabo Verde'  
    KH = 'Cambodia'  
    CM = 'Cameroon'  
    CA = 'Canada'  
    CF = 'Central African Republic'
    TD = 'Chad'  
    CL = 'Chile' 
    CN = 'China' 
    CO = 'Colombia' 
    KM = 'Comoros' 
    CD = 'Congo (Democratic Republic of the)' 
    CG = 'Congo (Republic of the)' 
    CR = 'Costa Rica' 
    CI = 'Côte d\'Ivoire' 
    HR = 'Croatia' 
    CU = 'Cuba' 
    CW = 'Curaçao' 
    CY = 'Cyprus' 
    CZ = 'Czechia'  
    DK = 'Denmark' 
    DJ = 'Djibouti' 
    DM = 'Dominica' 
    DO = 'Dominican Republic' 
    EC = 'Ecuador' 
    EG = 'Egypt' 
    SV = 'El Salvador' 
    GQ = 'Equatorial Guinea' 
    ER = 'Eritrea' 
    EE = 'Estonia' 
    SZ = 'Eswatini' 
    ET = 'Ethiopia' 
    FJ = 'Fiji' 
    FI = 'Finland' 
    FR = 'France' 
    GF = 'French Guiana' 
    PF = 'French Polynesia' 
    GA = 'Gabon' 
    GM = 'Gambia' 
    GE = 'Georgia' 
    DE = 'Germany' 
    GH = 'Ghana' 
    GR = 'Greece' 
    GD = 'Grenada' 
    GT = 'Guatemala' 
    GN = 'Guinea' 
    GW = 'Guinea-Bissau '
    GY = 'Guyana' 
    HT = 'Haiti' 
    HN = 'Honduras' 
    HU = 'Hungary' 
    IS = 'Iceland' 
    IN = 'India' 
    ID = 'Indonesia' 
    IR = 'Iran (Islamic Republic of)' 
    IQ = 'Iraq' 
    IE = 'Ireland' 
    IL = 'Israel' 
    IT = 'Italy' 
    JM = 'Jamaica' 
    JP = 'Japan' 
    JO = 'Jordan' 
    KZ = 'Kazakhstan' 
    KE = 'Kenya' 
    KI = 'Kiribati' 
    KW = 'Kuwait' 
    KG = 'Kyrgyzstan' 
    LA = 'Lao People\'s Democratic Republic '
    LV = 'Latvia' 
    LB = 'Lebanon' 
    LS = 'Lesotho' 
    LR = 'Liberia' 
    LY = 'Libya' 
    LI = 'Liechtenstein' 
    LT = 'Lithuania' 
    LU = 'Luxembourg' 
    MG = 'Madagascar' 
    MW = 'Malawi' 
    MY = 'Malaysia' 
    MV = 'Maldives' 
    ML = 'Mali' 
    MT = 'Malta' 
    MH = 'Marshall Islands' 
    MR = 'Mauritania' 
    MU = 'Mauritius' 
    MX = 'Mexico' 
    FM = 'Micronesia (Federated States of)' 
    MD = 'Moldova (Republic of) '
    MC = 'Monaco' 
    MN = 'Mongolia' 
    ME = 'Montenegro' 
    MA = 'Morocco' 
    MZ = 'Mozambique' 
    MM = 'Myanmar' 
    NA = 'Namibia' 
    NR = 'Nauru' 
    NP = 'Nepal' 
    NL = 'Netherlands' 
    NZ = 'New Zealand' 
    NI = 'Nicaragua' 
    NE = 'Niger' 
    NG = 'Nigeria' 
    KP = 'North Korea (Democratic People\'s Republic of Korea) '
    MK = 'North Macedonia' 
    NO = 'Norway' 
    OM = 'Oman' 
    PK = 'Pakistan' 
    PW = 'Palau' 
    PS = 'Palestine' 
    PA = 'Panama' 
    PG = 'Papua New Guinea' 
    PY = 'Paraguay' 
    PE = 'Peru' 
    PH = 'Philippines' 
    PL = 'Poland' 
    PT = 'Portugal' 
    QA = 'Qatar' 
    RO = 'Romania' 
    RU = 'Russia' 
    RW = 'Rwanda' 
    KN = 'Saint Kitts and Nevis' 
    LC = 'Saint Lucia' 
    MF = 'Saint Martin (French part)' 
    VC = 'Saint Vincent and the Grenadines' 
    WS = 'Samoa' 
    SM = 'San Marino' 
    ST = 'Sao Tome and Principe '
    SA = 'Saudi Arabia' 
    SN = 'Senegal' 
    RS = 'Serbia' 
    SC = 'Seychelles' 
    SL = 'Sierra Leone' 
    SG = 'Singapore' 
    SK = 'Slovakia' 
    SI = 'Slovenia' 
    SB = 'Solomon Islands' 
    SO = 'Somalia' 
    ZA = 'South Africa' 
    KR = 'South Korea (Republic of Korea)' 
    SS = 'South Sudan' 
    ES = 'Spain' 
    LK = 'Sri Lanka' 
    SD = 'Sudan' 
    SR = 'Suriname' 
    SE = 'Sweden' 
    CH = 'Switzerland' 
    SY = 'Syrian Arab Republic '
    TJ = 'Tajikistan' 
    TZ = 'Tanzania'
    TH = 'Thailand' 
    TL = 'Timor-Leste' 
    TG = 'Togo' 
    TK = 'Tokelau' 
    TO = 'Tonga' 
    TT = 'Trinidad and Tobago' 
    TN = 'Tunisia' 
    TR = 'Turkey' 
    TM = 'Turkmenistan' 
    TV = 'Tuvalu' 
    UG = 'Uganda' 
    UA = 'Ukraine' 
    ZM = 'Zambia'
    ZW = 'Zimbabwe' 
    VU = 'Vanuatu'
    VA = 'Vatican City'
    VE = 'Venezuela'
    VN = 'Vietnam'

    
class JobType(Enum):
    FULLTIME = 'FULL TIME'
    PARTTIIME = 'PART TIME'
    CONTRUCTOR = 'CONTRUCTOR'


class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    decription = Column(String, nullable=False)
    min_salary = Column(Double, nullable=True)
    max_salary = Column(Double, nullable=True)

    job_type = Column(Enum(JobType), default=JobType.FULLTIME)

    create_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class JobField(Base):
    __tablename__ = 'jobfields'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    users = relationship('user', back_populates='users')


class Permision(Base):
    __tablename__ = 'permisons'
    id = Column(Integer, primary_key=True, index=True)
