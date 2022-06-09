import inspect      #inspect라는 모듈임포트
from travel import *      #찾으려고하는폴더에 *을 임포트


#### 모듈 경로 변경 및 원하는곳으로 이동시키는


print(inspect.getfile(thailand))    #c:\pythoo\basic_gramer_pyrhon\travel\thailand.py 다음과 같이 경로확인됨    