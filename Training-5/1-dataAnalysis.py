import pandas as pd

# 데이터셋 로드
data = pd.read_csv('/Users/goldchae/Desktop/code/KakaoBootcamp-AI/Training-5/HeartDiseaseTrain-Test.csv')

# 데이터의 처음 몇 줄을 출력하여 구조 확인
print("#"*10)
print("데이터의 처음 몇 줄을 출력하여 구조 확인")
print(data.head())

# ##########
# 데이터의 처음 몇 줄을 출력하여 구조 확인
#    age     sex chest_pain_type  resting_blood_pressure  cholestoral  \
# 0   52    Male  Typical angina                     125          212   
# 1   53    Male  Typical angina                     140          203   
# 2   70    Male  Typical angina                     145          174   
# 3   61    Male  Typical angina                     148          203   
# 4   62  Female  Typical angina                     138          294   

#       fasting_blood_sugar               rest_ecg  Max_heart_rate  \
# 0    Lower than 120 mg/ml  ST-T wave abnormality             168   
# 1  Greater than 120 mg/ml                 Normal             155   
# 2    Lower than 120 mg/ml  ST-T wave abnormality             125   
# 3    Lower than 120 mg/ml  ST-T wave abnormality             161   
# 4  Greater than 120 mg/ml  ST-T wave abnormality             106   

#   exercise_induced_angina  oldpeak        slope vessels_colored_by_flourosopy  \
# 0                      No      1.0  Downsloping                           Two   
# 1                     Yes      3.1    Upsloping                          Zero   
# 2                     Yes      2.6    Upsloping                          Zero   
# 3                      No      0.0  Downsloping                           One   
# 4                      No      1.9         Flat                         Three   

#          thalassemia  target  
# 0  Reversable Defect       0  
# 1  Reversable Defect       0  
# 2  Reversable Defect       0  
# 3  Reversable Defect       0  
# 4       Fixed Defect       0  

# 데이터의 각 컬럼에 대한 정보 확인
print("#"*10)
print("데이터의 각 컬럼에 대한 정보 확인")
print(data.info())


# ##########
# 데이터의 각 컬럼에 대한 정보 확인
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1025 entries, 0 to 1024
# Data columns (total 14 columns):
#  #   Column                         Non-Null Count  Dtype  
# ---  ------                         --------------  -----  
#  0   age                            1025 non-null   int64  
#  1   sex                            1025 non-null   object 
#  2   chest_pain_type                1025 non-null   object 
#  3   resting_blood_pressure         1025 non-null   int64  
#  4   cholestoral                    1025 non-null   int64  
#  5   fasting_blood_sugar            1025 non-null   object 
#  6   rest_ecg                       1025 non-null   object 
#  7   Max_heart_rate                 1025 non-null   int64  
#  8   exercise_induced_angina        1025 non-null   object 
#  9   oldpeak                        1025 non-null   float64
#  10  slope                          1025 non-null   object 
#  11  vessels_colored_by_flourosopy  1025 non-null   object 
#  12  thalassemia                    1025 non-null   object 
#  13  target                         1025 non-null   int64  
# dtypes: float64(1), int64(5), object(8)
# memory usage: 112.2+ KB
# None


# 데이터 타입 확인
print("#"*10)
print("데이터 타입 확인")
print("Data Types:\n", data.dtypes)

# ##########
# 데이터 타입 확인
# Data Types:
#  age                                int64
# sex                               object
# chest_pain_type                   object
# resting_blood_pressure             int64
# cholestoral                        int64
# fasting_blood_sugar               object
# rest_ecg                          object
# Max_heart_rate                     int64
# exercise_induced_angina           object
# oldpeak                          float64
# slope                             object
# vessels_colored_by_flourosopy     object
# thalassemia                       object
# target                             int64
# dtype: object

# 범주형 및 수치형 데이터 분리하여 분석
categorical_cols = data.select_dtypes(include=['object', 'category']).columns
numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns

print("#"*10)
print("범주형 데이터 분리하여 분석")
print("\nCategorical Columns:\n", categorical_cols)

