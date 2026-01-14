"""
ComfyUI SMPL-X Export Nodes
Export SMPL parameters to SMPL-X format for match move tracking
"""

import os
import json
import torch
import numpy as np
from pathlib import Path

class SaveSMPLXParams:
    """Save SMPL parameters in SMPL-X compatible format"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "smpl_params": ("SMPL_PARAMS",),
                "filename_prefix": ("STRING", {"default": "motion_capture"}),
                "format": (["npz", "json", "pkl"], {"default": "npz"}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("file_path",)
    FUNCTION = "save_params"
    CATEGORY = "SMPL-X"
    OUTPUT_NODE = True
    
    def save_params(self, smpl_params, filename_prefix, format):
        """Save SMPL parameters to file"""
        
        # Create output directory
        output_dir = Path("output/smplx")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate filename
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename_prefix}_{timestamp}.{format}"
        filepath = output_dir / filename
        
        # Convert SMPL params to dict
        if isinstance(smpl_params, dict):
            params_dict = smpl_params
        else:
            # Extract from WHAM output
            params_dict = {
                "body_pose": smpl_params.get("body_pose", None),
                "global_orient": smpl_params.get("global_orient", None),
                "betas": smpl_params.get("betas", None),
                "transl": smpl_params.get("transl", None),
            }
        
        # Convert tensors to numpy
        params_numpy = {}
        for key, value in params_dict.items():
            if value is not None:
                if torch.is_tensor(value):
                    params_numpy[key] = value.cpu().numpy()
                else:
                    params_numpy[key] = np.array(value)
        
        # Save based on format
        if format == "npz":
            np.savez(str(filepath), **params_numpy)
        elif format == "json":
            # Convert numpy arrays to lists for JSON
            json_dict = {k: v.tolist() for k, v in params_numpy.items()}
            with open(filepath, 'w') as f:
                json.dump(json_dict, f, indent=2)
        elif format == "pkl":
            import pickle
            with open(filepath, 'wb') as f:
                pickle.dump(params_numpy, f)
        
        print(f"[SMPL-X Export] Saved parameters to: {filepath}")
        return (str(filepath),)


class ExportSMPLXMesh:
    """Export SMPL-X mesh using official SMPL-X library"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "smpl_params": ("SMPL_PARAMS",),
                "model_path": ("STRING", {"default": "models/smplx"}),
                "gender": (["neutral", "male", "female"], {"default": "neutral"}),
                "filename_prefix": ("STRING", {"default": "smplx_mesh"}),
                "format": (["obj", "ply", "fbx"], {"default": "obj"}),
            },
            "optional": {
                "frame_index": ("INT", {"default": 0, "min": 0}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("mesh_path",)
    FUNCTION = "export_mesh"
    CATEGORY = "SMPL-X"
    OUTPUT_NODE = True
    
    def export_mesh(self, smpl_params, model_path, gender, filename_prefix, format, frame_index=0):
        """Export SMPL-X mesh using official library"""
        
        try:
            import smplx
        except ImportError:
            print("[SMPL-X Export] ERROR: smplx library not installed!")
            print("[SMPL-X Export] Install with: pip install smplx")
            return ("ERROR: smplx not installed",)
        
        # Create output directory
        output_dir = Path("output/smplx/meshes")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Load SMPL-X model
        model = smplx.create(
            model_path=model_path,
            model_type='smplx',
            gender=gender,
            use_face_contour=False,
            use_pca=False,
            flat_hand_mean=True,
        )
        
        # Extract parameters for specific frame
        body_pose = smpl_params.get("body_pose", None)
        global_orient = smpl_params.get("global_orient", None)
        betas = smpl_params.get("betas", None)
        transl = smpl_params.get("transl", None)
        
        # Handle frame indexing
        if body_pose is not None and len(body_pose.shape) > 2:
            body_pose = body_pose[frame_index:frame_index+1]
        if global_orient is not None and len(global_orient.shape) > 2:
            global_orient = global_orient[frame_index:frame_index+1]
        if transl is not None and len(transl.shape) > 1:
            transl = transl[frame_index:frame_index+1]
        
        # Generate mesh
        output = model(
            body_pose=body_pose,
            global_orient=global_orient,
            betas=betas,
            transl=transl,
            return_verts=True
        )
        
        vertices = output.vertices.detach().cpu().numpy()[0]
        faces = model.faces
        
        # Generate filename
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename_prefix}_frame{frame_index:04d}_{timestamp}.{format}"
        filepath = output_dir / filename
        
        # Export mesh
        if format == "obj":
            self._save_obj(filepath, vertices, faces)
        elif format == "ply":
            self._save_ply(filepath, vertices, faces)
        elif format == "fbx":
            print("[SMPL-X Export] FBX export requires additional libraries")
            return ("ERROR: FBX not supported yet",)
        
        print(f"[SMPL-X Export] Exported mesh to: {filepath}")
        return (str(filepath),)
    
    def _save_obj(self, filepath, vertices, faces):
        """Save mesh as OBJ file"""
        with open(filepath, 'w') as f:
            for v in vertices:
                f.write(f"v {v[0]} {v[1]} {v[2]}\n")
            for face in faces:
                f.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")
    
    def _save_ply(self, filepath, vertices, faces):
        """Save mesh as PLY file"""
        with open(filepath, 'w') as f:
            f.write("ply\n")
            f.write("format ascii 1.0\n")
            f.write(f"element vertex {len(vertices)}\n")
            f.write("property float x\n")
            f.write("property float y\n")
            f.write("property float z\n")
            f.write(f"element face {len(faces)}\n")
            f.write("property list uchar int vertex_indices\n")
            f.write("end_header\n")
            for v in vertices:
                f.write(f"{v[0]} {v[1]} {v[2]}\n")
            for face in faces:
                f.write(f"3 {face[0]} {face[1]} {face[2]}\n")


# Node registration
NODE_CLASS_MAPPINGS = {
    "SaveSMPLXParams": SaveSMPLXParams,
    "ExportSMPLXMesh": ExportSMPLXMesh,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SaveSMPLXParams": "Save SMPL-X Parameters",
    "ExportSMPLXMesh": "Export SMPL-X Mesh",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
