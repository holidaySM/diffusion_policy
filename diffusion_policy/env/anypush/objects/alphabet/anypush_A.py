import pymunk
import pygame

def add_A(self, position, angle, scale=30, color='LightSlateGray', mask=pymunk.ShapeFilter.ALL_MASKS()):
    mass = 1
    length = 4
    base_width = length * scale
    leg_width = scale / 5
    h = length * scale  # A의 높이

    # 약간의 간격을 두기 위해 작은 값 추가
    epsilon = scale / 100  # 스케일에 비례한 작은 값

    # 왼쪽 다리의 꼭지점 (반시계 방향)
    left_leg_vertices = [
        (-base_width / 2, 0),  # 아래 왼쪽
        (-base_width / 2 + leg_width, 0),  # 아래 오른쪽
        (-leg_width / 2 + epsilon, h - leg_width),  # 위 오른쪽
        (-leg_width / 2 - epsilon, h - leg_width),  # 위 왼쪽
    ]

    # 오른쪽 다리의 꼭지점 (반시계 방향)
    right_leg_vertices = [
        (base_width / 2 - leg_width, 0),  # 아래 왼쪽
        (base_width / 2, 0),  # 아래 오른쪽
        (leg_width / 2 + epsilon, h - leg_width),  # 위 오른쪽
        (leg_width / 2 - epsilon, h - leg_width),  # 위 왼쪽
    ]

    # 가로 막대의 꼭지점 (반시계 방향)
    bar_height = leg_width
    bar_y = h * 0.5
    middle_bar_vertices = [
        (-base_width / 4, bar_y - bar_height / 2),
        (base_width / 4, bar_y - bar_height / 2),
        (base_width / 4, bar_y + bar_height / 2),
        (-base_width / 4, bar_y + bar_height / 2),
    ]

    # 각 부분의 관성 모멘트 계산
    inertia_left = pymunk.moment_for_poly(mass, vertices=left_leg_vertices)
    inertia_right = pymunk.moment_for_poly(mass, vertices=right_leg_vertices)
    inertia_middle = pymunk.moment_for_poly(mass, vertices=middle_bar_vertices)

    # 총 질량과 관성 모멘트
    total_mass = mass * 3
    total_inertia = inertia_left + inertia_right + inertia_middle

    # 바디 생성
    body = pymunk.Body(total_mass, total_inertia)

    # 모양 생성
    shape_left = pymunk.Poly(body, left_leg_vertices)
    shape_right = pymunk.Poly(body, right_leg_vertices)
    shape_middle = pymunk.Poly(body, middle_bar_vertices)

    # 색상 설정
    shape_left.color = pygame.Color(color)
    shape_right.color = pygame.Color(color)
    shape_middle.color = pygame.Color(color)

    # 필터 설정
    shape_left.filter = pymunk.ShapeFilter(mask=mask)
    shape_right.filter = pymunk.ShapeFilter(mask=mask)
    shape_middle.filter = pymunk.ShapeFilter(mask=mask)

    # 바디 속성 설정
    body.position = position
    body.angle = angle
    body.friction = 1

    # 스페이스에 추가
    self.space.add(body, shape_left, shape_right, shape_middle)

    return body
