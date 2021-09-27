# ✍️ 한글 폰트 지도

2021년 8월 제주코딩베이스캠프에서 진행했던 프로젝트입니다.

## 1. 프로젝트 소개

### 1.1. 기획 내용

#### 2 page의 웹 서비스 (폰트 지도와 폰트 검색창)

IDEO Font Map(http://fontmap.ideo.com/) 에 착안하여 구상한 아이디어로, IDEO Font Map은 영문 폰트를 디자인 유사도별로 묶어서 지도로 만들어놓은 페이지입니다. 원하는 폰트를 검색하고 유사 폰트를 추천해주기도 합니다. 한글 폰트 지도 프로젝트의 최종 목표는 IDEO Font Map과 같은 서비스를 한글 폰트로 제공하는 것입니다.

폰트 지도는 디자인 작업을 하는 사람들에게 유용합니다. 폰트는 디자인 작업의 중요한 요소로, 어떤 폰트를 활용하느냐에 따라 작업물이 확연히 달라집니다. 한글 폰트 지도로 다양한 폰트를 한 눈에 확인할 수 있다면, 폰트를 보다 효과적으로 활용할 수 있을 것입니다.

주요 기능은 유사 폰트끼리의 Gathering, 폰트 검색, 유사 폰트 추천입니다. 향후 새로운 폰트를 홍보할 수 있는 플랫폼, 인공지능 기반 폰트 자동 분류 기능 등으로 확장할 수 있습니다.

### 1.2. 실제 구현 내용

#### 1 page의 유사 폰트 추천 서비스

짧은 프로젝트 기간과 비대면 환경으로 , 모든 기획을 다 구현할 수는 없었습니다. 코드 작업을 통해 1 page의 유사 폰트 추천 페이지를 구현할 수 있었습니다. 유사 폰트는 100여개 정도의 폰트를 형태, 무게, 인상 3가지로 손수 카테고라이징 하였습니다. 하나의 폰트만을 대상으로 프로토타입 구현을 하였습니다. 프로젝트 기획 시 기능 단위로 Planning 하여, 하나의 기능이 구현되면 바로 다음 기능으로 연결될 수 있게 구상하였습니다. 


## 2. 시연
![image](https://user-images.githubusercontent.com/88834958/134668451-b3e4e6ae-7ca9-479e-b019-431b3190f391.png)
![image](https://user-images.githubusercontent.com/88834958/134669869-efbc44da-f8f4-4593-9fac-f48d94711c08.png)

다음과 같은 한 페이지 서비스를 구현하였습니다. 하나의 폰트에 대해 유사도 순으로 4개의 폰트를 뽑아줍니다. 우상단에 보이는 입력 창에 글자를 입력하면, 그 글자에 유사 폰트들이 적용된 모습을 볼 수 있습니다.

## 3. 제작 기간 & 참여 인원

약 3일 정도가 소요되었으며, 5명의 인원이 참여하였습니다. 코드 작업에 기여한 분들은 프론트엔드 1명, 백엔드 1명으로 총 2명입니다. 나머지 분들은 각각 기획, 유사도 집계, 발표를 담당해주셨습니다. 저는 백엔드 작업을 담당하였습니다.

## 4. 사용한 기술

* Front-end : Javascript JQuery
* Back-end : Python django framework & pandas library

## 5. 핵심 기능

다음 두 가지 기능을 핵심 기능으로 들 수 있습니다.

### 5.1. 유사 폰트 탐색 : 백엔드 작업
  
  pandas library를 활용해 간단한 탐색 알고리즘을 구현하였습니다. count를 매기는 column을 하나 만들어서, 모든 폰트를 순회하면서 counting 해주는 방식으로 작성하였습니다.
  자세한 설명은 코드 주석에 달아두었습니다. (Jupyter Notebook 버전이 보기 편합니다.)
  
  코드 링크 : https://github.com/Woonggss/Hangeul_Font_Map_for_portfolio/blob/main/Hackathon_Server/projectsite/main/similar_font.py
  코드 링크 (Jupyter Notebook) : https://github.com/Woonggss/Hangeul_Font_Map_Project/blob/main/%EC%9C%A0%EC%82%AC%20%ED%8F%B0%ED%8A%B8%20%EB%BD%91%EA%B8%B0%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98(Ranking_top5).ipynb
  
  
### 5.2. 유사 폰트 적용 : 프론트엔드 작업
  
  jQuery를 활용해서 유사 폰트에 해당하는 폰트를 적용해볼 수 있게끔 하였습니다.
  코드 링크 : https://github.com/Woonggss/Hangeul_Font_Map_for_portfolio/blob/main/Hackathon_Server/projectsite/main/templates/main/index.html
   
  
## 6. Trouble Shooting

### 6.1. 탐색 알고리즘을 어떻게 프론트엔드에 연결할 것인가?
  
  pandas를 활용하여 탐색 알고리즘을 작성한 다음 해결해야 할 이슈는, 알고리즘을 사용자 화면에 반영하는 것이었습니다. 문제 해결을 위해, 우선 Flow Chart를 그려서 현황을 파악해보았습니다.
  전반적인 흐름을 그려놓으니 해결이 된 부분과 해결이 되지 않은 부분이 명확하게 보였습니다.
  ![자료형new](https://user-images.githubusercontent.com/88834958/134769569-1a8c105b-6716-4dbb-a2b6-d22fa30e2f57.png)

  
### 6.2. 이슈 : 리스트 자료형 결과를 HTML에 적용한다

  구현한 알고리즘을 모듈화(.py)하여 views.py에서 import한 다음, 알고리즘에 담겨있는 리스트를 render하여 html에서 출력하였습니다. 아래는 문제 해결의 핵심 코드 블럭입니다.
  
  ```python
  # views.py
  from django.shortcuts import render
  import main.similar_font as similar_font
  # Create your views here.


    def index(request):
    
      ls = similar_font.similar_list_top4
    
      return render(request, 'main/index.html', { 'similar_list': ls })
  
  ```
  
  ```HTML
  # index.html의 일부
  <div class="neighboring-font">
     <div class="font-2 neighboring-font__name">{{ similar_list.0 }}</div>
     <div class="font-82 neighboring-font__name">{{ similar_list.1 }}</div>
     <div class="font-40 neighboring-font__name">{{ similar_list.2 }}</div>
     <div class="font-50 neighboring-font__name">{{ similar_list.3 }}</div>
  </div>
  ```
  

## 7. 회고 및 느낀 점

짧은 시간에 최소한의 내용을 베이스로 개발 프로세스 전체를 경험하다보니, 아쉬움이 남는 프로젝트였습니다. 그래도 짧은 기간에 웹 개발의 전반적인 과정을 경험해 볼 수 있었습니다. 다양한 분들과 협업할 수 있었다는 사실은 그 자체로 값진 경험이었습니다. 특히 디자이너 분과 이런저런 이야기를 나눌 기회가 있었는데, 디자인에 문외한인 저로써는 정말 흥미로웠습니다. 개발 공부를 체계적으로 시작할 수 있게 된 계기였던 것 같습니다. 

