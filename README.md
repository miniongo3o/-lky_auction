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

![Untitled](https://user-images.githubusercontent.com/59273807/99900687-83cfad00-2cf4-11eb-9d90-d8050c060d85.png)

---

---

# ⚙️ 구현

---

# 1. 시스템 아키텍쳐

---

![Untitled 1](https://user-images.githubusercontent.com/59273807/99900688-84684380-2cf4-11eb-91b9-c09cca93db57.png)

---

# 2. 기술 스택

---

![Untitled 2](https://user-images.githubusercontent.com/59273807/99900689-84684380-2cf4-11eb-860c-5c6fe3122b20.png)

# 3. Front-end

---

## (1) 싱글페이지

- 페이지의 이동 없이 카테고리에 따른 상품을 볼 수 있다.

![Untitled 3](https://user-images.githubusercontent.com/59273807/99900691-8500da00-2cf4-11eb-8bb4-26951ad9f652.png)

![Untitled 4](https://user-images.githubusercontent.com/59273807/99900692-85997080-2cf4-11eb-856c-4a7a3a2c00fe.png)

![Untitled 5](https://user-images.githubusercontent.com/59273807/99900693-85997080-2cf4-11eb-9d05-d29a628083a9.png)

- 상품을 클릭하면 클라이언트의 이동 없이 상세 내용을 모달로 보여주는 편리함 구성

![Untitled 6](https://user-images.githubusercontent.com/59273807/99900694-86320700-2cf4-11eb-9016-9837797fca4c.png)

![Untitled 7](https://user-images.githubusercontent.com/59273807/99900695-86ca9d80-2cf4-11eb-8f6c-ea1b9f73b64f.png)

## (2) 반응형 페이지

- 해상도에 따라 유연하게 대응하는 반응형 페이지 구현

![Untitled 8](https://user-images.githubusercontent.com/59273807/99900697-86ca9d80-2cf4-11eb-9b9a-9396a947f279.png)

![Untitled 9](https://user-images.githubusercontent.com/59273807/99900698-87633400-2cf4-11eb-9337-b2b304d29d1f.png)

---

# 4. Back-end

---

## (1) Database 구조

### 1-1 App1 : User

![Untitled 10](https://user-images.githubusercontent.com/59273807/99900700-87633400-2cf4-11eb-84e3-5b967e85c67d.png)

- 장고 기본 유저 모델의 id와 커스텀 유저 모델을 만들어 User_id 속성을 외래키로 두어 연동
- 크레딧 충전 시 연동된 값(user_id)기준으로 데이터 조회 및 크레딧을 관리

### 1-2 App2: Auction

![Untitled 11](https://user-images.githubusercontent.com/59273807/99900702-87fbca80-2cf4-11eb-8bf7-a3d78829cb09.png)

- 상품을 관리하는 auction_product 테이블
- start_date로 상품 등록 날짜를 기록하여 3일이 지난 상품을 관리하는데 이용
- 상품 리스트는 visible_status에 따라 가시화/비가시화
- 상품 등록시 저장한 이름, 사진 , 최소 가격을 결정하고 경매에 참여
- 유저가 입찰한 가격의 타당성이 판별되면, max_price의 값으로 저장

## (2) App1: User

### 2-1 회원가입

- 아이디, 이메일, 비밀번호를 입력하여 회원 가입 가능
- 회원가입 화면에서 로그인 화면으로 전환 가능

![Untitled 12](https://user-images.githubusercontent.com/59273807/99900703-88946100-2cf4-11eb-9275-6c999b0ade0b.png)

- 모든 정보를 입력하지 않거나, 비밀번호가 일치하지 않으면 가입하기 버튼 비활성화

![Untitled 13](https://user-images.githubusercontent.com/59273807/99900705-88946100-2cf4-11eb-8c4f-0af5c0c99aa0.png)

![Untitled 14](https://user-images.githubusercontent.com/59273807/99900706-892cf780-2cf4-11eb-8a38-615b6c98e123.png)

- 가입하기
    - 회원가입이 성공적으로 완료되면 완료 메세지 출력
    - 이미 아이디가 존재하면 경고 메세지가 출력

![Untitled 15](https://user-images.githubusercontent.com/59273807/99900707-892cf780-2cf4-11eb-9e35-04ef29014806.png)

![Untitled 16](https://user-images.githubusercontent.com/59273807/99900708-89c58e00-2cf4-11eb-8ada-7f6b86a0ad8f.png)

### 2-2 로그인

- 로그인 화면
    - 회원가입으로 접근 가능

![Untitled 17](https://user-images.githubusercontent.com/59273807/99900710-89c58e00-2cf4-11eb-91d4-02a56cbb2c81.png)

- 로그인 실패시, 메세지 생성
- 로그인 성공시, 메인화면 헤더

![Untitled 18](https://user-images.githubusercontent.com/59273807/99900711-8a5e2480-2cf4-11eb-8279-7e2bd067cbec.png)

### 2-3 로그아웃

- 헤더의 로그아웃 버튼을 클릭하여 로그아웃 가능
- 로그아웃 하면, 메인의 헤더에는 회원가입과 로그인 버튼만 보인다.

![Untitled 19](https://user-images.githubusercontent.com/59273807/99900672-7dd9cc00-2cf4-11eb-9ccb-527e95ce9ad3.png)

### 2-4 마이페이지

- 유저 정보와 입찰 목록을 한눈에 확인할 수 있다.

![Untitled 20](https://user-images.githubusercontent.com/59273807/99900673-7f0af900-2cf4-11eb-860e-e9f526dce603.png)

- 이메일을 수정하고 변경사항을 저장할 수 있다.
    - [변경사항 저장]버튼을 누르면 변경한 내용이 저장되고 완료 메세지가 나온다.

![Untitled 21](https://user-images.githubusercontent.com/59273807/99900674-7f0af900-2cf4-11eb-9e17-0fe25eb33ac3.png)

## (3) App2: Auction

### 3-1 경매목록

- 메인화면에서는 카테고리와 상관없이 모든 종류의 경매 리스트를 보여준다.

![Untitled 22](https://user-images.githubusercontent.com/59273807/99900675-7fa38f80-2cf4-11eb-8fd5-303998393b3b.png)

- 메뉴에서 카테고리를 선택하면, 선택한 메뉴의 색이 변하며 해당 카테고리만을 보여준다.

![Untitled 23](https://user-images.githubusercontent.com/59273807/99900676-803c2600-2cf4-11eb-8eaf-9e2a444add29.png)

### 3-2 입찰하기

- 제품 상세페이지에서 [입찰하기]가 가능하다
- 입찰을 하려면 로그인 해야 한다.
    - 로그인 한 경우, [입찰하기] 버튼이 보여진다.
    - 로그인 하지 않은 경우, [로그인하기] 버튼이 보여진다.

![Untitled 24](https://user-images.githubusercontent.com/59273807/99900677-80d4bc80-2cf4-11eb-8e83-14bdaae7208d.png)

- 입찰이 불가능 한 경우,
    - 입력 값이 최소 입찰가 보다 작은 경우
    - 크레딧이 부족한 경우

![Untitled 25](https://user-images.githubusercontent.com/59273807/99900678-80d4bc80-2cf4-11eb-9743-0376e7af73b9.png)

- 입력 값이 현재 최고가 보다 높고, 크레딧이 충분한 경우 → 입찰 완료

![Untitled 26](https://user-images.githubusercontent.com/59273807/99900679-816d5300-2cf4-11eb-8c71-40699839eabf.png)

### 3-3 경매등록

- [경매 등록] 메뉴를 통해 페이지 이동

![Untitled 27](https://user-images.githubusercontent.com/59273807/99900680-8205e980-2cf4-11eb-9e5a-308be5a40b6d.png)

- 입력 형식에 맞춰 작성, 이미지 파일 업로드

![Untitled 28](https://user-images.githubusercontent.com/59273807/99900681-8205e980-2cf4-11eb-92a6-5e1d861d5345.png)

- 메인화면에서 상품이 등록된 것을 확인할 수 있다.

![Untitled 29](https://user-images.githubusercontent.com/59273807/99900682-829e8000-2cf4-11eb-80b8-b7be819e9866.png)

### 3-4 크레딧 충전

- 입찰 참여를 위한 금액은 크레딧 충전을 통해 할 수 있다.

![Untitled 30](https://user-images.githubusercontent.com/59273807/99900683-829e8000-2cf4-11eb-9759-50273a3d2461.png)

- 크레딧 충전 메뉴를 통해 페이지를 이동한다.

![Untitled 31](https://user-images.githubusercontent.com/59273807/99900684-83371680-2cf4-11eb-9033-257670e5e593.png)

- 충전 할 크레딧 금액을 선택하고 충전하기 버튼을 누른다.

![Untitled 32](https://user-images.githubusercontent.com/59273807/99900685-83371680-2cf4-11eb-81fc-16b4e4d5a9d8.png)

- 크레딧이 충전된 것을 확인할 수 있다.

![Untitled 33](https://user-images.githubusercontent.com/59273807/99900686-83cfad00-2cf4-11eb-8c2b-18bdb59eef0e.png)

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


