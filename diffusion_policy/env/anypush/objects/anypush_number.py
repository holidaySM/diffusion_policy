import pymunk
import pygame

def add_digit(self, digit, position, angle, scale=50, color='LightSlateGray', mask=pymunk.ShapeFilter.ALL_MASKS(), body_type=pymunk.Body.DYNAMIC):
    mass = 1
    width = scale * 2.5          
    height = scale * 5           
    thickness = scale * 0.7

    # 막대 정의 (9개의 막대 - 상단, 중앙, 하단, 좌상, 좌하, 우상, 우하, 왼쪽중앙, 오른쪽중앙)
    bar_vertices = {
        'top': [
            (-width / 2 + thickness / 2, height / 2 + thickness / 2),
            (width / 2 - thickness / 2, height / 2 + thickness / 2),
            (width / 2 - thickness / 2, height / 2 - thickness / 2),
            (-width / 2 + thickness / 2, height / 2 - thickness / 2),
        ],
        'middle': [
            (-width / 2 + thickness / 2, 0 - thickness / 2),
            (width / 2 - thickness / 2, 0 - thickness / 2),
            (width / 2 - thickness / 2, 0 + thickness / 2),
            (-width / 2 + thickness / 2, 0 + thickness / 2),
        ],
        'bottom': [
            (-width / 2 + thickness / 2, -height / 2 - thickness / 2),
            (width / 2 - thickness / 2, -height / 2 - thickness / 2),
            (width / 2 - thickness / 2, -height / 2 + thickness / 2),
            (-width / 2 + thickness / 2, -height / 2 + thickness / 2),
        ],
        'top_right': [
            (-width / 2 - thickness / 2, 0 ),
            (-width / 2 + thickness / 2, 0 ),
            (-width / 2 + thickness / 2, height / 2 + thickness / 2),
            (-width / 2 - thickness / 2, height / 2 + thickness / 2),
        ],
        'bottom_right': [
            (-width / 2 - thickness / 2, -height / 2 - thickness / 2),
            (-width / 2 + thickness / 2, -height / 2 - thickness / 2),
            (-width / 2 + thickness / 2, 0 ),
            (-width / 2 - thickness / 2, 0 ),
        ],
        'top_left': [
            (width / 2 - thickness / 2, 0 ),
            (width / 2 + thickness / 2, 0 ),
            (width / 2 + thickness / 2, height / 2 + thickness / 2),
            (width / 2 - thickness / 2, height / 2 + thickness / 2),
        ],
        'bottom_left': [
            (width / 2 - thickness / 2, -height / 2 - thickness / 2),
            (width / 2 + thickness / 2, -height / 2 - thickness / 2),
            (width / 2 + thickness / 2, 0 ),
            (width / 2 - thickness / 2, 0 ),
        ],
    }

    # 각 숫자에 대해 활성화될 막대 (top, middle, bottom, top_left, bottom_left, top_right, bottom_right)
    digit_bars = {
        0: ['top', 'bottom', 'top_left', 'bottom_left', 'top_right', 'bottom_right'],
        1: ['top_right', 'bottom_right'],
        2: ['top', 'middle', 'bottom', 'top_right', 'bottom_left'],
        3: ['top', 'middle', 'bottom', 'top_right', 'bottom_right'],
        4: ['middle', 'top_left', 'top_right', 'bottom_right'],
        5: ['top', 'middle', 'bottom', 'top_left', 'bottom_right'],
        6: ['top', 'middle', 'bottom', 'top_left', 'bottom_left', 'bottom_right'],
        7: ['top', 'top_right', 'bottom_right'],
        8: ['top', 'middle', 'bottom', 'top_left', 'bottom_left', 'top_right', 'bottom_right'],
        9: ['top', 'middle', 'bottom', 'top_left', 'top_right', 'bottom_right'],
    }

    # 활성화된 막대에 대한 모멘트 계산 및 생성
    total_mass = mass * len(digit_bars[digit])
    total_inertia = 0
    body = pymunk.Body()
    shapes = []

    for bar in digit_bars[digit]:
        vertices = bar_vertices[bar]
        inertia = pymunk.moment_for_poly(mass, vertices)
        total_inertia += inertia
        shape = pymunk.Poly(body, vertices)
        shape.color = pygame.Color(color)
        shape.filter = pymunk.ShapeFilter(mask=mask)
        shapes.append(shape)

    # 바디 속성 설정
    body.mass = total_mass 
    body.moment = total_inertia
    body.position = position
    body.angle = angle
    body.friction = 1 
    body.body_type = body_type

    # 스페이스에 추가
    self.space.add(body, *shapes)

    return body