print("#"*10)
print("수치형 데이터 분리하여 분석")
print("\nNumerical Columns:\n", numerical_cols)

# ##########
# 범주형 데이터 분리하여 분석

# Categorical Columns:
#  Index(['sex', 'chest_pain_type', 'fasting_blood_sugar', 'rest_ecg',
#        'exercise_induced_angina', 'slope', 'vessels_colored_by_flourosopy',
#        'thalassemia'],
#       dtype='object')
# ##########
# 수치형 데이터 분리하여 분석

# Numerical Columns:
#  Index(['age', 'resting_blood_pressure', 'cholestoral', 'Max_heart_rate',
#        'oldpeak', 'target'],
#       dtype='object')

# 결측치 확인
print("\nMissing Values:\n", data.isnull().sum())

# 각 범주형 변수의 유니크한 값과 빈도수
for col in categorical_cols:
    print(f"\nUnique values in {col}:\n", data[col].value_counts())

# 수치형 데이터의 기초 통계
print("\nDescriptive Statistics for Numerical Data:\n", data[numerical_cols].describe())

# Missing Values:
#  age                              0
# sex                              0
# chest_pain_type                  0
# resting_blood_pressure           0
# cholestoral                      0
# fasting_blood_sugar              0
# rest_ecg                         0
# Max_heart_rate                   0
# exercise_induced_angina          0
# oldpeak                          0
# slope                            0
# vessels_colored_by_flourosopy    0
# thalassemia                      0
# target                           0
# dtype: int64

# Unique values in sex:
#  sex
# Male      713
# Female    312
# Name: count, dtype: int64

# Unique values in chest_pain_type:
#  chest_pain_type
# Typical angina      497
# Non-anginal pain    284
# Atypical angina     167
# Asymptomatic         77
# Name: count, dtype: int64

# Unique values in fasting_blood_sugar:
#  fasting_blood_sugar
# Lower than 120 mg/ml      872
# Greater than 120 mg/ml    153
# Name: count, dtype: int64

# Unique values in rest_ecg:
#  rest_ecg
# ST-T wave abnormality           513
# Normal                          497
# Left ventricular hypertrophy     15
# Name: count, dtype: int64

# Unique values in exercise_induced_angina:
#  exercise_induced_angina
# No     680
# Yes    345
# Name: count, dtype: int64

# Unique values in slope:
#  slope
# Flat           482
# Downsloping    469
# Upsloping       74
# Name: count, dtype: int64

# Unique values in vessels_colored_by_flourosopy:
#  vessels_colored_by_flourosopy
# Zero     578
# One      226
# Two      134
# Three     69
# Four      18
# Name: count, dtype: int64

# Unique values in thalassemia:
#  thalassemia
# Fixed Defect         544
# Reversable Defect    410
# Normal                64
# No                     7
# Name: count, dtype: int64

# Descriptive Statistics for Numerical Data:
#                 age  resting_blood_pressure  cholestoral  Max_heart_rate  \
# count  1025.000000             1025.000000   1025.00000     1025.000000   
# mean     54.434146              131.611707    246.00000      149.114146   
# std       9.072290               17.516718     51.59251       23.005724   
# min      29.000000               94.000000    126.00000       71.000000   
# 25%      48.000000              120.000000    211.00000      132.000000   
# 50%      56.000000              130.000000    240.00000      152.000000   
# 75%      61.000000              140.000000    275.00000      166.000000   
# max      77.000000              200.000000    564.00000      202.000000   

#            oldpeak       target  
# count  1025.000000  1025.000000  
# mean      1.071512     0.513171  
# std       1.175053     0.500070  
# min       0.000000     0.000000  
# 25%       0.000000     0.000000  
# 50%       0.800000     1.000000  
# 75%       1.800000     1.000000  
# max       6.200000     1.000000  

# 왜도와 첨도 확인
"""
왜도(Skewness): 0에 가까울수록 정규분포에 근사, 양의 값은 오른쪽 꼬리가 긴 분포(왼쪽으로 치우친), 음의 값은 왼쪽 꼬리가 긴 분포(오른쪽으로 치우친)
첨도(Kurtosis): 0에 가까울수록 정규분포에 근사, 높으면 분포가 뾰족하고, 낮으면 평평
"""

