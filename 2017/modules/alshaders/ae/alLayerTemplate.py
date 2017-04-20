import pymel.core as pm
from alShaders import *

class AEalLayerTemplate(alShadersTemplate):
	controls = {}
	params = {}
	def setup(self):
		self.params.clear()
		self.params["layer1"] = Param("layer1", "Layer 1", "The bottom layer to blend.", "rgb", presets=None)
		self.params["layer2"] = Param("layer2", "Layer 2", "The top layer to blend.", "rgb", presets=None)
		self.params["mix"] = Param("mix", "Mix", "The amount to blend from the bottom layer to the top.", "float", presets=None)
		self.params["debug"] = Param("debug", "Debug", "Allows you to quickly preview each layer and the mix value.", "enum", presets=None)
		self.params["standardCompatibleAOVs"] = Param("standardCompatibleAOVs", "Write standard AOVs only", "", "bool", presets=None)
		self.params["aov_diffuse_color"] = Param("aov_diffuse_color", "Diffuse color", "", "rgb", presets=None)
		self.params["aov_direct_diffuse"] = Param("aov_direct_diffuse", "Direct diffuse", "", "rgb", presets=None)
		self.params["aov_direct_diffuse_raw"] = Param("aov_direct_diffuse_raw", "Direct diffuse (raw)", "", "rgb", presets=None)
		self.params["aov_indirect_diffuse"] = Param("aov_indirect_diffuse", "Indirect diffuse", "", "rgb", presets=None)
		self.params["aov_indirect_diffuse_raw"] = Param("aov_indirect_diffuse_raw", "Indirect diffuse (raw)", "", "rgb", presets=None)
		self.params["aov_direct_backlight"] = Param("aov_direct_backlight", "Direct backlight", "", "rgb", presets=None)
		self.params["aov_indirect_backlight"] = Param("aov_indirect_backlight", "Indirect backlight", "", "rgb", presets=None)
		self.params["aov_direct_specular"] = Param("aov_direct_specular", "Direct specular", "", "rgb", presets=None)
		self.params["aov_indirect_specular"] = Param("aov_indirect_specular", "Indirect specular", "", "rgb", presets=None)
		self.params["aov_direct_specular_2"] = Param("aov_direct_specular_2", "Direct specular 2", "", "rgb", presets=None)
		self.params["aov_indirect_specular_2"] = Param("aov_indirect_specular_2", "Indirect specular 2", "", "rgb", presets=None)
		self.params["aov_single_scatter"] = Param("aov_single_scatter", "Single scatter", "", "rgb", presets=None)
		self.params["aov_sss"] = Param("aov_sss", "SSS", "", "rgb", presets=None)
		self.params["aov_refraction"] = Param("aov_refraction", "Refraction", "", "rgb", presets=None)
		self.params["aov_emission"] = Param("aov_emission", "Emission", "", "rgb", presets=None)
		self.params["aov_uv"] = Param("aov_uv", "UV", "", "rgb", presets=None)
		self.params["aov_depth"] = Param("aov_depth", "Depth", "", "rgb", presets=None)
		self.params["aov_light_group_1"] = Param("aov_light_group_1", "Light group [1]", "", "rgb", presets=None)
		self.params["aov_light_group_2"] = Param("aov_light_group_2", "Light group [2]", "", "rgb", presets=None)
		self.params["aov_light_group_3"] = Param("aov_light_group_3", "Light group [3]", "", "rgb", presets=None)
		self.params["aov_light_group_4"] = Param("aov_light_group_4", "Light group [4]", "", "rgb", presets=None)
		self.params["aov_light_group_5"] = Param("aov_light_group_5", "Light group [5]", "", "rgb", presets=None)
		self.params["aov_light_group_6"] = Param("aov_light_group_6", "Light group [6]", "", "rgb", presets=None)
		self.params["aov_light_group_7"] = Param("aov_light_group_7", "Light group [7]", "", "rgb", presets=None)
		self.params["aov_light_group_8"] = Param("aov_light_group_8", "Light group [8]", "", "rgb", presets=None)
		self.params["aov_light_group_9"] = Param("aov_light_group_9", "Light group [9]", "", "rgb", presets=None)
		self.params["aov_light_group_10"] = Param("aov_light_group_10", "Light group [10]", "", "rgb", presets=None)
		self.params["aov_light_group_11"] = Param("aov_light_group_11", "Light group [11]", "", "rgb", presets=None)
		self.params["aov_light_group_12"] = Param("aov_light_group_12", "Light group [12]", "", "rgb", presets=None)
		self.params["aov_light_group_13"] = Param("aov_light_group_13", "Light group [13]", "", "rgb", presets=None)
		self.params["aov_light_group_14"] = Param("aov_light_group_14", "Light group [14]", "", "rgb", presets=None)
		self.params["aov_light_group_15"] = Param("aov_light_group_15", "Light group [15]", "", "rgb", presets=None)
		self.params["aov_light_group_16"] = Param("aov_light_group_16", "Light group [16]", "", "rgb", presets=None)
		self.params["aov_id_1"] = Param("aov_id_1", "ID [1]", "", "rgb", presets=None)
		self.params["aov_id_2"] = Param("aov_id_2", "ID [2]", "", "rgb", presets=None)
		self.params["aov_id_3"] = Param("aov_id_3", "ID [3]", "", "rgb", presets=None)
		self.params["aov_id_4"] = Param("aov_id_4", "ID [4]", "", "rgb", presets=None)
		self.params["aov_id_5"] = Param("aov_id_5", "ID [5]", "", "rgb", presets=None)
		self.params["aov_id_6"] = Param("aov_id_6", "ID [6]", "", "rgb", presets=None)
		self.params["aov_id_7"] = Param("aov_id_7", "ID [7]", "", "rgb", presets=None)
		self.params["aov_id_8"] = Param("aov_id_8", "ID [8]", "", "rgb", presets=None)
		self.params["aov_crypto_asset"] = Param("aov_crypto_asset", "Crypto Asset", "", "rgb", presets=None)
		self.params["aov_crypto_object"] = Param("aov_crypto_object", "Crypto Object", "", "rgb", presets=None)
		self.params["aov_crypto_material"] = Param("aov_crypto_material", "Crypto Material", "", "rgb", presets=None)
		self.params["aov_shadow_group_1"] = Param("aov_shadow_group_1", "Shadow group [1]", "", "rgba", presets=None)
		self.params["aov_shadow_group_2"] = Param("aov_shadow_group_2", "Shadow group [2]", "", "rgba", presets=None)
		self.params["aov_shadow_group_3"] = Param("aov_shadow_group_3", "Shadow group [3]", "", "rgba", presets=None)
		self.params["aov_shadow_group_4"] = Param("aov_shadow_group_4", "Shadow group [4]", "", "rgba", presets=None)
		self.params["aov_shadow_group_5"] = Param("aov_shadow_group_5", "Shadow group [5]", "", "rgba", presets=None)
		self.params["aov_shadow_group_6"] = Param("aov_shadow_group_6", "Shadow group [6]", "", "rgba", presets=None)
		self.params["aov_shadow_group_7"] = Param("aov_shadow_group_7", "Shadow group [7]", "", "rgba", presets=None)
		self.params["aov_shadow_group_8"] = Param("aov_shadow_group_8", "Shadow group [8]", "", "rgba", presets=None)

		self.addSwatch()
		self.beginScrollLayout()

		self.addCustomRgb("layer1")
		self.addCustomRgb("layer2")
		self.addCustomFlt("mix")
		self.addControl("debug", label="Debug", annotation="Allows you to quickly preview each layer and the mix value.")
		self.beginLayout("AOVs", collapse=True)
		self.addControl("standardCompatibleAOVs", label="Write standard AOVs only", annotation="")
		self.addControl("aov_diffuse_color", label="Diffuse color", annotation="")
		self.addControl("aov_direct_diffuse", label="Direct diffuse", annotation="")
		self.addControl("aov_direct_diffuse_raw", label="Direct diffuse (raw)", annotation="")
		self.addControl("aov_indirect_diffuse", label="Indirect diffuse", annotation="")
		self.addControl("aov_indirect_diffuse_raw", label="Indirect diffuse (raw)", annotation="")
		self.addControl("aov_direct_backlight", label="Direct backlight", annotation="")
		self.addControl("aov_indirect_backlight", label="Indirect backlight", annotation="")
		self.addControl("aov_direct_specular", label="Direct specular", annotation="")
		self.addControl("aov_indirect_specular", label="Indirect specular", annotation="")
		self.addControl("aov_direct_specular_2", label="Direct specular 2", annotation="")
		self.addControl("aov_indirect_specular_2", label="Indirect specular 2", annotation="")
		self.addControl("aov_single_scatter", label="Single scatter", annotation="")
		self.addControl("aov_sss", label="SSS", annotation="")
		self.addControl("aov_refraction", label="Refraction", annotation="")
		self.addControl("aov_emission", label="Emission", annotation="")
		self.addControl("aov_uv", label="UV", annotation="")
		self.addControl("aov_depth", label="Depth", annotation="")
		self.addControl("aov_light_group_1", label="Light group [1]", annotation="")
		self.addControl("aov_light_group_2", label="Light group [2]", annotation="")
		self.addControl("aov_light_group_3", label="Light group [3]", annotation="")
		self.addControl("aov_light_group_4", label="Light group [4]", annotation="")
		self.addControl("aov_light_group_5", label="Light group [5]", annotation="")
		self.addControl("aov_light_group_6", label="Light group [6]", annotation="")
		self.addControl("aov_light_group_7", label="Light group [7]", annotation="")
		self.addControl("aov_light_group_8", label="Light group [8]", annotation="")
		self.addControl("aov_light_group_9", label="Light group [9]", annotation="")
		self.addControl("aov_light_group_10", label="Light group [10]", annotation="")
		self.addControl("aov_light_group_11", label="Light group [11]", annotation="")
		self.addControl("aov_light_group_12", label="Light group [12]", annotation="")
		self.addControl("aov_light_group_13", label="Light group [13]", annotation="")
		self.addControl("aov_light_group_14", label="Light group [14]", annotation="")
		self.addControl("aov_light_group_15", label="Light group [15]", annotation="")
		self.addControl("aov_light_group_16", label="Light group [16]", annotation="")
		self.addControl("aov_id_1", label="ID [1]", annotation="")
		self.addControl("aov_id_2", label="ID [2]", annotation="")
		self.addControl("aov_id_3", label="ID [3]", annotation="")
		self.addControl("aov_id_4", label="ID [4]", annotation="")
		self.addControl("aov_id_5", label="ID [5]", annotation="")
		self.addControl("aov_id_6", label="ID [6]", annotation="")
		self.addControl("aov_id_7", label="ID [7]", annotation="")
		self.addControl("aov_id_8", label="ID [8]", annotation="")
		self.addControl("aov_crypto_asset", label="Crypto Asset", annotation="")
		self.addControl("aov_crypto_object", label="Crypto Object", annotation="")
		self.addControl("aov_crypto_material", label="Crypto Material", annotation="")
		self.addControl("aov_shadow_group_1", label="Shadow group [1]", annotation="")
		self.addControl("aov_shadow_group_2", label="Shadow group [2]", annotation="")
		self.addControl("aov_shadow_group_3", label="Shadow group [3]", annotation="")
		self.addControl("aov_shadow_group_4", label="Shadow group [4]", annotation="")
		self.addControl("aov_shadow_group_5", label="Shadow group [5]", annotation="")
		self.addControl("aov_shadow_group_6", label="Shadow group [6]", annotation="")
		self.addControl("aov_shadow_group_7", label="Shadow group [7]", annotation="")
		self.addControl("aov_shadow_group_8", label="Shadow group [8]", annotation="")
		self.endLayout() # END AOVs

		pm.mel.AEdependNodeTemplate(self.nodeName)
		self.addExtraControls()

		self.endScrollLayout()
