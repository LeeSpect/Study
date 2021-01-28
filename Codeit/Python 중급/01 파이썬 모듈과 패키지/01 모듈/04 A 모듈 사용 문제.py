# main.py

import cil# cil 모듈을 임포트해 주세요
### 코드를 작성해 주세요 ###
from cil import display # cil 모듈의 display 함수를 직접 임포트해 주세요
### 코드를 작성해 주세요 ###

img1 = cil.read_image('img1')
img2 = cil.read_image('img2')

inverted_img1 = cil.invert(img1)
inverted_img2 = cil.invert(img2)

print('원본 이미지')
print('\nimage1:')
display(img1)
print('\nimage2:')
display(img2)

print('\n색상 반전된 이미지')
print('\nimage1:')
display(inverted_img1)
print('\nimage2:')
display(inverted_img2)

# 채점 코드
print()
print('cil' in dir())
print('display' in dir())

# --------------------------------------------------------------------------------------------------------------

# cil.py

# 이미지를 파일에서 읽어오는 함수
def read_image(filepath):
    img = []
    with open(filepath, 'r') as f:
        data = f.readlines()

    for row in data:
        row = row[:-1]
        img.append([int(bit) for bit in row])
    return img


# 이미지를 파일에 저장해 주는 함수
def save_image(img, filepath):
    with open(filepath, 'w+') as f:
        for row in img:
            line = ''
            for bit in row:
                line += str(bit)
            line += '\n'
            f.write(line)


# 이미지를 디스플레이해 주는 함수
def display(img):
    height, width = len(img), len(img[0])
    for i in range(height):
        for j in range(width):
            print(img[i][j], end=' ')
        print()


# 이미지 색상 반전
def invert(img):
    # img 이미지 크기
    height, width = len(img), len(img[0])

# 작성 시작
    new_img = empty_image(height, width)
    for i in range(height):
        for j in range(width):
            new_img[i][j] = invert_bit(img[i][j])

# 작성 끝
    return new_img


# -1로 채워진 새로운 이미지 생성
def empty_image(height, width):
    new_img = []
    for i in range(height):
        new_img.append([-1] * width)
    return new_img


# 비트 반전
def invert_bit(bit):
    return 1 - bit
    
# --------------------------------------------------------------------------------------------------------------

# 출력

원본 이미지

image1:
0 1 1
1 0 1
0 0 1

image2:
1 0 0 0 1
0 0 0 1 1
0 0 1 0 1
0 1 0 0 1
1 1 1 1 1

색상 반전된 이미지

image1:
1 0 0 
0 1 0
1 1 0

image2:
0 1 1 1 0
1 1 1 0 0
1 1 0 1 0
1 0 1 1 0
0 0 0 0 0

True
True
