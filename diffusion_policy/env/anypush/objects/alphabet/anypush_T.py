import pymunk
import pygame

def add_T(self, position, angle, scale=30, color='LightSlateGray', mask=pymunk.ShapeFilter.ALL_MASKS(), body_type=pymunk.Body.DYNAMIC):
    mass = 1
    length = 4
    vertices1 = [(-length*scale/2, scale),
                                ( length*scale/2, scale),
                                ( length*scale/2, 0),
                                (-length*scale/2, 0)]
    inertia1 = pymunk.moment_for_poly(mass, vertices=vertices1)
    vertices2 = [(-scale/2, scale),
                                (-scale/2, length*scale),
                                ( scale/2, length*scale),
                                ( scale/2, scale)]
    inertia2 = pymunk.moment_for_poly(mass, vertices=vertices1)
    body = pymunk.Body(mass, inertia1 + inertia2)
    shape1 = pymunk.Poly(body, vertices1)
    shape2 = pymunk.Poly(body, vertices2)
    shape1.color = pygame.Color(color)
    shape2.color = pygame.Color(color)
    shape1.filter = pymunk.ShapeFilter(mask=mask)
    shape2.filter = pymunk.ShapeFilter(mask=mask)
    body.center_of_gravity = (shape1.center_of_gravity + shape2.center_of_gravity) / 2
    body.position = position
    body.angle = angle
    body.friction = 1
    body.body_type = body_type
    body.collision_type = 1

    self.space.add(body, shape1, shape2)
    return body
