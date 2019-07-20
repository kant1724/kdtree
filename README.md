# KDTree (k-dimensional tree)

#### KDTree 상세설명
https://en.wikipedia.org/wiki/K-d_tree

#### 사용언어
Python 3.7

#### Dependency

```
pip install requests==2.21.0  
pip install scipy==1.1.0  
pip install numpy==1.16.4  
```

#### 1. 근접 거리 기반
#### 개요
KDTree와 google API를 이용하여 내 위치에서 가까운 거리순으로 주변 위치정보를 가져온다.  

#### 실행방법
```
  python go_distance.py
```

#### 2. 단어 유사도 기반
#### 개요
KDTree를 이용하여 제품(Product)과 창고의 카테고리(Category)의 유사도가 가까운것 순으로 가져온다.

아래 링크에 있는 파일을 다운로드받아 압축을 풀어 패키지에 포함  
https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ko.300.vec.gz

#### 실행방법
```
  python go_word_vec.py
```

#### 기타 참고 사이트

##### JSI (R-Trees)
http://jsi.sourceforge.net/  

##### 위치정보 기반 솔루션 업체
https://www.sphinfo.com/
