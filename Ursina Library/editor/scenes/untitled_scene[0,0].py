
class Scene(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Entity(parent=self, position=Vec3(-1.3587, 0.032, 1.0418), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-2.2072, 1.5801, -1.6211), scale=Vec3(2.0645, 3.3151, 2.0645), model='diamond', origin=Vec3(0, -0.5, 0), shader='matcap_shader', texture='sky_sunset', color=color.white, )
        Entity(parent=self, position=Vec3(3.27829, 3.10035, -2.9419), scale=Vec3(1.26204, 1.2617, 1.32665), model='sphere', origin=Vec3(0, -0.5, 0), shader='normals_shader', color=color.white, )
        PokeShape(parent=self, position=Vec3(-1.35646, 0.44662, -3.19325), shader='lit_with_shadows_shader', texture='grass', color=color.white, points=[Vec3(-7.3357, 0.000999391, -3.77637), Vec3(-4.30231, 0.000997722, -8.43793), Vec3(2.05479, 0.0014984, -8.07026), Vec3(5.90676, 0, -7.98567), Vec3(4.53698, 0.0020012, -2.74367), Vec3(4.211, 0.00199896, 4.88175), Vec3(-3.13966, 0, 6.57585), Vec3(-7.71829, 0.0010013, 1.87861)], )
        PokeShape(parent=self, position=Vec3(-0.37176, -0.01124, 0.97381), rotation=Vec3(0, 27.8437, 0), shader='lit_with_shadows_shader', texture='grass', color=color.white, points=[Vec3(-7.79579, 0, -4.98429), Vec3(4.0883, 0, -3.73695), Vec3(5.75721, 0.00100046, 0.779251), Vec3(5.73138, 0, 6.07817), Vec3(2.51629, 0.000999451, 9.67638), Vec3(-3.13966, 0, 6.57585)], )
        PokeShape(parent=self, position=Vec3(3.87398, -0.86933, -6.31747), rotation=Vec3(0, 27.8437, 0), shader='lit_with_shadows_shader', texture='grass', color=color.white, points=[Vec3(-7.79579, 0, -4.98429), Vec3(4.0883, 0, -3.73695), Vec3(5.75721, 0.00100046, 0.779251), Vec3(5.73138, 0, 6.07817), Vec3(2.51629, 0.000999451, 9.67638), Vec3(-3.13966, 0, 6.57585)], )
        Entity(parent=self, position=Vec3(-3.94621, 0.469049, 0.89991), scale=Vec3(1.64058, 1.64058, 1.64058), model='cube', origin=Vec3(0, -0.5, 0), shader='triplanar_shader', texture='sky_default', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-1.65768, 0.032, 3.55647), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-0.07, 0.032, 1.343), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-2.52262, 0.26793, -3.37339), rotation=Vec3(-2.68895, -4.86919, 0), scale=Vec3(1, 1.47187, 1), model='cube', origin=Vec3(0, -0.5, 0), shader='matcap_shader', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-1.2686, 0.31124, -3.34212), rotation=Vec3(-2.68895, -6.25, 0), scale=Vec3(1, 2.07546, 1), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', texture='brick', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-3.77403, 0.05084, -3.37339), rotation=Vec3(-0.290699, -9.44767, 0), scale=Vec3(1, 1.0377, 1), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', texture='brick', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-5.05155, 0.31294, -3.39142), rotation=Vec3(3.77907, 29.2878, 0), scale=Vec3(1, 1.56189, 1.03606), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', texture='brick', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-5.05155, 0.34537, -4.95027), rotation=Vec3(-0.145351, -31.3954, 0), scale=Vec3(1, 1.62675, 1), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', texture='brick', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-2.52262, 0.05421, -4.95027), rotation=Vec3(-5.08721, -4.65117, 0), scale=Vec3(1, 1.04443, 1), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', texture='brick', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-3.77403, 0.21806, -4.95027), rotation=Vec3(-6.03198, -13.3721, 0), scale=Vec3(1, 1.37213, 1), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', texture='brick', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-5.05155, 0.19428, -6.57237), rotation=Vec3(-3.63372, 14.3169, 0), scale=Vec3(1, 1.32456, 1), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', texture='brick', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-1.64195, -0.02037, -6.57237), rotation=Vec3(0.436045, -6.32268, 0), scale=Vec3(2.76135, 0.895258, 1), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', texture='brick', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-3.77403, 0.09065, -6.57237), rotation=Vec3(-3.70639, 11.5552, 0), scale=Vec3(1, 1.11731, 1), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', texture='brick', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-5.05155, 0.49679, -8.2112), rotation=Vec3(-2.18023, 4.86919, 0), scale=Vec3(1, 1.92959, 1), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', texture='brick', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-2.52262, -0.05909, -8.2112), rotation=Vec3(9.6657, -5.74128, 0), scale=Vec3(1, 0.817806, 1), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', texture='brick', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(-3.74471, -0.13274, -8.2112), rotation=Vec3(-0.43605, 9.01163, 0), scale=Vec3(1.05863, 0.670514, 1), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', texture='brick', color=color.white, collider='box', )
        Entity(parent=self, position=Vec3(1.75246, 0.032, 1.41679), model='cube', origin=Vec3(0, -0.5, 0), shader='lit_with_shadows_shader', color=color.white, collider='box', )
        PokeShape(parent=self, position=Vec3(11.7381, -0.01124, 18.6926), rotation=Vec3(0, 27.8437, 0), shader='lit_with_shadows_shader', texture='grass', color=color.white, points=[Vec3(-7.79579, 0, -4.98429), Vec3(4.0883, 0, -3.73695), Vec3(5.75721, 0.00100046, 0.779251), Vec3(5.73138, 0, 6.07817), Vec3(2.51629, 0.000999451, 9.67638), Vec3(-3.13966, 0, 6.57585)], )
        PokeShape(parent=self, position=Vec3(11.7381, -0.01124, 18.6926), rotation=Vec3(0, 27.8437, 0), shader='lit_with_shadows_shader', texture='grass', color=color.white, points=[Vec3(-7.79579, 0, -4.98429), Vec3(4.0883, 0, -3.73695), Vec3(5.75721, 0.00100046, 0.779251), Vec3(5.73138, 0, 6.07817), Vec3(2.51629, 0.000999451, 9.67638), Vec3(-3.13966, 0, 6.57585)], )
