import pymunk
import pygame
import math

def add_shape(self, shape_type, position, angle, scale=50, color='LightSlateGray', mask=pymunk.ShapeFilter.ALL_MASKS(), body_type=pymunk.Body.DYNAMIC):
    mass = 1
    body = pymunk.Body()
    total_inertia = 0
    scale = scale * 2

    if shape_type == 'ellipse':
        width = scale * 2
        height = scale
        ellipse_vertices = [
            (width * 0.5 * math.cos(theta), height * 0.5 * math.sin(theta))
            for theta in [i * (2 * math.pi / 32) for i in range(32)]
        ]
        shape = pymunk.Poly(body, ellipse_vertices)
        inertia = pymunk.moment_for_poly(mass, ellipse_vertices)
    elif shape_type == 'rectangle':
        width = scale * 2
        height = scale
        vertices = [
            (-width / 2, -height / 2),
            (width / 2, -height / 2),
            (width / 2, height / 2),
            (-width / 2, height / 2),
        ]
        shape = pymunk.Poly(body, vertices)
        inertia = pymunk.moment_for_poly(mass, vertices)
    elif 'reg' in shape_type:
        which_size = int(shape_type.split('reg')[-1])
        assert which_size > 2, "Regular polygon must have at least 3 sides"
        vertices = [
            (scale * math.cos(i * (2 * math.pi / which_size)),
             scale * math.sin(i * (2 * math.pi / which_size)))
            for i in range(which_size)
        ]
        shape = pymunk.Poly(body, vertices)
        inertia = pymunk.moment_for_poly(mass, vertices)
    else:
        raise ValueError("Unsupported shape type: {}".format(shape_type))

    # Set properties
    total_inertia += inertia
    shape.color = pygame.Color(color)
    if not isinstance(shape, pymunk.Circle):
        shape.filter = pymunk.ShapeFilter(mask=mask)

    # Set body properties
    body.mass = mass
    body.moment = total_inertia
    body.position = position
    body.angle = angle
    body.friction = 1
    body.body_type = body_type

    # Add body and shape to space
    self.space.add(body, shape)

    return body
