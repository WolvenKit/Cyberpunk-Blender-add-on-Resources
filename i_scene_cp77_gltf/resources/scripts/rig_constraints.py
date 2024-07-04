# A script to apply copy rotation constraints to all bones with the same name in one armature to another

import bpy

sourcearm = "SourceArmature" ## replace SourceArmature with the name of the armature the constraints should be applied to 
targetarm = "TargetArmature" ## replace TargetArmature with the name of the armature to constrain to 

if sourcearm in bpy.data.objects and targetarm in bpy.data.objects:
    src_arm = bpy.data.objects[sourcearm]
    tgt_arm = bpy.data.objects[targetarm]

    for src_bone in src_arm.pose.bones:
        if src_bone.name in tgt_arm.pose.bones:
            copy_constraint = tgt_arm.pose.bones[src_bone.name].constraints.new('COPY_ROTATION')
            copy_constraint.target = src_arm
            copy_constraint.subtarget = src_bone.name
    print("Copy rotation constraints applied successfully.")
else:
    print("One or both armatures not found in the scene.")
