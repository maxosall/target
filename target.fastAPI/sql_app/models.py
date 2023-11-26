from sqlalchemy.orm import relationship
from .database import Base
from enum import Enum
import enum
from click import DateTime
from sqlalchemy import Boolean, Enum, Column, Float, ForeignKey, Integer, String, func, TIMESTAMP
from sqlalchemy.sql.expression import text
from datetime import datetime

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, nullable=False)
  email = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)
  jobs = relationship('Job', back_populates='users')
  created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
  updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())
  
  # group = relationship('Group', back_populates='users') 
  profile = relationship("Profile", uselist=False, back_populates="user")


class Group(Base):
  __tablename__ = 'groups'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  description = Column(String, nullable=True)
  # user_id = Column(Integer, ForeignKey('users.id'))
  # users=relationship('User', back_populates='group')

  created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
  updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())

# class Permission(Base):
#   __tablename__ = 'permissions'
#   id = Column(Integer, primary_key=True, index=True)

class Profile(Base):
  __tablename__ = "profiles"
  id= Column(Integer, primary_key=True)
  first_name = Column(String(150), nullable=False)
  last_name = Column(String(150), nullable=False)
  phone_number = Column(String(150), unique=True, nullable=False)
  address = Column(String)
  resume = Column(String)

  user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
  user = relationship("User", back_populates="profile")

  created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
  updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())

  
# class Role(Base):
#   __tablename__ = 'roles'
#   id = Column(Integer, primary_key=True, index=True)
#   name = Column(String, nullable=False)
#   description = Column(String, nullable=True)
#   permissions = relationship('Permission', secondary='role_permission', back_populates='roles')

# class RolePermission(Base):
#   __tablename__ = 'role_permission'
#   role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)
#   permission_id = Column(Integer, ForeignKey('permissions.id'), primary_key=True)


# class Country(Base):
#   __tablename__ = "countries"

#   id = Column(Integer, primary_key=True)
#   inial = Column(String(2))
#   country_name = Column(String)

# class JobType( enum.Enum):  
#   FULLTIME = "fulltime"
#   PARTTIME = "parttime"
#   CONTRACT = "contract"

# class SalaryType( enum.Enum):  
#   DAILY = "daily"
#   WEEKLY = "weekly"
#   MONTHLY = "monthly"


class Job(Base):
  __tablename__ = 'jobs'
    
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(150), nullable=False)
  decription = Column(String, nullable=False)
  min_salary = Column(Float, nullable=True)
  max_salary = Column(Float, nullable=True)
  user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
  # job_type = Column(Enum(JobType), default=JobType.FULLTIME)
  # salary_type = Column(Enum(SalaryType))
  users = relationship("User", back_populates="jobs")
  created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
  updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())


# class JobField(Base):
#   __tablename__ = 'jobfields'

#   id = Column(Integer, primary_key=True, index=True)
#   title = Column(String, nullable=False)


# class Application(Base):
#   """docstring for Application"""
#   __tablename__ = "applications"
#   id = Column(Integer, primary_key=True, index=True)
#   user_id = Column(Integer, ForeignKey('users.id'))
#   users = relationship('user', back_populates='users')
#   status = Column(Boolean, nullable=True)
#   job_id = Column(Integer, ForeignKey('jobs.id'))
#   jobs = relationship('job', back_populates='jobs')




