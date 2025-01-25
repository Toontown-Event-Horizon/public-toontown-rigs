import bpy
import fnmatch
import math

bl_info = {
    "name": "Auto Bake Suit Metarig",
    "blender": (3, 15, 0),
    "category": "Object",
}

class BakeIntoMetarig(bpy.types.Operator):
    """Bakes all animations present in the action collection from any rig with the \"suit*\" name to rig named \"rig\""""

    bl_idname = "action.autobakecog"
    bl_label = "Bake Cog Animations"
    bl_options = {'REGISTER', 'UNDO'}
    
    def select_one_object(self, obj):
        bpy.context.area.type = "VIEW_3D"
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.select_all(action="DESELECT")
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode="POSE")
        bpy.ops.pose.select_all(action='SELECT')
                
    def get_keyframes(self, obj):
        keyframes = []
        anim = obj.animation_data
        if anim is not None and anim.action is not None:
            for fcu in anim.action.fcurves:
                for keyframe in fcu.keyframe_points:
                    x, y = keyframe.co
                    if x not in keyframes:
                        keyframes.append((math.ceil(x)))
        keyframes.sort()
        return keyframes
    
    def execute(self, context):
        scene = context.scene
        
        newrig = bpy.data.objects["rig"]
        oldrig = bpy.data.objects[[o.name for o in bpy.data.objects if "suit" in o.name][0]]
        print(newrig)
        print(oldrig)
        actions = [action for action in bpy.data.actions]
            
        # bake all animations for each action we have
        for action in actions:
            self.select_one_object(newrig)
            bpy.ops.pose.transforms_clear()
            oldrig.animation_data.action = action
            
            last_frame = self.get_keyframes(oldrig)[-1]
            
            print(f"doing animation {action.name} of length {last_frame} frames.")
            
            bpy.ops.nla.bake(frame_start=0, frame_end=last_frame, step=2, only_selected=True, visual_keying=True, clean_curves=True)
            
            new_action_name = f"{action.name}"
            bpy.data.actions.remove(action, do_unlink=True)
            
            new_action = newrig.animation_data.action
            new_action.name = new_action_name
            new_action.use_fake_user = True
            
            newrig.animation_data.action = None
            self.select_one_object(oldrig)
            bpy.ops.pose.transforms_clear()
            
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(BakeIntoMetarig.bl_idname)


def register():
    bpy.utils.register_class(BakeIntoMetarig)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(BakeIntoMetarig)


if __name__ == "__main__":
    register()
