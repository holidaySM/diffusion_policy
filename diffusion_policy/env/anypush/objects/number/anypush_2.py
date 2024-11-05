import pymunk
import pygame

def add_2(self, position, angle, scale=30, color='LightSlateGray', mask=pymunk.ShapeFilter.ALL_MASKS()):
    mass = 1
    width = scale * 2          # 숫자 '2'의 너비
    height = scale * 4         # 숫자 '2'의 높이
    thickness = scale / 5      # 선의 두께

    # 도형들의 위치를 기준점으로부터 상대적으로 정의
    half_width = width / 2
    half_height = height / 2
    half_thickness = thickness / 2

    # 바디와 모양을 저장할 리스트
    bodies_and_shapes = []

    # 상단 가로 막대 (바디와 모양 생성)
    top_bar_vertices = [
        (-half_width, half_height - half_thickness),
        (half_width, half_height - half_thickness),
        (half_width, half_height + half_thickness),
        (-half_width, half_height + half_thickness),
    ]
    top_body = pymunk.Body(mass, pymunk.moment_for_poly(mass, top_bar_vertices))
    top_shape = pymunk.Poly(top_body, top_bar_vertices)
    top_shape.color = pygame.Color(color)
    top_shape.filter = pymunk.ShapeFilter(mask=mask)
    top_body.position = position
    top_body.angle = angle
    top_body.friction = 1
    self.space.add(top_body, top_shape)
    bodies_and_shapes.append((top_body, top_shape))

    # 중간 가로 막대 (바디와 모양 생성)
    middle_bar_vertices = [
        (-half_width, 0 - half_thickness),
        (half_width, 0 - half_thickness),
        (half_width, 0 + half_thickness),
        (-half_width, 0 + half_thickness),
    ]
    middle_body = pymunk.Body(mass, pymunk.moment_for_poly(mass, middle_bar_vertices))
    middle_shape = pymunk.Poly(middle_body, middle_bar_vertices)
    middle_shape.color = pygame.Color(color)
    middle_shape.filter = pymunk.ShapeFilter(mask=mask)
    middle_body.position = position
    middle_body.angle = angle
    middle_body.friction = 1
    self.space.add(middle_body, middle_shape)
    bodies_and_shapes.append((middle_body, middle_shape))

    # 하단 가로 막대 (바디와 모양 생성)
    bottom_bar_vertices = [
        (-half_width, -half_height - half_thickness),
        (half_width, -half_height - half_thickness),
        (half_width, -half_height + half_thickness),
        (-half_width, -half_height + half_thickness),
    ]
    bottom_body = pymunk.Body(mass, pymunk.moment_for_poly(mass, bottom_bar_vertices))
    bottom_shape = pymunk.Poly(bottom_body, bottom_bar_vertices)
    bottom_shape.color = pygame.Color(color)
    bottom_shape.filter = pymunk.ShapeFilter(mask=mask)
    bottom_body.position = position
    bottom_body.angle = angle
    bottom_body.friction = 1
    self.space.add(bottom_body, bottom_shape)
    bodies_and_shapes.append((bottom_body, bottom_shape))

    # 왼쪽 세로 막대 (바디와 모양 생성)
    left_bar_vertices = [
        (-half_width - half_thickness, 0 + half_thickness),
        (-half_width + half_thickness, 0 + half_thickness),
        (-half_width + half_thickness, -half_height + half_thickness),
        (-half_width - half_thickness, -half_height + half_thickness),
    ]
    left_body = pymunk.Body(mass, pymunk.moment_for_poly(mass, left_bar_vertices))
    left_shape = pymunk.Poly(left_body, left_bar_vertices)
    left_shape.color = pygame.Color(color)
    left_shape.filter = pymunk.ShapeFilter(mask=mask)
    left_body.position = position
    left_body.angle = angle
    left_body.friction = 1
    self.space.add(left_body, left_shape)
    bodies_and_shapes.append((left_body, left_shape))

    return bodies_and_shapes  # 필요 시 바디와 모양을 참조하기 위해 반환합니다.
