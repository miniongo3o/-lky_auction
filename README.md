# 이경영 - 이거 경매해요 0원 부터!

---

# 👨‍👧‍👧 Team

---

## 윤서율, 이민용, 유은서, 김유진

---

2020.10.28 ~ 2020.11.17 

삼성 멀티캠퍼스 [융복합프로젝트형 클라우드 서비스 개발] 과정 - 웹 인터페이스 프로젝트

GitHub repo⇒  [https://github.com/multicampus-3rd-project](https://github.com/multicampus-3rd-project)

---

---

# 📚 Abstract

---

### 이거 경매해요 0원부터!

어렵다고 생각한 경매에 나도 간편하게 참여할 수 있다!

- 경매 주최자가 되기는 어렵다? NO
- 경매는 부자들만 참여한다? NO
- 누구나 쉽게 경매를 시작하고 참여할 수 있는 곳!

---

---

# 🙌 Role

---

## 이민용 (팀장)

---

- 경매 입찰 기능 구현
- 크레딧 충전
- 마이페이지 - 입찰/낙찰 내역 조회
- 시연 영상 제작

## 유은서 (부팀장)

---

- 경매관리(Auction) 모델 작성
- 프론트엔드 전체 틀 구성
- 상품 리스트 조회 (전체, 카테고리 별)
- 경매 마감 기능 구현
- 경매 등록 기능 구현
- 웹 사이트 배포

## 윤서율

---

- MongoDB + Django 연동
- 웹 사이트 컨테이너화 및 배포 - MSA 구현
- 총괄 감독
- 디버깅
- PPT작성

## 김유진

---

- 유저관리(User) 모델 작성
- 로그인/로그아웃, 회원가입 기능 구현
- 마이페이지 - 유저정보 조회기능 구현
- PPT 및 포트폴리오 작성

---

---

# 🚚 Process

---

## 프로젝트 기획 → WBS

---

- MS Project 를 사용한 프로젝트 진행 상황 관리

![Untitled](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled.png)

---

---

# ⚙️ 구현

---

# 1. 시스템 아키텍쳐

---

![Untitled 1](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 1.png)

---

# 2. 기술 스택

---

![Untitled 2](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 2.png)

# 3. Front-end

---

## (1) 싱글페이지

- 페이지의 이동 없이 카테고리에 따른 상품을 볼 수 있다.

![Untitled 3](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 3.png)

![Untitled 4](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 4.png)

![Untitled 5](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 5.png)

- 상품을 클릭하면 클라이언트의 이동 없이 상세 내용을 모달로 보여주는 편리함 구성

![Untitled 6](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 6.png)

![Untitled 7](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 7.png)

## (2) 반응형 페이지

- 해상도에 따라 유연하게 대응하는 반응형 페이지 구현

![Untitled 8](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 8.png)

![Untitled 9](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 9.png)

---

# 4. Back-end

---

## (1) Database 구조

### 1-1 App1 : User

![Untitled 10](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 10.png)

- 장고 기본 유저 모델의 id와 커스텀 유저 모델을 만들어 User_id 속성을 외래키로 두어 연동
- 크레딧 충전 시 연동된 값(user_id)기준으로 데이터 조회 및 크레딧을 관리

### 1-2 App2: Auction

![Untitled 11](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 11.png)

- 상품을 관리하는 auction_product 테이블
- start_date로 상품 등록 날짜를 기록하여 3일이 지난 상품을 관리하는데 이용
- 상품 리스트는 visible_status에 따라 가시화/비가시화
- 상품 등록시 저장한 이름, 사진 , 최소 가격을 결정하고 경매에 참여
- 유저가 입찰한 가격의 타당성이 판별되면, max_price의 값으로 저장

## (2) App1: User

### 2-1 회원가입

- 아이디, 이메일, 비밀번호를 입력하여 회원 가입 가능
- 회원가입 화면에서 로그인 화면으로 전환 가능

![Untitled 12](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 12.png)

- 모든 정보를 입력하지 않거나, 비밀번호가 일치하지 않으면 가입하기 버튼 비활성화

![Untitled 13](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 13.png)

![Untitled 14](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 14.png)

- 가입하기
    - 회원가입이 성공적으로 완료되면 완료 메세지 출력
    - 이미 아이디가 존재하면 경고 메세지가 출력

![Untitled 15](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 15.png)

![Untitled 16](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 16.png)

### 2-2 로그인

- 로그인 화면
    - 회원가입으로 접근 가능

![Untitled 17](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 17.png)

- 로그인 실패시, 메세지 생성
- 로그인 성공시, 메인화면 헤더

![Untitled 18](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 18.png)

### 2-3 로그아웃

- 헤더의 로그아웃 버튼을 클릭하여 로그아웃 가능
- 로그아웃 하면, 메인의 헤더에는 회원가입과 로그인 버튼만 보인다.

![Untitled 19](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 19.png)

### 2-4 마이페이지

- 유저 정보와 입찰 목록을 한눈에 확인할 수 있다.

![Untitled 20](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 20.png)

- 이메일을 수정하고 변경사항을 저장할 수 있다.
    - [변경사항 저장]버튼을 누르면 변경한 내용이 저장되고 완료 메세지가 나온다.

![Untitled 21](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 21.png)

## (3) App2: Auction

### 3-1 경매목록

- 메인화면에서는 카테고리와 상관없이 모든 종류의 경매 리스트를 보여준다.

![Untitled 22](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 22.png)

- 메뉴에서 카테고리를 선택하면, 선택한 메뉴의 색이 변하며 해당 카테고리만을 보여준다.

![Untitled 23](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 23.png)

### 3-2 입찰하기

- 제품 상세페이지에서 [입찰하기]가 가능하다
- 입찰을 하려면 로그인 해야 한다.
    - 로그인 한 경우, [입찰하기] 버튼이 보여진다.
    - 로그인 하지 않은 경우, [로그인하기] 버튼이 보여진다.

![Untitled 24](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 24.png)

- 입찰이 불가능 한 경우,
    - 입력 값이 최소 입찰가 보다 작은 경우
    - 크레딧이 부족한 경우

![Untitled 25](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 25.png)

- 입력 값이 현재 최고가 보다 높고, 크레딧이 충분한 경우 → 입찰 완료

![Untitled 26](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 26.png)

### 3-3 경매등록

- [경매 등록] 메뉴를 통해 페이지 이동

![Untitled 27](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 27.png)

- 입력 형식에 맞춰 작성, 이미지 파일 업로드

![Untitled 28](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 28.png)

- 메인화면에서 상품이 등록된 것을 확인할 수 있다.

![Untitled 29](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 29.png)

### 3-4 크레딧 충전

- 입찰 참여를 위한 금액은 크레딧 충전을 통해 할 수 있다.

![Untitled 30](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 30.png)

- 크레딧 충전 메뉴를 통해 페이지를 이동한다.

![Untitled 31](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 31.png)

- 충전 할 크레딧 금액을 선택하고 충전하기 버튼을 누른다.

![Untitled 32](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 32.png)

- 크레딧이 충전된 것을 확인할 수 있다.

![Untitled 33](C:\Users\ektmf\Desktop\Export-5e05e7b8-88ee-4816-a090-6c9582f71fea\이경영 포트폴리오 467999a473f04eeaae5e6a19ff3a2d69\Untitled 33.png)

## (4) Deploy

### Docker

- api-user : 유저 데이터 관리

```jsx
FROM python:3.8.3-slim

COPY ./api-user/requirements.txt /api-user/requirements.txt
COPY ./api-user/sources /api-user
WORKDIR /api-user

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r /api-user/requirements.txt

ENTRYPOINT ["./start.sh"]
```

- api-auction : 경매 상품 데이터 관리

```jsx
FROM python:3.8.3-slim

COPY ./api-auction/requirements.txt /api-auction/requirements.txt
COPY ./api-auction/sources /api-auction
WORKDIR /api-auction

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r /api-auction/requirements.txt

ENTRYPOINT ["./start.sh"]
```

- docker-compose.yml

```jsx
version: "3"
services:
  # API
  api-user:
    build:
      context: .
      dockerfile: api-user/api-user.Dockerfile
    image: lky/api-user
    ports:
      - "80:8000"

  api-auction:
    build:
      context: .
      dockerfile: api-auction/api-auction.Dockerfile
    image: lky/api-auction
    ports:
      - "7000:7000"
```

### AWS

- EC2를 이용한 배포
- Route53을 이용한 도메인 연결

---

---

# 🏆 Conclusion

## 개선할 점

---

- 부하분산 대책방안 마련
- 데이터베이스 부하 대책 방안


