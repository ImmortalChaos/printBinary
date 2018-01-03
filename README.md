# pythonFileUtil

이 프로젝트는 python을 이용하여 파일의 일부 내용을 바꾸거나 잘라내어 추출하는 등 유틸리티 함수를 모아놓은 오픈소스 프로젝트입니다.

# printBinary.py

이진 파일을 헥스 에디터에서 보는것과 같이 뷰잉할 수 있는 텍스트 형태로 변환합니다.

사용방법

    python printBinary.py -f [filename] > save.txt

제공옵션

    -f : input file path
    -n : show number line
    -m : limit file size(bytes) 

# cutFile.py

파일의 특정 영역을 잘라내어 별도 다른 파일로 추출합니다.
