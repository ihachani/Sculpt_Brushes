import bpy
import os


root = bpy.utils.script_path_user()
sep = os.sep


#check if IK in data
ikbrushexist = False  
for item in bpy.data.brushes:
    if item.name.endswith("IK"):
        ikbrushexist = True  
    
    
#Load / reload IK Brushes
#Libraries Brushes
if ikbrushexist == False:  
    filepath = root + sep + "addons" + sep + "sculpt_brushes" + sep + "Brushes_IK.blend"
    #Load IK Brushes 
    if bpy.context.scene:
        with bpy.data.libraries.load(filepath) as (data_from, data_to):
            data_to.brushes = [name for name in data_from.brushes if name.endswith("IK")]

else:
    #remove Brushes IK
    activeBrush = bpy.context.tool_settings.sculpt.brush.name
    for item in bpy.data.brushes:
        if item.name != activeBrush:
            if item.name.endswith("IK"):
                brush = item
                print(brush)
                bpy.data.brushes.remove(brush)

#Load script main_brush.py
def execscript():
    lien = root + sep + "addons" + sep + "sculpt_brushes" + sep + "main_brush.py"
    bpy.ops.script.python_file_run( filepath = lien )


#remove texturs
for textures in bpy.data.textures:
    if not textures.users:
        bpy.data.textures.remove(textures)                



#Load script main_brush.py
execscript()