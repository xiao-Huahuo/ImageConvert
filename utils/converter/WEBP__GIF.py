from PIL import Image

def webp_to_gif(input_path, output_path):
    """Converts WebP to GIF."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'gif')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 WebP 转换为 GIF 时出错: {e}"

def gif_to_webp(input_path, output_path):
    """Converts the first frame of a GIF to WebP."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'webp', quality=80)
        return f"成功！图像的第一帧已保存到 {output_path}"
    except Exception as e:
        return f"从 GIF 转换为 WebP 时出错: {e}"
