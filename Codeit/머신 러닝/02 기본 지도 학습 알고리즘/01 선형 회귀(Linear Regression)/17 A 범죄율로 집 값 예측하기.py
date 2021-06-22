# 필요한 라이브러리 import
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd  

# 보스턴 집 데이터 갖고 오기
boston_house_dataset = datasets.load_boston()

# 입력 변수를 사용하기 편하게 pandas dataframe으로 변환
x = pd.DataFrame(boston_house_dataset.data, columns=boston_house_dataset.feature_names)

# 목표 변수를 사용하기 편하게 pandas dataframe으로 변환
y = pd.DataFrame(boston_house_dataset.target, columns=['MEDV'])

# 과제 해설
# 가장 먼저 입력 변수 데이터에서 범죄율 열만 선택해주겠습니다.
x = x[['CRIM']]  # 범죄율 열만 사용

# 이제 변수 X에는 입력 변수, 범죄율 데이터가 저장돼있고, y에는 목표 변수, 집 값이 저장되어 있습니다.
# 머신 러닝에서는 항상 모델을 학습시ㅣ는 데이터와 평가하는 데이터를 분리해서 다룬다고 했는데요.
# 이건 scikit-learn의 train_test_split 함수를 사용하면 됩니다.

# train_test_split를 사용해서 주어진 데이터를 학습, 테스트 데이터로 나눈다
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)

# 다음은 나눈 데이터로 모델을 학습시켜야 하는데요. 먼저 scikit-learn에서 모델을 가지고 옵니다.
model = LinearRegression()  # 선형 회귀 모델을 가지고 오고 
# 새로 만든 모델을 training set 데이터만을 이용해서 학습시킵니다.
model.fit(x_train, y_train)  # 학습 데이터를 이용해서 모델을 학습 시킨다
# 위처럼 fit 메소드를 사용하고, 파라미터로 training set 데이터를 넘겨주면 모델을 학습시킬 수 있습니다.

# 마지막으로는 test set 데이터를 이용해서 학습시킨 모델로 예측을 해보겠습니다.
y_test_predict = model.predict(x_test)  # 학습시킨 모델로 예측

# 평균 제곱 오차의 루트를 통해서 테스트 데이터에서의 모델 성능 판단
mse = mean_squared_error(y_test, y_test_predict)

print(mse ** 0.5)

# ----------------------------------------------------------------------------------------------------
8.1806972283173476
# ----------------------------------------------------------------------------------------------------
