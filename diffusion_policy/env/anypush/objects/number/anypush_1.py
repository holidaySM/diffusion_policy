import pymunk
import pygame

def add_1(self, position, angle, scale=30, color='LightSlateGray', mask=pymunk.ShapeFilter.ALL_MASKS()):
    mass = 1
    width = scale       # 숫자 '1'의 너비
    height = 4 * scale  # 숫자 '1'의 높이

    # 사각형의 꼭지점 (반시계 방향), 중심을 원점으로 설정
    vertices = [
        (-width / 2, -height / 2),    # 아래 왼쪽
        (width / 2, -height / 2),     # 아래 오른쪽
        (width / 2, height / 2),      # 위 오른쪽
        (-width / 2, height / 2),     # 위 왼쪽
    ]

    # 관성 모멘트 계산
    inertia = pymunk.moment_for_poly(mass, vertices)

    # 바디 생성
    body = pymunk.Body(mass, inertia)

    # 모양 생성
    shape = pymunk.Poly(body, vertices)

    # 색상 설정
    shape.color = pygame.Color(color)

    # 필터 설정
    shape.filter = pymunk.ShapeFilter(mask=mask)

    # 바디 속성 설정
    body.position = position
    body.angle = angle
    body.friction = 1

    # 스페이스에 추가
    self.space.add(body, shape)

    return body
