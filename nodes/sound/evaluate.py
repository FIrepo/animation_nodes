import bpy
from ... base_types.node import AnimationNode

class EvaluateSoundNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_EvaluateSoundNode"
    bl_label = "Evaluate Sound"

    def create(self):
        self.inputs.new("an_SoundSocket", "Sound", "sound")
        self.inputs.new("an_FloatSocket", "Frame", "frame")
        self.outputs.new("an_FloatSocket", "Strength", "strength")

    def execute(self, sound, frame):
        if sound is None: return 0
        if sound.type != "Single": return 0
        return sound.evaluate(int(frame))
