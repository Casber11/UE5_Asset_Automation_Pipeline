import unreal
from unreal import EditorActorSubsystem

actor_system = unreal.get_editor_subsystem(EditorActorSubsystem)

all_actors = actor_system.get_all_level_actors()

same_name_meshes_groups = []

for actor in all_actors:
    if not isinstance(actor, unreal.StaticMeshActor):
        continue

    found = False

    for group in same_name_meshes_groups:
        if actor.static_mesh_component.static_mesh.get_name() == group[0].static_mesh_component.static_mesh.get_name():
            found = True
            group.append(actor)
            break

    if not found:
        same_name_meshes_groups.append([actor])

same_name_meshes_groups = [a for a in same_name_meshes_groups if len(a) >= 2]

overlapping_meshes_groups = []

for group in same_name_meshes_groups:
    matched_indexes = []

    for i in range(len(group) -1, -1, -1):
        if i in matched_indexes:
            continue

        first = group[i]
        nearby_actors = [first]
        group.pop(i)

        for j in range(len(group) -1, -1, -1):
            if j in matched_indexes:
                continue

            second = group[j]

            if first.get_actor_transform().is_near_equal(second.get_actor_transform()):
                nearby_actors.append(second)
                matched_indexes.append(j)

        if len(nearby_actors) > 1:
            overlapping_meshes_groups.append(nearby_actors)

apply_destroy = True

if len(overlapping_meshes_groups) == 0:
    print("=== There is no overlapping meshes")
else:
    for group in overlapping_meshes_groups:
        for actor in group:
            print(f"=== overlapping meshes : {actor.get_actor_label()}, transform : {actor.get_actor_transform().translation}")

        if apply_destroy:
            to_destroy_actors = group[:-1]
            for actor in to_destroy_actors:
                print(f"=== destroyed : {actor.get_actor_label()}")
                actor_system.destroy_actor(actor)

        print(20* "_")
