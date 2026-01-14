"""
Feathered Inpaint Mask Node
Creates a mask with soft edges for inpainting while preserving original pixels outside the feather zone
"""
import torch
import numpy as np
from scipy.ndimage import distance_transform_edt

class FeatheredInpaintMask:
    """
    Creates a feathered mask for inpainting with three zones:
    1. Full inpaint (mask = 1.0)
    2. Feathered blend (mask = 0.0 to 1.0 gradient)
    3. Preserve original (mask = 0.0) - untouched pixels
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask": ("MASK",),
                "feather_pixels": ("INT", {
                    "default": 10,
                    "min": 0,
                    "max": 100,
                    "step": 1,
                    "display": "slider",
                }),
                "feather_falloff": (["linear", "smooth", "smoother"], {
                    "default": "smooth",
                }),
            },
        }
    
    RETURN_TYPES = ("MASK", "MASK", "MASK")
    RETURN_NAMES = ("feathered_mask", "inpaint_zone", "preserve_zone")
    FUNCTION = "create_feathered_mask"
    CATEGORY = "mask/inpaint"
    
    def create_feathered_mask(self, mask, feather_pixels, feather_falloff):
        if isinstance(mask, torch.Tensor):
            mask_np = mask.cpu().numpy()
        else:
            mask_np = mask
        
        if len(mask_np.shape) == 2:
            mask_np = mask_np[np.newaxis, ...]
        
        batch_size = mask_np.shape[0]
        feathered_masks = []
        inpaint_zones = []
        preserve_zones = []
        
        for i in range(batch_size):
            single_mask = mask_np[i]
            binary_mask = (single_mask > 0.5).astype(np.float32)
            
            if feather_pixels == 0:
                feathered = binary_mask
                inpaint = binary_mask
                preserve = 1.0 - binary_mask
            else:
                dist_inside = distance_transform_edt(binary_mask)
                feathered = np.zeros_like(binary_mask)
                full_inpaint = dist_inside > feather_pixels
                feathered[full_inpaint] = 1.0
                feather_zone = (dist_inside > 0) & (dist_inside <= feather_pixels)
                
                if np.any(feather_zone):
                    gradient = dist_inside[feather_zone] / feather_pixels
                    if feather_falloff == "linear":
                        gradient_curved = gradient
                    elif feather_falloff == "smooth":
                        gradient_curved = gradient * gradient * (3.0 - 2.0 * gradient)
                    else:
                        gradient_curved = gradient * gradient * gradient * (gradient * (gradient * 6.0 - 15.0) + 10.0)
                    feathered[feather_zone] = gradient_curved
                
                inpaint = (feathered > 0).astype(np.float32)
                preserve = (feathered == 0).astype(np.float32)
            
            feathered_masks.append(feathered)
            inpaint_zones.append(inpaint)
            preserve_zones.append(preserve)
        
        feathered_result = np.stack(feathered_masks, axis=0)
        inpaint_result = np.stack(inpaint_zones, axis=0)
        preserve_result = np.stack(preserve_zones, axis=0)
        
        feathered_tensor = torch.from_numpy(feathered_result).float()
        inpaint_tensor = torch.from_numpy(inpaint_result).float()
        preserve_tensor = torch.from_numpy(preserve_result).float()
        
        return (feathered_tensor, inpaint_tensor, preserve_tensor)


class PreserveOriginalPixels:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "original_image": ("IMAGE",),
                "inpainted_image": ("IMAGE",),
                "feathered_mask": ("MASK",),
            },
        }
    
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("result",)
    FUNCTION = "preserve_pixels"
    CATEGORY = "image/inpaint"
    
    def preserve_pixels(self, original_image, inpainted_image, feathered_mask):
        if len(feathered_mask.shape) == 2:
            feathered_mask = feathered_mask.unsqueeze(0).unsqueeze(-1)
        elif len(feathered_mask.shape) == 3:
            feathered_mask = feathered_mask.unsqueeze(-1)
        
        if feathered_mask.shape[-1] == 1:
            feathered_mask = feathered_mask.expand(-1, -1, -1, original_image.shape[-1])
        
        result = original_image * (1.0 - feathered_mask) + inpainted_image * feathered_mask
        return (result,)


NODE_CLASS_MAPPINGS = {
    "FeatheredInpaintMask": FeatheredInpaintMask,
    "PreserveOriginalPixels": PreserveOriginalPixels,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FeatheredInpaintMask": "Feathered Inpaint Mask 🎨",
    "PreserveOriginalPixels": "Preserve Original Pixels 🔒",
}
