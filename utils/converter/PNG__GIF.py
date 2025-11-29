from PIL import Image

def png_to_gif(input_path, output_path):
    """Converts PNG to GIF."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'gif')
        return f"成功！图像已保存到 {output_path}"
    except Exception as e:
        return f"从 PNG 转换为 GIF 时出错: {e}"

def gif_to_png(input_path, output_path):
    """Converts the first frame of a GIF to PNG."""
    try:
        img = Image.open(input_path)
        img.save(output_path, 'png')
        return f"成功！图像的第一帧已保存到 {output_path}"
    except Exception as e:
        return f"从 GIF 转换为 PNG 时出错: {e}"
