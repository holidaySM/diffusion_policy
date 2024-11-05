import pymunk
import pygame

def add_3(self, position, angle, scale=30, color='LightSlateGray', mask=pymunk.ShapeFilter.ALL_MASKS()):
    mass = 1
    width = scale * 2          # 숫자 '3'의 너비
    height = scale * 4         # 숫자 '3'의 높이
    thickness = scale / 5      # 선의 두께
    curve_height = height / 2  # 곡선 부분의 높이

    # 상단 가로 막대 (사각형)
    top_bar_vertices = [
        (-width / 2, height / 2 - thickness / 2),
        (width / 2, height / 2 - thickness / 2),
        (width / 2, height / 2 + thickness / 2),
        (-width / 2, height / 2 + thickness / 2),
    ]

    # 중앙 가로 막대 (사각형)
    middle_bar_vertices = [
        (-width / 2, 0 - thickness / 2),
        (width / 2, 0 - thickness / 2),
        (width / 2, 0 + thickness / 2),
        (-width / 2, 0 + thickness / 2),
    ]

    # 하단 가로 막대 (사각형)
    bottom_bar_vertices = [
        (-width / 2, -height / 2 - thickness / 2),
        (width / 2, -height / 2 - thickness / 2),
        (width / 2, -height / 2 + thickness / 2),
        (-width / 2, -height / 2 + thickness / 2),
    ]

    # 오른쪽 세로 막대 (상단부터 중앙까지)
    right_vertical_top_vertices = [
        (width / 2 - thickness / 2, 0 + thickness / 2),
        (width / 2 + thickness / 2, 0 + thickness / 2),
        (width / 2 + thickness / 2, height / 2 - thickness / 2),
        (width / 2 - thickness / 2, height / 2 - thickness / 2),
    ]

    # 오른쪽 세로 막대 (중앙부터 하단까지)
    right_vertical_bottom_vertices = [
        (width / 2 - thickness / 2, -height / 2 + thickness / 2),
        (width / 2 + thickness / 2, -height / 2 + thickness / 2),
        (width / 2 + thickness / 2, 0 - thickness / 2),
        (width / 2 - thickness / 2, 0 - thickness / 2),
    ]

    # 관성 모멘트와 질량 합산
    inertia_top = pymunk.moment_for_poly(mass, top_bar_vertices)
    inertia_middle = pymunk.moment_for_poly(mass, middle_bar_vertices)
    inertia_bottom = pymunk.moment_for_poly(mass, bottom_bar_vertices)
    inertia_right_top = pymunk.moment_for_poly(mass, right_vertical_top_vertices)
    inertia_right_bottom = pymunk.moment_for_poly(mass, right_vertical_bottom_vertices)

    total_mass = mass * 5
    total_inertia = inertia_top + inertia_middle + inertia_bottom + inertia_right_top + inertia_right_bottom

    # 바디 생성
    body = pymunk.Body(total_mass, total_inertia)

    # 모양 생성
    shape_top = pymunk.Poly(body, top_bar_vertices)
    shape_middle = pymunk.Poly(body, middle_bar_vertices)
    shape_bottom = pymunk.Poly(body, bottom_bar_vertices)
    shape_right_top = pymunk.Poly(body, right_vertical_top_vertices)
    shape_right_bottom = pymunk.Poly(body, right_vertical_bottom_vertices)

    # 색상 설정
    for shape in [shape_top, shape_middle, shape_bottom, shape_right_top, shape_right_bottom]:
        shape.color = pygame.Color(color)
        shape.filter = pymunk.ShapeFilter(mask=mask)

    # 바디 속성 설정
    body.position = position
    body.angle = angle
    body.friction = 1

    # 스페이스에 추가
    self.space.add(body, shape_top, shape_middle, shape_bottom, shape_right_top, shape_right_bottom)

    return body