# class Country(Enum):
    # AF = "Afghanistan"
    # AL = 'Albania'
    # DZ = 'Algeria'
    # AD = 'Andorra'
    # AO = 'Angola'
    # AG = 'Antigua'
    # AR = 'Argentina'
    # AM = 'Armenia'
    # AU = 'Australia'
    # AT = 'Austria'
    # AZ = 'Azerbaijan'
    # BS = 'Bahamas' 
    # BH = 'Bahrain' 
    # BD = 'Bangladesh' 
    # BB = 'Barbados' 
    # BY = 'Belarus' 
    # BE = 'Belgium' 
    # BZ = 'Belize'
    # BJ = 'Benin' 
    # BT = 'Bhutan' 
    # BO = 'Bolivia' 
    # BA = 'Bosnia' 
    # BW = 'Botswana'  
    # BR = 'Brazil'  
    # BN = 'Brunei Darussalam'
    # BG = 'Bulgaria'  
    # BF = 'Burkina Faso'
    # BI = 'Burundi'  
    # CV = 'Cabo Verde'  
    # KH = 'Cambodia'  
    # CM = 'Cameroon'  
    # CA = 'Canada'  
    # CF = 'Central African Republic'
    # TD = 'Chad'  
    # CL = 'Chile' 
    # CN = 'China' 
    # CO = 'Colombia' 
    # KM = 'Comoros' 
    # CD = 'Congo (Democratic Republic of the)' 
    # CG = 'Congo (Republic of the)' 
    # CR = 'Costa Rica' 
    # CI = 'Côte d\'Ivoire' 
    # HR = 'Croatia' 
    # CU = 'Cuba' 
    # CW = 'Curaçao' 
    # CY = 'Cyprus' 
    # CZ = 'Czechia'  
    # DK = 'Denmark' 
    # DJ = 'Djibouti' 
    # DM = 'Dominica' 
    # DO = 'Dominican Republic' 
    # EC = 'Ecuador' 
    # EG = 'Egypt' 
    # SV = 'El Salvador' 
    # GQ = 'Equatorial Guinea' 
    # ER = 'Eritrea' 
    # EE = 'Estonia' 
    # SZ = 'Eswatini' 
    # ET = 'Ethiopia' 
    # FJ = 'Fiji' 
    # FI = 'Finland' 
    # FR = 'France' 
    # GF = 'French Guiana' 
    # PF = 'French Polynesia' 
    # GA = 'Gabon' 
    # GM = 'Gambia' 
    # GE = 'Georgia' 
    # DE = 'Germany' 
    # GH = 'Ghana' 
    # GR = 'Greece' 
    # GD = 'Grenada' 
    # GT = 'Guatemala' 
    # GN = 'Guinea' 
    # GW = 'Guinea-Bissau '
    # GY = 'Guyana' 
    # HT = 'Haiti' 
    # HN = 'Honduras' 
    # HU = 'Hungary' 
    # IS = 'Iceland' 
    # IN = 'India' 
    # ID = 'Indonesia' 
    # IR = 'Iran (Islamic Republic of)' 
    # IQ = 'Iraq' 
    # IE = 'Ireland' 
    # IL = 'Israel' 
    # IT = 'Italy' 
    # JM = 'Jamaica' 
    # JP = 'Japan' 
    # JO = 'Jordan' 
    # KZ = 'Kazakhstan' 
    # KE = 'Kenya' 
    # KI = 'Kiribati' 
    # KW = 'Kuwait' 
    # KG = 'Kyrgyzstan' 
    # LA = 'Lao People\'s Democratic Republic '
    # LV = 'Latvia' 
    # LB = 'Lebanon' 
    # LS = 'Lesotho' 
    # LR = 'Liberia' 
    # LY = 'Libya' 
    # LI = 'Liechtenstein' 
    # LT = 'Lithuania' 
    # LU = 'Luxembourg' 
    # MG = 'Madagascar' 
    # MW = 'Malawi' 
    # MY = 'Malaysia' 
    # MV = 'Maldives' 
    # ML = 'Mali' 
    # MT = 'Malta' 
    # MH = 'Marshall Islands' 
    # MR = 'Mauritania' 
    # MU = 'Mauritius' 
    # MX = 'Mexico' 
    # FM = 'Micronesia (Federated States of)' 
    # MD = 'Moldova (Republic of) '
    # MC = 'Monaco' 
    # MN = 'Mongolia' 
    # ME = 'Montenegro' 
    # MA = 'Morocco' 
    # MZ = 'Mozambique' 
    # MM = 'Myanmar' 
    # NA = 'Namibia' 
    # NR = 'Nauru' 
    # NP = 'Nepal' 
    # NL = 'Netherlands' 
    # NZ = 'New Zealand' 
    # NI = 'Nicaragua' 
    # NE = 'Niger' 
    # NG = 'Nigeria' 
    # KP = 'North Korea (Democratic People\'s Republic of Korea) '
    # MK = 'North Macedonia' 
    # NO = 'Norway' 
    # OM = 'Oman' 
    # PK = 'Pakistan' 
    # PW = 'Palau' 
    # PS = 'Palestine' 
    # PA = 'Panama' 
    # PG = 'Papua New Guinea' 
    # PY = 'Paraguay' 
    # PE = 'Peru' 
    # PH = 'Philippines' 
    # PL = 'Poland' 
    # PT = 'Portugal' 
    # QA = 'Qatar' 
    # RO = 'Romania' 
    # RU = 'Russia' 
    # RW = 'Rwanda' 
    # KN = 'Saint Kitts and Nevis' 
    # LC = 'Saint Lucia' 
    # MF = 'Saint Martin (French part)' 
    # VC = 'Saint Vincent and the Grenadines' 
    # WS = 'Samoa' 
    # SM = 'San Marino' 
    # ST = 'Sao Tome and Principe '
    # SA = 'Saudi Arabia' 
    # SN = 'Senegal' 
    # RS = 'Serbia' 
    # SC = 'Seychelles' 
    # SL = 'Sierra Leone' 
    # SG = 'Singapore' 
    # SK = 'Slovakia' 
    # SI = 'Slovenia' 
    # SB = 'Solomon Islands' 
    # SO = 'Somalia' 
    # ZA = 'South Africa' 
    # KR = 'South Korea (Republic of Korea)' 
    # SS = 'South Sudan' 
    # ES = 'Spain' 
    # LK = 'Sri Lanka' 
    # SD = 'Sudan' 
    # SR = 'Suriname' 
    # SE = 'Sweden' 
    # CH = 'Switzerland' 
    # SY = 'Syrian Arab Republic '
    # TJ = 'Tajikistan' 
    # TZ = 'Tanzania'
    # TH = 'Thailand' 
    # TL = 'Timor-Leste' 
    # TG = 'Togo' 
    # TK = 'Tokelau' 
    # TO = 'Tonga' 
    # TT = 'Trinidad and Tobago' 
    # TN = 'Tunisia' 
    # TR = 'Turkey' 
    # TM = 'Turkmenistan' 
    # TV = 'Tuvalu' 
    # UG = 'Uganda' 
    # UA = 'Ukraine' 
    # ZM = 'Zambia'
    # ZW = 'Zimbabwe' 
    # VU = 'Vanuatu'
    # VA = 'Vatican City'
    # VE = 'Venezuela'
    # VN = 'Vietnam'

    
# JobType = Enum('JobType', ['FULLTIME', 'PARTTIME', 'CONTRACT', 'FREELANCE', 'INTERNSHIP'])
# JobType = Enum('JobType', {'FULLTIME': 1, 'PARTTIME': 2, 'CONTRACT': 3, 'FREELANCE': 4, 'INTERNSHIP': 5})



