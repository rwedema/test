from pypovray import pypovray, models
from vapory import Sphere, Box, Cone, Scene


def frame(step):


        sphere = Sphere([0, 0, 0], 3, models.custom_sphere_model)
        box_1 = Box([-5, -4, 3], [-3, 4, -3], models.custom_box_model)
        box_2 = Box([-5, 4, -3], [5, 6, 3], models.custom_box_model)
        box_3 = Box([3, 6, 3], [5,-4, -3], models.custom_box_model)
        box_4 = Box([-5, -4, 3], [5, -6, -3], models.custom_box_model)
        cone_1 = Cone([0, 6, 0], 3,
                      [0, 9, 0], 0, models.custom_cone_model)
        cone_2 = Cone([5, 0, 0], 3,
                      [8, 0, 0], 0, models.custom_cone_model)
        cone_3 = Cone([-5, 0, 0], 3,
                      [-8, 0, 0], 0, models.custom_cone_model)
        cone_4 = Cone([0, -6, 0], 3,
                      [0, -9, 0], 0, models.custom_cone_model)


        # Return the Scene object for rendering
        return Scene(models.default_camera,
                     objects=[models.default_light, sphere, box_1, box_2, box_3, box_4, cone_1, cone_2, cone_3, cone_4],
                     included=['colors.inc'])

if __name__ == '__main__':
    # Render as an image
    pypovray.render_scene_to_png(frame)

