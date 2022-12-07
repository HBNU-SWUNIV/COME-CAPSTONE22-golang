# 한밭대학교 컴퓨터공학과 GoLang팀

**팀 구성**
- 20171579 김범수 
- 20171581 도용주
- 20171593 이제혁

## Project Background
- ### 필요성
  - OOO
  - OOO
- ### 기존 해결책의 문제점
  - 기술이 발전함에 따라 규모와 복잡성의 증대로 결과를 도출해내기까지 많은 시간이 소요된다.
- ### 모델링 시뮬레이션 공학
  - 자연현상, 사회과학, 공학 분야의 문제를 모델로 만들고 시뮬레이션 하는 과정이다. 자동차, 드론 등 시스템의 행동을 모델링 해서 컴퓨터 시뮬레이션 엔진을 통해 재현하고 그 결과를 도출해 내어 시뮬레이션 상황을 분석하고 실제 상황에 활용할 수 있다.
- ### 이산사건시스템 명세(DEVS) 형식론
  - 이산 시간 사건 모델링을 위한 수학적 틀로 DEVS는 최소단위인 원자 모델과 결합 모델로 이루어 져 있으며 원자 모델은 시스템의 행동을 기록하고 모델의 상태에 따른 동작에 대해 표현한다. 결합 모델 은 모델들을 내부적으로 연결하여 만든 모델로 결합 모델을 통해 복잡한 시스템의 모델링이 가능하다. 
  
  
## System Design
<img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=Go&logoColor=white"> 

  - ### System Requirements
    - 시뮬레이션 엔진 아키텍쳐
    <img src="https://user-images.githubusercontent.com/82207310/206108809-ddbf17f1-1c5e-4761-9445-c594d67dd718.png">
    - 시뮬레이션 엔진 클래스 다이어그램
    <img src="https://user-images.githubusercontent.com/82207310/206108922-0067e694-954f-482d-88f4-eac3731997df.png">
 
## Case Study
   **2022년 제 14회 소외된 이웃과 함께하는 창의설계 온라인 경진대회 참가**
  - 주제 : 개발도상국 협동조합 소득증대를 위한 재고관리SW 설계 및 개발
  - ### System Requirements
    - 저전력 분산컴퓨팅 환경
    - 협동조합원들의 현 상황을 파악하고 이를 바탕으로 협동조합의 의사결정을 지원
    - 오픈소스 기반의 데이터 베이스 관리 시스템
    - 손쉽게 사용할 수 있는 사용자 인터페이스 및 사용자 경험
    - 수확치를 예상해 볼 수 있는 모델링 및 시뮬렐이션 기술을 활용
  - ### Solution & WBS
    <img src="https://user-images.githubusercontent.com/97873618/206085999-5d72eca9-873a-4516-8859-0ae00da9b9f3.PNG">
    
  - ### System Architecture
    <img src="https://user-images.githubusercontent.com/97873618/205780550-1c41f05b-daa0-4a1e-be19-586c0a5f7acd.png" height="80%" width="80%">
    
  - ### Simulation Modeling  
    - 조합원, 협동조합, 구매자 의 행동을 DEVS 기반으로 모델링
    - 지난 1년간의 평균 입고량 과 평균 출하량을 바탕으로 1년동안의 재고량을 시뮬레이션
    <img src="https://user-images.githubusercontent.com/97873618/205785749-a0cdaaa8-cfeb-48ec-abd2-54679a054a1c.png">
  
  - ### Simulation Result
    - 입력 : 보관기간, 수요 변화 예상, 공급 변화 예상
    - 출력 : 입고량, 출하량, 재고, 보관기간이 지나 버려진량, 구매를 희망했으나 재고부족으로 판매하지 못한 양
    <img src="https://user-images.githubusercontent.com/97873618/205791070-4b1cd477-3a35-4c50-9067-3934a8b3bdf2.png" height="70%" width="70%">
## Conclusion
  - ### OOO
  - ### OOO
  (성능비교사진)
  
## Project Outcome
- ### 2022년 한국시뮬레이션학회 춘계온라인 학술대회 참가
- ### 2022년 제 14회 소외된 이웃과 함께하는 창의설계 온라인 경진대회 동상 수상
- ### 2022년 제 11회 정보기술대학 작품전시회 동상 수상

## Poster
<img src="https://user-images.githubusercontent.com/97873618/205790513-104c5004-7337-41b0-bb82-2c2930ce626d.png" height="70%" width="70%">

