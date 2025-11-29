from PIL import Image

def jpg_to_gif(input_path, output_path):
    """Converts JPG to GIF."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'gif')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 JPG 转换为 GIF 时出错: {e}"

def gif_to_jpg(input_path, output_path):
    """Converts the first frame of a GIF to JPG."""
    try:
        img = Image.open(input_path)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        img.save(output_path, 'jpeg')
        return f"成功！图像的第一帧已保存到 {output_path}"
    except Exception as e:
        return f"从 GIF 转换为 JPG 时出错: {e}"
