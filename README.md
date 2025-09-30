# TDD Practice Repository

켄트 벡(Kent Beck)의 『Test-Driven Development: By Example』을 바탕으로 TDD를 연습하는 저장소입니다.

## 목표

- Red-Green-Refactor 사이클 체득
- 작은 단위의 테스트부터 시작하여 점진적으로 기능 구현
- 테스트 코드를 통한 설계 개선

## 구성

각 연습 문제별로 별도의 디렉토리를 구성하여 단계별로 TDD를 적용합니다.

## TDD 사이클

1. **Red**: 실패하는 테스트 작성
2. **Green**: 테스트를 통과하는 최소한의 코드 작성
3. **Refactor**: 코드 개선 및 중복 제거

## 테스트 실행 방법

### Chapter 1 - Money 예제

```bash
# 모든 테스트 실행
python -m pytest ch-1/tests/

# 특정 테스트 파일 실행
python -m pytest ch-1/tests/test_currency.py

# 특정 테스트 케이스 실행
python -m pytest ch-1/tests/test_currency.py::TestMoney::test_multiplication

# 상세한 출력과 함께 실행
python -m pytest ch-1/tests/ -v

# 실패한 테스트만 다시 실행
python -m pytest ch-1/tests/ --lf
```

## 참고 자료

- Kent Beck, "Test-Driven Development: By Example"
