from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
import random
import math

noise = PerlinNoise(octaves=3, seed=random.randint(1, 1000))
cave_noise = PerlinNoise(octaves=3, seed=random.randint(1, 1000))  # Bruit spécifique pour les grottes

app = Ursina()

selected_block = "grass"

player = FirstPersonController(
    mouse_sensitivity=Vec2(100, 100),
    position=(0, 5, 0)
)

block_textures = {
    "grass": load_texture("assets/textures/groundEarth.png"),
    "dirt": load_texture("assets/textures/groundMud.png"),
    "stone": load_texture("assets/textures/wallStone.png"),
    "bedrock": load_texture("assets/textures/stone07.png"),
    "sky_bg": load_texture("assets/textures/Sky.png"),
    "bricks": load_texture("assets/textures/wallBrick01.png"),
    "lava": load_texture("assets/textures/lava01.png"),
    "ice": load_texture("assets/textures/ice01.png"),
    "buisson": load_texture("assets/textures/ground.png"),
    "underground_stone": load_texture("assets/textures/stone05.png")
}

class Block(Entity):
    def __init__(self, position, block_type):
        super().__init__(
            position=position,
            model="assets/models/block_model",
            scale=1,
            origin_y=-0.5,
            texture=block_textures.get(block_type),
            collider="box"
        )
        self.block_type = block_type

mini_block = Entity(
    parent=camera,
    model="assets/models/block_model",
    scale=0.2,
    texture=block_textures.get(selected_block),
    position=(0.35, -0.25, 0.5),
    rotation=(-15, -30, -5)
)

min_height = -10

# Fonction pour générer des grottes
def is_in_cave(x, y, z):
    cave_threshold = 0.4
    noise_value = cave_noise([x * 0.1, y * 0.1, z * 0.1])  # Utilise un bruit de Perlin pour les grottes
    return noise_value > cave_threshold

for x in range(-10, 10):
    for z in range(-10, 10):
        height = noise([x * 0.02, z * 0.02])
        height = math.floor(height * 7.5)
        for y in range(height, min_height - 1, -1):
            # Si nous sommes dans une grotte, ne mettons pas de blocs
            if is_in_cave(x, y, z):
                continue  # Laisser l'espace vide pour la grotte
            if y == min_height:
                block = Block((x, y + min_height, z), "bedrock")
            elif y == height:
                block = Block((x, y + min_height, z), "grass")
            elif height - y > 3:
                block = Block((x, y + min_height, z), "underground_stone")
            elif height - y < 9:
                block = Block((x, y + min_height, z), "stone")
            else:
                block = Block((x, y + min_height, z), "dirt")

def input(key):
    global selected_block
    if key == "right mouse down":
        hit_info = raycast(camera.world_position, camera.forward, distance=10)
        if hit_info.hit:
            distance = math.dist(player.position, hit_info.entity.position)
            if distance <= 4:
                new_position = hit_info.entity.position + hit_info.normal
                block = Block(new_position, selected_block)
    if key == "left mouse down" and mouse.hovered_entity:
        if not mouse.hovered_entity.block_type == "bedrock":
            if  not mouse.hovered_entity.block_type == "lava":
                distance = math.dist(player.position, mouse.hovered_entity.position)
                if distance <= 6:
                    destroy(mouse.hovered_entity)
    if held_keys["escape"]:
        application.quit()
    if key == "1":
        selected_block = "grass"
    if key == '2':
        selected_block = "dirt"
    if key == '3':
        selected_block = "stone"
    if key == '4':
        selected_block = "bricks"
    if key == '5':
        selected_block = "lava"
    if key == '6':
        selected_block = "ice"
    if key == '7':
        selected_block = "buisson"
    if key == 'p':
        print(noise)

def update():
    mini_block.texture = block_textures.get(selected_block)
    if player.y <= -60:
        player.position = (0, 0, 0)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sphere",
            texture="sky_bg",
            scale=150,
            double_sided=True
        )

app.run()