print("\nSkewness of the data:\n", data[numerical_cols].skew())
print("\nKurtosis of the data:\n", data[numerical_cols].kurt())

# Skewness of the data:
#  age                      -0.248866
# resting_blood_pressure    0.739768
# cholestoral               1.074073
# Max_heart_rate           -0.513777
# oldpeak                   1.210899
# target                   -0.052778
# dtype: float64

# Kurtosis of the data:
#  age                      -0.525618
# resting_blood_pressure    0.991221
# cholestoral               3.996803
# Max_heart_rate           -0.088822
# oldpeak                   1.314471
# target                   -2.001123
# dtype: float64

"""
상관계수 값이 1에 가까울수록 완벽한 양의 상관관계, -1에 가까울수록 완벽한 음의 상관관계를 나타냅니다.
"""

# 피어슨 상관 계수
print("Pearson Correlation:\n", data[numerical_cols].corr(method='pearson'))

# 스피어만 상관 계수
print("\nSpearman Correlation:\n", data[numerical_cols].corr(method='spearman'))

# Pearson Correlation:
#                               age  resting_blood_pressure  cholestoral  \
# age                     1.000000                0.271121     0.219823   
# resting_blood_pressure  0.271121                1.000000     0.127977   
# cholestoral             0.219823                0.127977     1.000000   
# Max_heart_rate         -0.390227               -0.039264    -0.021772   
# oldpeak                 0.208137                0.187434     0.064880   
# target                 -0.229324               -0.138772    -0.099966   

#                         Max_heart_rate   oldpeak    target  
# age                          -0.390227  0.208137 -0.229324  
# resting_blood_pressure       -0.039264  0.187434 -0.138772  
# cholestoral                  -0.021772  0.064880 -0.099966  
# Max_heart_rate                1.000000 -0.349796  0.422895  
# oldpeak                      -0.349796  1.000000 -0.438441  
# target                        0.422895 -0.438441  1.000000  

# Spearman Correlation:
#                               age  resting_blood_pressure  cholestoral  \
# age                     1.000000                0.280189     0.203253   
# resting_blood_pressure  0.280189                1.000000     0.127010   
# cholestoral             0.203253                0.127010     1.000000   
# Max_heart_rate         -0.382724               -0.028880    -0.054794   
# oldpeak                 0.264500                0.146722     0.057102   
# target                 -0.240326               -0.115009    -0.132926   

#                         Max_heart_rate   oldpeak    target  
# age                          -0.382724  0.264500 -0.240326  
# resting_blood_pressure       -0.028880  0.146722 -0.115009  
# cholestoral                  -0.054794  0.057102 -0.132926  
# Max_heart_rate                1.000000 -0.439987  0.429832  
# oldpeak                      -0.439987  1.000000 -0.437669  
# target                        0.429832 -0.437669  1.000000  

from scipy import stats

"""
T-통계량의 절대값이 크면 클수록 두 그룹 간의 차이가 크다고 할 수 있습니다.

일반적으로 P-값이 0.05보다 작으면 귀무 가설을 기각하고, 통계적으로 유의미한 차이가 있음을 인정합니다
"""

# 남성과 여성 그룹 데이터 분할
male_max_hr = data[data['sex'] == 'Male']['Max_heart_rate']
female_max_hr = data[data['sex'] == 'Female']['Max_heart_rate']

# 두 그룹 간의 평균 최대 심박수 차이 검정
t_stat, p_val = stats.ttest_ind(male_max_hr, female_max_hr)
print(f"T-statistic: {t_stat}, P-value: {p_val}")

# T-statistic: -1.5808436320867354, P-value: 0.1142229084355055

print(male_max_hr)

# 0       168
# 1       155
# 2       125
# 3       161
# 6       140
#        ... 
# 1019    143
# 1020    164
# 1021    141
# 1022    118
# 1024    113
# Name: Max_heart_rate, Length: 713, dtype: int64