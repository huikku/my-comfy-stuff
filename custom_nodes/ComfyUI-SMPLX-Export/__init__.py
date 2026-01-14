"""
ComfyUI SMPL-X Export Nodes - Extended
Export SMPL parameters to animation formats (BVH, FBX, etc.)
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


class ExportSMPLXAnimation:
    """Export SMPL-X animation to BVH or FBX format"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "smpl_params": ("SMPL_PARAMS",),
                "filename_prefix": ("STRING", {"default": "animation"}),
                "format": (["bvh", "fbx"], {"default": "bvh"}),
                "fps": ("FLOAT", {"default": 30.0, "min": 1.0, "max": 120.0}),
            },
            "optional": {
                "model_path": ("STRING", {"default": "models/smplx"}),
                "gender": (["neutral", "male", "female"], {"default": "neutral"}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("file_path",)
    FUNCTION = "export_animation"
    CATEGORY = "SMPL-X"
    OUTPUT_NODE = True
    
    def export_animation(self, smpl_params, filename_prefix, format, fps, model_path="models/smplx", gender="neutral"):
        """Export animation file"""
        
        # Create output directory
        output_dir = Path("output/smplx/animations")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate filename
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename_prefix}_{timestamp}.{format}"
        filepath = output_dir / filename
        
        # Extract parameters
        body_pose = smpl_params.get("body_pose", None)
        global_orient = smpl_params.get("global_orient", None)
        transl = smpl_params.get("transl", None)
        
        # Convert to numpy if needed
        if torch.is_tensor(body_pose):
            body_pose = body_pose.cpu().numpy()
        if torch.is_tensor(global_orient):
            global_orient = global_orient.cpu().numpy()
        if torch.is_tensor(transl):
            transl = transl.cpu().numpy()
        
        if format == "bvh":
            self._export_bvh(filepath, body_pose, global_orient, transl, fps)
        elif format == "fbx":
            print("[SMPL-X Export] FBX export requires additional libraries (fbx-sdk)")
            print("[SMPL-X Export] Falling back to BVH format")
            bvh_path = filepath.with_suffix('.bvh')
            self._export_bvh(bvh_path, body_pose, global_orient, transl, fps)
            filepath = bvh_path
        
        print(f"[SMPL-X Export] Exported animation to: {filepath}")
        return (str(filepath),)
    
    def _export_bvh(self, filepath, body_pose, global_orient, transl, fps):
        """Export to BVH format"""
        
        num_frames = len(body_pose) if body_pose is not None else 1
        frame_time = 1.0 / fps
        
        # SMPL skeleton hierarchy (simplified)
        joints = [
            "Hips", "Spine", "Spine1", "Spine2", "Neck", "Head",
            "LeftShoulder", "LeftArm", "LeftForeArm", "LeftHand",
            "RightShoulder", "RightArm", "RightForeArm", "RightHand",
            "LeftUpLeg", "LeftLeg", "LeftFoot", "LeftToeBase",
            "RightUpLeg", "RightLeg", "RightFoot", "RightToeBase"
        ]
        
        with open(filepath, 'w') as f:
            # Write header
            f.write("HIERARCHY\n")
            f.write("ROOT Hips\n")
            f.write("{\n")
            f.write("  OFFSET 0.0 0.0 0.0\n")
            f.write("  CHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation\n")
            
            # Write simplified skeleton
            self._write_joint(f, "Spine", 1)
            
            f.write("}\n")
            
            # Write motion data
            f.write("MOTION\n")
            f.write(f"Frames: {num_frames}\n")
            f.write(f"Frame Time: {frame_time}\n")
            
            # Write frame data
            for frame in range(num_frames):
                # Root position
                if transl is not None:
                    pos = transl[frame]
                    f.write(f"{pos[0]:.6f} {pos[1]:.6f} {pos[2]:.6f} ")
                else:
                    f.write("0.0 0.0 0.0 ")
                
                # Root rotation
                if global_orient is not None:
                    rot = global_orient[frame]
                    # Convert axis-angle to euler (simplified)
                    f.write(f"{rot[0]*57.3:.6f} {rot[1]*57.3:.6f} {rot[2]*57.3:.6f} ")
                else:
                    f.write("0.0 0.0 0.0 ")
                
                # Body rotations (simplified - just output zeros for now)
                if body_pose is not None:
                    for i in range(21):  # 21 body joints
                        f.write("0.0 0.0 0.0 ")
                
                f.write("\n")
    
    def _write_joint(self, f, name, indent):
        """Write joint hierarchy (simplified)"""
        spaces = "  " * indent
        f.write(f"{spaces}JOINT {name}\n")
        f.write(f"{spaces}{{\n")
        f.write(f"{spaces}  OFFSET 0.0 10.0 0.0\n")
        f.write(f"{spaces}  CHANNELS 3 Zrotation Xrotation Yrotation\n")
        f.write(f"{spaces}  End Site\n")
        f.write(f"{spaces}  {{\n")
        f.write(f"{spaces}    OFFSET 0.0 5.0 0.0\n")
        f.write(f"{spaces}  }}\n")
        f.write(f"{spaces}}}\n")


class ExportSMPLXMeshSequence:
    """Export animated SMPL-X mesh sequence"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "smpl_params": ("SMPL_PARAMS",),
                "model_path": ("STRING", {"default": "models/smplx"}),
                "gender": (["neutral", "male", "female"], {"default": "neutral"}),
                "filename_prefix": ("STRING", {"default": "mesh_seq"}),
                "format": (["obj", "ply"], {"default": "obj"}),
            },
            "optional": {
                "frame_skip": ("INT", {"default": 1, "min": 1, "max": 10}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_dir",)
    FUNCTION = "export_sequence"
    CATEGORY = "SMPL-X"
    OUTPUT_NODE = True
    
    def export_sequence(self, smpl_params, model_path, gender, filename_prefix, format, frame_skip=1):
        """Export mesh sequence (animated mesh)"""
        
        try:
            import smplx
        except ImportError:
            print("[SMPL-X Export] ERROR: smplx library not installed!")
            return ("ERROR: smplx not installed",)
        
        # Create output directory
        output_dir = Path(f"output/smplx/mesh_sequences/{filename_prefix}")
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
        
        # Extract parameters
        body_pose = smpl_params.get("body_pose", None)
        global_orient = smpl_params.get("global_orient", None)
        betas = smpl_params.get("betas", None)
        transl = smpl_params.get("transl", None)
        
        num_frames = len(body_pose) if body_pose is not None else 1
        
        # Export each frame
        for frame in range(0, num_frames, frame_skip):
            # Get frame parameters
            bp = body_pose[frame:frame+1] if body_pose is not None else None
            go = global_orient[frame:frame+1] if global_orient is not None else None
            tr = transl[frame:frame+1] if transl is not None else None
            
            # Generate mesh
            output = model(
                body_pose=bp,
                global_orient=go,
                betas=betas,
                transl=tr,
                return_verts=True
            )
            
            vertices = output.vertices.detach().cpu().numpy()[0]
            faces = model.faces
            
            # Save mesh
            filename = f"{filename_prefix}_{frame:04d}.{format}"
            filepath = output_dir / filename
            
            if format == "obj":
                self._save_obj(filepath, vertices, faces)
            elif format == "ply":
                self._save_ply(filepath, vertices, faces)
            
            if frame % 30 == 0:
                print(f"[SMPL-X Export] Exported frame {frame}/{num_frames}")
        
        print(f"[SMPL-X Export] Exported {num_frames//frame_skip} meshes to: {output_dir}")
        return (str(output_dir),)
    
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
    "ExportSMPLXAnimation": ExportSMPLXAnimation,
    "ExportSMPLXMeshSequence": ExportSMPLXMeshSequence,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SaveSMPLXParams": "Save SMPL-X Parameters",
    "ExportSMPLXAnimation": "Export SMPL-X Animation (BVH/FBX)",
    "ExportSMPLXMeshSequence": "Export SMPL-X Mesh Sequence",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
