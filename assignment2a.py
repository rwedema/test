from pypovray import pypovray, models
from vapory import Cylinder, Cone, Scene


def legend(step):
    cylinder_x = Cylinder([-5, 0, 0], [-1, 0, 0], 0.05, models.custom_cylinder_model_x)
    cone_x = Cone([-1, 0, 0],0.3, [0, 0, 0], 0, models.custom_cone_model_x)
    cylinder_y = Cylinder([-5, 0, 0], [-5, 4, 0], 0.05, models.custom_cylinder_model_y)
    cone_y = Cone([-5, 4, 0], 0.3, [-5, 5, 0], 0, models.custom_cone_model_y)
    cylinder_z = Cylinder([-5, 0, 0], [-5, 0, 4], 0.05, models.custom_cylinder_model_z)
    cone_z = Cone([-5, 0, 5], 0.3, [-5, 0, 4], 0, models.custom_cone_model_z)

    return Scene(objects=[models.custom_light_axis, cylinder_x, cone_x, cylinder_y, cone_y, cylinder_z, cone_z],
                 included=['colors.inc'])


